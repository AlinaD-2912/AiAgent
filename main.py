from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool, save_code_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


class CodeResponse(BaseModel):
    filename: str
    language: str
    code: str
    instructions: str


# Pick LLM
# llm = ChatOpenAI(model="gpt-4o-mini")
llm = ChatAnthropic(model="claude-3-5-haiku-20241022")

mode = input("Choose mode (research/coding): ").strip().lower()

if mode == "research":
    parser = PydanticOutputParser(pydantic_object=ResearchResponse)
    tools = [search_tool, wiki_tool, save_tool]
    system_prompt = """
    You are a research assistant.
    Answer the user query and use necessary tools. 
    Always output JSON ONLY in this format: {format_instructions}
    """
    query = input("What can I help you research? ")

elif mode == "coding":
    parser = PydanticOutputParser(pydantic_object=CodeResponse)
    tools = [save_code_tool]
    system_prompt = """
    You are a coding assistant.
    Generate code in the requested programming language.

    Always include:
    - filename (with correct extension, e.g., .py, .js, .php, .java, .html, etc.)
    - language (e.g., "python", "javascript", "php", "java", "html", "css")
    - code (the full source code)
    - instructions (like a README explaining dependencies, usage, etc.)

    Always output JSON ONLY in this format: {format_instructions}
    """
    query = input("What can I help you code? ")

else:
    print("Invalid mode. Please choose 'research' or 'coding'.")
    exit()


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e)
    print("Raw Response:", raw_response)
