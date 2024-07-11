from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.agents import  OpenAIFunctionsAgent, AgentExecutor
from langchain.schema import SystemMessage
from tools.sql import list_tables, run_query_tool, describe_table_tool


load_dotenv()

chat = ChatOpenAI()
tables = list_tables()
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=f"You are an analyst with access to a SQLite database.\n List of database tables: \n {tables}"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)
tools = [run_query_tool, describe_table_tool]
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools
)

agent_executor("How many users who have provided a shipping address live in the west coast?")
