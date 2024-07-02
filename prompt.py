from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()

print("program start...")

embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

retriever = db.as_retriever()

chat = ChatOpenAI()

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

result = chain.run("What is an interesting fact about english language?")

print(result)
