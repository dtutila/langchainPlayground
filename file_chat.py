from dotenv import load_dotenv
from langchain.document_loaders import  TextLoader
from langchain.text_splitter import  CharacterTextSplitter

load_dotenv()

print("program start...")

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("context/facts.txt")
doc = loader.load_and_split(
    text_splitter=text_splitter
)

