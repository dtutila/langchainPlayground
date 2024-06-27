from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

print("program start...")
llm = OpenAI()

code_prompt = PromptTemplate(
    input_variables=["task", "language"],
    template="write a very short {language} function that will {task}"
)

code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt
)

result = code_chain({
    "language": args.language,
    "task": args.task
})
print(result["text"])
