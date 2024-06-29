from dotenv import load_dotenv
from langchain.prompts import HumanMessagePromptTemplate,ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


load_dotenv()

prompt = ChatPromptTemplate(
    input_variable=["content"],
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chat = ChatOpenAI()
chain = LLMChain(
    llm=chat,
    prompt=prompt,
)


print("Start chatting...\n")
while True:
    content = input(">>> ")
    result = chain({"content": content})
    print(result["text"])





