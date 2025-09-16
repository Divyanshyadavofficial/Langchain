
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

load_dotenv()

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables = ['topic']
)
prompt2 = PromptTemplate(
    template = "Explain the following joke -{text}",
    input_variables=['text']
)
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task= "text-generation"
)
parser = StrOutputParser()

model = ChatHuggingFace(llm=llm)

chain  = RunnableSequence(prompt,model,parser)
