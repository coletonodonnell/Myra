from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from operations.windows.osfunctions import PrintScreen, DiskSpace, WebSearch

class PrintScreenInput(BaseModel):
    clipboard: int = Field(description="Whether to place screenshot in clipboard as well. Set to one if true, zero if false", default=1)


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
    description: str = "Takes a users search and google's it for them using their default web browser."
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
