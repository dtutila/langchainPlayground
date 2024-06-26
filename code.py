from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
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
test_prompt = PromptTemplate(
    input_variables=["code", "language"],
    template="write a test for the following {language} code: {code}"
)
code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code"
)

test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key="test"
)

chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["task", "language"],
    output_variables=["code", "test"]

)
result = chain({
    "language": args.language,
    "task": args.task
})
print(result["code"])
print(result["test"])
