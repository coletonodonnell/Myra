import pyclip
import datetime
import os
import platform
from operations.universal.abstracts import OSScriptlet
from mss import mss, tools


class PrintScreen(OSScriptlet):
    def __init__(self, store_to_clipboard):
        self.clipboard: bool = store_to_clipboard
    def execute(self) -> bool:
        try:    
            with mss() as sct:
                monitor = sct.monitors[1]
                now = datetime.datetime.now()

                img = sct.grab(monitor)
                png = tools.to_png(img.rgb, img.size)
                if self.clipboard:
                    pyclip.copy(png)

                if platform.system() == "Windows":
                    downloads_folder = os.path.join(os.environ["USERPROFILE"], "Downloads")
                else:
                    downloads_folder = os.path.join(os.environ["HOME"], "Downloads")

                filename = now.strftime("Screenshot-%Y-%m-%d_%H-%M-%S.png")
                filepath = os.path.join(downloads_folder, filename)

                with open(filepath, "wb") as file:
                    file.write(png)

                return True
        except Exception as e:
            return False
