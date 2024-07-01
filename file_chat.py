from dotenv import load_dotenv
from langchain.document_loaders import  TextLoader
from langchain.text_splitter import  CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

print("program start...")
embeddings = OpenAIEmbeddings()
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("context/facts.txt")
doc = loader.load_and_split(
    text_splitter=text_splitter
)

