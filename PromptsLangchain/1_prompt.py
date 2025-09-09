# prompts are the input instructions or queries 
# given to a model to guide its output
# two types of prompts
# text based 
# multi model prompts
# here we work on text based propmpts
# llm outputs are prompt sensitive
# static and dynamic prompts


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt


load_dotenv()


model = ChatOpenAI()

st.header('Research Tool')

# user_input = st.text_input("Enter your prompt") static prompt

# dynamic prompting here asking user to enter these values 
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')


if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)
    

# when you have to write a new prompt as a
# user to generate a new response everytime
# those prompts are static prompts and gives too much flexiblity to 
# the user 
# for consistent user experience you should 
# define a template for your research tool

# for example
# this is an example of dynamic prompt

# please summarize the research paper titled
# "{paper input}" with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}
# 1. Mathematical Details: 
#   - include relevant mathematical equations if present in the paper
#   - Explain the mathematical concepts using simple,intutive code snippets
# 2. Analogies: 
#   - use relatable analogies to simplify complex ideas
# if certain information is not available in the paper, respond with: "insufficient
# information available" instead of guessing
# ensure summary is clear, accurate and aligned
# with provided style and length.   

# why use PromptTemplate over f strings

# 1 Default validation
# 2 reusable
# 3 langchain ecosystem

# console oriented chatbot flow
# you ---
# chatbot ---
# you ---
