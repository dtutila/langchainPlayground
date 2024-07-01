from dotenv import load_dotenv
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory


load_dotenv()

prompt = ChatPromptTemplate(
    input_variable=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chat = ChatOpenAI()

memory = ConversationBufferMemory(
    memory_key="messages",
    return_messages=True,
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
)


print("Start chatting...\n")
while True:
    content = input(">>> ")
    result = chain({"content": content})
    print(result["text"])





