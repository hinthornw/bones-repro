from typing import TypedDict

import structlog
from langchain_core.messages import AnyMessage
from langgraph.func import entrypoint

logger = structlog.stdlib.get_logger()


class Input(TypedDict):
    messages: list[AnyMessage]


@entrypoint()
async def agent(state: Input):
    logger.info(f"I'm in the 'agent': {state['messages'][-1]}", node="agent", other_val="bar")
    return {"messages": [{"role": "assistant", "content": "I'm in the 'agent'"}]}
