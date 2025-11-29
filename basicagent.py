from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv, find_dotenv
import logging
import os

load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

gemini_llm = Gemini(id="gemini-2.5-flash", temperature=0.5)

reporting_agent = Agent(
    name="reporting agent",
    instructions="Write a report on the topic. Output only the well formatted report.",
    model=gemini_llm,  
    markdown=True,
    debug_mode=True,
)

reporting_agent.print_response(input="Latest trends in AI in last 1 week", stream=False)