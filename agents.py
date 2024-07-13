from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.agents import  OpenAIFunctionsAgent, AgentExecutor
from langchain.schema import SystemMessage
from tools.sql import list_tables, run_query_tool, describe_table_tool
from langchain.memory import ConversationBufferMemory
from tools.report import write_report_tool


load_dotenv()

chat = ChatOpenAI()
tables = list_tables()
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(
            "You are an analyst with access to a SQLite database."
            f"The database has tables of: \n {tables}"
            "Do not make any assumptions about the database tables and columns,"
            "instead use the 'describe_table' function"
        )),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

tools = [
    run_query_tool,
    describe_table_tool,
    write_report_tool
]
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
    memory=memory
)

agent_executor("how many orders are there? write the results in a html file")
agent_executor("do the exact same for the users")
