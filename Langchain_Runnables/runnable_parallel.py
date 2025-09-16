
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

load_dotenv()

prompt1 = PromptTemplate(
    template="write a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about topic {topic}",
    input_variables=['topic']
)

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task= "text-generation"
)

parser = StrOutputParser()

model = ChatHuggingFace(llm=llm)


parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    "linkedin": RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result)