from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from operations.windows.osfunctions import PrintScreen

class PrintScreenInput(BaseModel):
    clipboard: int = Field(description="Whether to place screenshot in clipboard as well. Set to one if true, zero if false", default=1)

class PrintScreenTool(BaseTool):
    name: str = "print_screen_tool"
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
