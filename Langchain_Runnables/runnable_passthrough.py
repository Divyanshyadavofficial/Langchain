
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

load_dotenv()

prompt1 = PromptTemplate(
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
joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))