from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from operations.windows.osfunctions import PrintScreen

class PrintScreenInput(BaseModel):
    store_to_clipboard: bool = Field(
        default=True,
        description="Whether to place screenshot in clipboard as well",
    )

class PrintScreenTool(BaseTool):
    name: str = "print_screen_tool"
    description: str = (
        "Takes a screenshot of the primary monitor, saves to Downloads, "
        "and optionally copies it to clipboard."
    )
    args_schema: Type[BaseModel] = PrintScreenInput

    def _run(self, store_to_clipboard: bool = True) -> str:
        ps = PrintScreen(store_to_clipboard)
        success = ps.execute()
        if success:
            return (
                f"Screenshot taken and saved. Clipboard option = {store_to_clipboard}"
            )
        else:
            return "An error occurred during screenshot capture."

    async def _arun(self, store_to_clipboard: bool = True) -> str:
        raise NotImplementedError("Async execution not implemented.")