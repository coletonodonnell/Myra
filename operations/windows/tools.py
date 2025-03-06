from langchain.tools import BaseTool
from typing import Type, List
from pydantic import BaseModel, Field

from operations.windows.osfunctions import (
    PrintScreen,
    DiskSpace,
    WebSearch,
    NetworkMonitor,
    CPUUsage,
    MemoryUsage,
    ProcessList,
    ErrorLog,
    BatteryStatus,
    PortScanner,
    SystemInfo,
    NetworkSpeedTest,
    EmptyTrashCan,
    SecurityScan,
)

class PrintScreenInput(BaseModel):
    clipboard: int = Field(
        description="Whether to place screenshot in clipboard as well. Set to one if true, zero if false",
        default=1,
    )


class PrintScreenTool(BaseTool):
    name: str = "print_screen"
    description: str = (
        "Takes a screenshot of the primary monitor, saves to Downloads, "
        "and optionally copies it to clipboard."
    )
    args_schema: Type[BaseModel] = PrintScreenInput

    def _run(self, clipboard: int) -> str:
        clipboard = bool(clipboard)
        ps: PrintScreen = PrintScreen(clipboard)
        success: bool = ps.execute()
        if success:
            return f"Screenshot taken and saved. Clipboard option = {clipboard}"
        else:
            return "An error occurred during screenshot capture."

    async def _arun(self, clipboard: bool) -> str:
        raise NotImplementedError("Async execution not implemented.")


class DiskSpaceTool(BaseTool):
    name: str = "disk_space"
    description: str = "Return the disk usage for the OS drive."

    def _run(self) -> str:
        ds: DiskSpace = DiskSpace()
        return ds.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")


class WebSearchInput(BaseModel):
    search: str = Field(description="Put the user's search in here")


class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = (
        "Takes a users search and google's it for them using their default web browser."
    )
    args_schema: Type[BaseModel] = WebSearchInput

    def _run(self, search: str) -> str:
        ws: WebSearch = WebSearch(search)
        success: bool = ws.execute()
        if success:
            return f"Searched for {search}."
        else:
            return "An error occurred during searching."

    async def _arun(self, clipboard: bool) -> str:
        raise NotImplementedError("Async execution not implemented.")


class NetworkMonitorInput(BaseModel):
    targets: List[str] = Field(
        default=lambda: ["8.8.8.8", "1.1.1.1", "www.google.com"],
        description="List of targets (IP addresses or hostnames) to ping.",
    )
    count: int = Field(default=4, description="Number of ping attempts per target.")


class NetworkMonitorTool(BaseTool):
    name: str = "network_monitor"
    description: str = (
        "Pings multiple targets concurrently and returns network statistics "
        "such as packet loss and average latency for each target. "
        "Targets are specified as a list of IP addresses or hostnames. "
        "The number of ping attempts per target can also be specified as count."
    )
    args_schema: Type[BaseModel] = NetworkMonitorInput

    def _run(self, targets: List[str], count: int) -> str:
        nm = NetworkMonitor(targets=targets, count=count)
        report = nm.execute()
        return report

    async def _arun(self, targets: List[str], count: int) -> str:
        raise NotImplementedError("Async execution not implemented.")


class CPUUsageTool(BaseTool):
    name: str = "cpu_usage"
    description: str = (
        "Returns the current CPU usage percentage by measuring CPU usage over a 1-second interval."
    )

    def _run(self) -> str:
        cpu = CPUUsage()
        return cpu.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")


class MemoryUsageTool(BaseTool):
    name: str = "memory_usage"
    description: str = (
        "Returns the current memory usage statistics including the percentage of memory used, "
        "as well as the used and total memory in GB."
    )

    def _run(self) -> str:
        mem_usage = MemoryUsage()
        return mem_usage.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")


class ProcessListTool(BaseTool):
    name: str = "process_list"
    description: str = (
        "Returns a list of currently running processes along with their process IDs (PIDs) and names."
    )

    def _run(self) -> str:
        process_list = ProcessList()
        return process_list.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")


class ErrorLogInput(BaseModel):
    log_type: str = Field(
        default="System",
        description="The type of log to query (e.g., 'System' or 'Application').",
    )
    count: int = Field(
        default=10, description="The number of error log entries to retrieve."
    )


class ErrorLogTool(BaseTool):
    name: str = "error_log"
    description: str = (
        "Collects and displays recent error logs from the specified Windows log (System or Application). "
        "Keep the default to 5."
    )
    args_schema: Type[BaseModel] = ErrorLogInput

    def _run(self, log_type: str = "System", count: int = 10) -> str:
        error_log = ErrorLog(log_type=log_type, count=count)
        return error_log.execute()

    async def _arun(self, log_type: str = "System", count: int = 10) -> str:
        raise NotImplementedError("Async execution not implemented.")


class BatteryStatusTool(BaseTool):
    name: str = "battery_status"
    description: str = (
        "Reports battery health and charge status for laptops or portable devices. "
        "Returns 'This device does not have a battery' if no battery is detected."
    )

    def _run(self) -> str:
        battery_status = BatteryStatus()
        return battery_status.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")


class PortScannerInput(BaseModel):
    target: str = Field(
        default="127.0.0.1",
        description="The IP address or hostname to scan for open ports.",
    )
    ports: List[int] = Field(
        default_factory=lambda: [22, 80, 443],
        description="List of port numbers to scan.",
    )


class PortScannerTool(BaseTool):
    name: str = "port_scanner"
    description: str = (
        "Scans the specified target for open ports among the provided list of port numbers. "
        "Default ports are 22 (SSH), 80 (HTTP), and 443 (HTTPS). "
        "Default IP address is 127.0.0.1."
    )
    args_schema: Type[BaseModel] = PortScannerInput

    def _run(self, target: str, ports: List[int]) -> str:
        scanner = PortScanner(target, ports)
        return scanner.execute()

    async def _arun(self, target: str, ports: List[int]) -> str:
        raise NotImplementedError("Async execution not implemented.")


class SystemInfoTool(BaseTool):
    name: str = "system_info"
    description: str = (
        "Retrieves detailed information about the computer’s hardware and software, "
        "including operating system details, CPU, memory, and disk usage."
    )

    def _run(self) -> str:
        sys_info = SystemInfo()
        return sys_info.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")


class NetworkSpeedTestTool(BaseTool):
    name: str = "network_speed_test"
    description: str = (
        "Measures the network speed including download, upload, and ping using the speedtest library."
    )

    def _run(self) -> str:
        speed_test = NetworkSpeedTest()
        return speed_test.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")


class EmptyTrashCanTool(BaseTool):
    name: str = "empty_trash_can"
    description: str = (
        "Empties the system's Recycle Bin (Trash Can) on Windows. "
        "Returns a message indicating whether the operation was successful."
    )

    def _run(self) -> str:
        empty_trash = EmptyTrashCan()
        return empty_trash.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")


class SecurityScanTool(BaseTool):
    name: str = "security_scan"
    description: str = (
        "Executes a security scan using Windows Defender (quick scan by default) on Windows systems. "
        "Returns the results of the scan."
    )

    def _run(self) -> str:
        scan = SecurityScan()
        return scan.execute()

    async def _arun(self) -> str:
        raise NotImplementedError("Async execution not implemented.")
