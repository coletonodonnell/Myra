from operations.universal.abstracts import OSScriptlet

import os
import datetime

# PrintScreen
import win32clipboard
from PIL import Image
from io import BytesIO
from mss import mss, tools

# DiskSpace
from shutil import disk_usage

# WebSearch
from webbrowser import open_new_tab
from urllib.parse import quote

# NetworkMonitor
import subprocess
import re
import concurrent.futures

# CPUUsage, MemoryUsage, ProcessList, BatteryStatus, SystemInfo
import psutil

# ErrorLog
import subprocess

# PortScanner
import socket

# SystemInfo
import platform

# NetworkSpeedTest
import speedtest

# EmptyTrashCan, SecurityScan
import ctypes
import sys


class PrintScreen(OSScriptlet):
    def __init__(self, store_to_clipboard: str):
        self.clipboard: bool = bool(store_to_clipboard)

    def execute(self) -> bool:
        try:
            with mss() as sct:
                # Get first monitor
                monitor = sct.monitors[1]
                now = datetime.datetime.now()

                img = sct.grab(monitor)
                png = tools.to_png(img.rgb, img.size)

                downloads_folder = os.path.join(os.environ["USERPROFILE"], "Downloads")

                filename = now.strftime("Screenshot-%Y-%m-%d_%H-%M-%S.png")
                filepath = os.path.join(downloads_folder, filename)

                with open(filepath, "wb") as file:
                    file.write(png)

                    if self.clipboard:
                        image = Image.open(filepath)
                        output = BytesIO()
                        image.convert("RGB").save(output, "BMP")
                        data = output.getvalue()[14:]
                        output.close()

                        self.send_to_clipboard(win32clipboard.CF_DIB, data)

                return True
        except Exception as e:
            return False

    @staticmethod
    def send_to_clipboard(clip_type, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()


class DiskSpace(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> bool:
        try:
            system_drive = os.environ.get("SystemDrive", "C:")
            path = system_drive + "\\"
            total, used, free = disk_usage(path)

            return (
                f"Disk usage for {path}:\n"
                f"Total: {self.bytes_to_gb(total):.2f} GB\n"
                f"Used:  {self.bytes_to_gb(used):.2f} GB\n"
                f"Free:  {self.bytes_to_gb(free):.2f} GB"
            )

        except Exception:
            return "An error occurred while calculating disk space."

    @staticmethod
    def bytes_to_gb(bytes_value):
        return bytes_value / (2**30)


class WebSearch(OSScriptlet):
    def __init__(self, query: str):
        self.query = query

    def execute(self) -> bool:
        try:
            query_encoded = quote(self.query)
            url = f"https://www.google.com/search?q={query_encoded}"
            open_new_tab(url)
            return True
        except Exception:
            return False


class NetworkMonitor(OSScriptlet):
    def __init__(self, targets=None, count: int = 4):
        # If no targets are provided, use a default list.
        if targets is None:
            targets = ["8.8.8.8", "1.1.1.1", "www.google.com"]
        self.targets = targets
        self.count = count

    def execute(self) -> str:
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_target = {
                executor.submit(self.ping_target, target): target
                for target in self.targets
            }
            for future in concurrent.futures.as_completed(future_to_target):
                target = future_to_target[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as exc:
                    results.append({"target": target, "error": f"Exception: {exc}"})

        return self.format_results(results)

    def ping_target(self, target: str) -> dict:
        """
        Pings the target and returns a dictionary with parsed statistics.
        """
        try:
            output = subprocess.check_output(
                ["ping", target, "-n", str(self.count)],
                universal_newlines=True,
                stderr=subprocess.STDOUT,
            )
            stats = self.parse_ping_output(output)
            stats["target"] = target
            return stats
        except subprocess.CalledProcessError as e:
            return {"target": target, "error": f"Ping failed: {e.output}"}
        except Exception as e:
            return {"target": target, "error": str(e)}

    def parse_ping_output(self, output: str) -> dict:
        """
        Parses the ping command output to extract packet loss and average latency.
        This parser is tailored for Windows ping output.
        """
        result = {}
        # Regex for packet loss: e.g. "Lost = 0 (0% loss)"
        loss_match = re.search(r"Lost = \d+.*\((\d+)% loss\)", output)
        if loss_match:
            result["packet_loss_percent"] = int(loss_match.group(1))
        else:
            result["packet_loss_percent"] = None

        # Regex for average round trip time: e.g. "Average = 15ms"
        avg_match = re.search(r"Average = (\d+)ms", output)
        if avg_match:
            result["avg_latency_ms"] = int(avg_match.group(1))
        else:
            result["avg_latency_ms"] = None

        return result

    def format_results(self, results: list) -> str:
        """
        Formats the aggregated ping results into a summary string.
        """
        report_lines = ["Network Monitor Report:"]
        for res in results:
            target = res.get("target", "Unknown")
            if "error" in res:
                report_lines.append(f"- {target}: Error - {res['error']}")
            else:
                loss = res.get("packet_loss_percent")
                latency = res.get("avg_latency_ms")
                if loss is not None and latency is not None:
                    report_lines.append(
                        f"- {target}: {loss}% packet loss, Average latency {latency}ms"
                    )
                else:
                    report_lines.append(f"- {target}: Unable to parse statistics.")
        return "\n".join(report_lines)


class CPUUsage(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> str:
        try:
            # Measure CPU usage over a 1-second interval
            usage = psutil.cpu_percent(interval=1)
            return f"Current CPU Usage: {usage}%"
        except Exception as e:
            return f"An error occurred while retrieving CPU usage: {e}"


class MemoryUsage(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> str:
        try:
            mem = psutil.virtual_memory()
            return (
                f"Memory Usage: {mem.percent}% used, "
                f"{mem.used / (2**30):.2f} GB used out of {mem.total / (2**30):.2f} GB total."
            )
        except Exception as e:
            return f"An error occurred while retrieving memory usage: {e}"


class ProcessList(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> str:
        try:
            # Iterate over all processes and collect PID and name
            processes = []
            for proc in psutil.process_iter(["pid", "name"]):
                processes.append(proc.info)

            if not processes:
                return "No processes found."

            # Sort processes by PID for readability
            processes_sorted = sorted(processes, key=lambda x: x["pid"])
            output_lines = ["Process List:"]
            for proc in processes_sorted:
                output_lines.append(f"PID {proc['pid']}: {proc['name']}")

            return "\n".join(output_lines)
        except Exception as e:
            return f"An error occurred while retrieving process list: {e}"


class ErrorLog(OSScriptlet):
    def __init__(self, log_type: str = "System", count: int = 10):
        """
        Initialize with the type of log to query and the number of entries to retrieve.

        Args:
            log_type (str): The Windows Event Log to query ("System" or "Application").
            count (int): Number of error log entries to retrieve.
        """
        self.log_type = log_type
        self.count = count

    def execute(self) -> str:
        try:
            # Construct the wevtutil command to query for error logs (Level=2 indicates error)
            command = (
                f'wevtutil qe {self.log_type} /q:"*[System[(Level=2)]]" '
                f"/f:text /c:{self.count}"
            )
            output = subprocess.check_output(
                command, shell=True, universal_newlines=True
            )
            if not output.strip():
                return f"No error logs found in the {self.log_type} log."
            return f"Recent error logs from {self.log_type}:\n\n{output.strip()}"
        except Exception as e:
            return f"An error occurred while retrieving error logs: {e}"


class BatteryStatus(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> str:
        try:
            battery = psutil.sensors_battery()
            if battery is None:
                return "This device does not have a battery."

            percent = battery.percent
            charging = battery.power_plugged
            secs_left = battery.secsleft

            if secs_left == psutil.POWER_TIME_UNLIMITED:
                time_left = "Unlimited"
            elif secs_left == psutil.POWER_TIME_UNKNOWN or secs_left < 0:
                time_left = "Unknown"
            else:
                hours = secs_left // 3600
                minutes = (secs_left % 3600) // 60
                time_left = f"{hours}h {minutes}m"

            return (
                f"Battery Status:\n"
                f"Percentage: {percent}%\n"
                f"Charging: {charging}\n"
                f"Time Left: {time_left}"
            )
        except Exception as e:
            return f"An error occurred while retrieving battery status: {e}"


class PortScanner(OSScriptlet):
    def __init__(self, target: str, ports: list):
        """
        Initialize with the target host and list of ports to scan.

        Args:
            target (str): The IP address or hostname to scan.
            ports (list): List of port numbers to check.
        """
        self.target = target
        self.ports = ports

    def execute(self) -> str:
        result_lines = [f"Scanning {self.target}:"]
        for port in self.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                connection_result = s.connect_ex((self.target, port))
                if connection_result == 0:
                    result_lines.append(f"Port {port}: Open")
                else:
                    result_lines.append(f"Port {port}: Closed")
            except Exception as e:
                result_lines.append(f"Port {port}: Error ({e})")
            finally:
                s.close()
        return "\n".join(result_lines)


class SystemInfo(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> str:
        try:
            os_info: str = (
                "Operating System:\n"
                f"  System: {platform.system()}\n"
                f"  Release: {platform.release()}\n"
                f"  Version: {platform.version()}\n"
                f"  Machine: {platform.machine()}\n"
                f"  Processor: {platform.processor()}\n"
            )

            cpu_info: str = (
                "\nCPU Info:\n"
                f"  Physical cores: {psutil.cpu_count(logical=False)}\n"
                f"  Total cores: {psutil.cpu_count(logical=True)}\n"
            )
            cpufreq = psutil.cpu_freq()
            if cpufreq:
                cpu_info += (
                    f"  Max Frequency: {cpufreq.max:.2f} Mhz\n"
                    f"  Min Frequency: {cpufreq.min:.2f} Mhz\n"
                    f"  Current Frequency: {cpufreq.current:.2f} Mhz\n"
                )
            cpu_info += f"  CPU Usage: {psutil.cpu_percent(interval=1)}%\n"

            memory_info: str = (
                "\nMemory Info:\n"
                f"  Total: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n"
                f"  Available: {psutil.virtual_memory().available / (1024 ** 3):.2f} GB\n"
                f"  Used: {psutil.virtual_memory().used / (1024 ** 3):.2f} GB\n"
                f"  Percentage: {psutil.virtual_memory().percent}%\n"
            )

            disk_info: str = "\nDisk Info:\n"
            partitions = psutil.disk_partitions()
            for partition in partitions:
                disk_info += (
                    f"  === Device: {partition.device} ===\n"
                    f"    Mountpoint: {partition.mountpoint}\n"
                    f"    File system type: {partition.fstype}\n"
                )
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                    disk_info += (
                        f"    Total Size: {partition_usage.total / (1024 ** 3):.2f} GB\n"
                        f"    Used: {partition_usage.used / (1024 ** 3):.2f} GB\n"
                        f"    Free: {partition_usage.free / (1024 ** 3):.2f} GB\n"
                        f"    Percentage: {partition_usage.percent}%\n"
                    )
                except PermissionError:
                    disk_info += "    Permission Denied for this partition.\n"

            return os_info + cpu_info + memory_info + disk_info
        except Exception as e:
            return f"An error occurred while retrieving system information: {e}"


class NetworkSpeedTest(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> str:
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download()  # bits per second
            upload_speed = st.upload()  # bits per second
            ping = st.results.ping

            download_mbps = download_speed / 1e6  # convert to Mbps
            upload_mbps = upload_speed / 1e6  # convert to Mbps

            result: str = (
                "Network Speed Test Results:\n"
                f"Download Speed: {download_mbps:.2f} Mbps\n"
                f"Upload Speed: {upload_mbps:.2f} Mbps\n"
                f"Ping: {ping:.2f} ms"
            )
            return result
        except Exception as e:
            return f"An error occurred during network speed test: {e}"


class EmptyTrashCan(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> str:
        try:
            if sys.platform != "win32":
                return "Empty Trash Can functionality is only supported on Windows."

            # SHEmptyRecycleBinW: https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shemptyrecyclebinw
            # Flags set to 0 for default behavior.
            result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0)
            if result == 0:
                return "Recycle Bin emptied successfully."
            else:
                return f"Failed to empty Recycle Bin. Error code: {result}"
        except Exception as e:
            return f"An error occurred while emptying the Recycle Bin: {e}"


class SecurityScan(OSScriptlet):
    def __init__(self):
        pass

    def execute(self) -> str:
        try:
            if sys.platform != "win32":
                return "Security scan functionality is only supported on Windows."

            # Define the path to the Windows Defender command line utility.
            defender_path = r"C:\Program Files\Windows Defender\MpCmdRun.exe"
            # Using a quick scan (ScanType 1). For a full scan, use ScanType 2.
            command = [defender_path, "-Scan", "-ScanType", "1"]

            # Execute the scan command and capture the output.
            output = subprocess.check_output(
                command, universal_newlines=True, stderr=subprocess.STDOUT
            )
            return f"Security Scan Completed:\n{output}"
        except subprocess.CalledProcessError as e:
            return f"Security scan failed:\n{e.output}"
        except Exception as e:
            return f"An error occurred during the security scan: {e}"
