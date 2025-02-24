from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from langchain_core.prompts import PromptTemplate

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from operations.windows.tools import PrintScreenTool


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

template = """<|system|>
You are a personal assistant named Myra. Answer any questions I have and help me with simple requests.<|end|>
<|user|>
{question}<|end|>
<|assistant|>"""

prompt = PromptTemplate.from_template(template)

# Huggingface LLM Interface
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
)
chat_model = ChatHuggingFace(llm=llm)

tools = [PrintScreenTool()]

chat_model_with_tools = chat_model.bind_tools(tools)

chain = prompt | chat_model_with_tools

def assistant(state: State):
    return {"messages": [chain.invoke(state["messages"])]}

graph_builder.add_node("assistant", assistant)

tool_node = ToolNode(tools = tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "assistant")
graph_builder.add_conditional_edges(
    "assistant",
    tools_condition,
    {"tools": "tools", END: END}
)
graph_builder.add_edge("tools", "assistant")


memory = MemorySaver()

myraGraph = graph_builder.compile(checkpointer=memory)