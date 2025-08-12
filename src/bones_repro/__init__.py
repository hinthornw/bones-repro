from typing import TypedDict

import structlog
from langchain_core.messages import AnyMessage
from langgraph.func import entrypoint

logger = structlog.stdlib.get_logger()


class Input(TypedDict):
    messages: list[AnyMessage]


@entrypoint()
async def agent(state: Input):
    logger.info("I'm in the 'agent'", node="agent", other_val="bar")
