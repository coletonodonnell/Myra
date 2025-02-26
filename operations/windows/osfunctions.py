from operations.universal.abstracts import OSScriptlet

import os
import datetime

import win32clipboard
from PIL import Image
from io import BytesIO
from mss import mss, tools

from webbrowser import open_new_tab
from urllib.parse import quote

from shutil import disk_usage


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

                downloads_folder = os.path.join(
                    os.environ["USERPROFILE"], "Downloads"
                )

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
