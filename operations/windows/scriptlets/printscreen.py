from operations.universal.abstracts import OSScriptlet


class PrintScreen(OSScriptlet):
    def __init__(self, store_to_clipboard):
        self.clipboard: bool = store_to_clipboard
    def execute(self) -> bool:
        pass
