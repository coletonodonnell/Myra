import win32clipboard
import os
import platform
import datetime
from PIL import Image
from io import BytesIO
from operations.universal.abstracts import OSScriptlet
from mss import mss, tools


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


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

                if platform.system() == "Windows":
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

                        send_to_clipboard(win32clipboard.CF_DIB, data)

                return True
        except Exception as e:
            return False
