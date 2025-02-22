from command.config import *
from audio.AUDIO import *
from response.RESPONSE import RESPONSE_SYSTEM

from interpretation.assistant.Myra_Graph import myraGraph
from langchain_core.runnables import RunnableConfig

config = RunnableConfig(configurable={"thread_id": "1"})

def Core_Process(query):
    Process_Query(query)
    ## TODO: Implement better tool integration so stalls and errors can be handled as well
    pass

def Process_Query(user_input: str):
    for event in myraGraph.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config
        ):
        for value in event.values():
            RESPONSE_SYSTEM.Custom_Response(value["messages"][-1].content)
            