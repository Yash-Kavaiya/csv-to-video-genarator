# !pip install --upgrade --user langchain-core langchain-google-vertexai --quiet
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import ChatVertexAI
df=pd.read_csv("https://storage.googleapis.com/quiz11111111111111111111/quiz.csv")
df=df.drop(columns=["Unnamed: 0"],axis=1)

def translation_df(row_name):
    system1= """ If question is in Gujarati Then translate english find answer and translate in gujarati again and give me answer in gujarati You are a helpful assistant Answer Convert sentence to gujarati to english   
a Question You will recive a Question on ['Question','A) Option A','B) Option B','C) Option C','D) Option D']
format and You need to Answer in ['Question','A) Option A','B) Option B','C) Option C','D) Option D','Answer: A,B,C,D (Only one)', 
'Explantion about right Answer'] Format Make sure Answer Should be 100 % Correct"""
    human1 =df.iloc[row_name].to_list()
    #human1 = """['વિદ્યુતપાવર નો SI એકમ ક્યો છે ?', 'વોટ', 'વોલ્ટ', 'એમ્પિયર', 'કુલંબ']"""
    prompt = ChatPromptTemplate.from_messages([("system", system1), ("human", human1)])

    chat = ChatVertexAI(model_name="gemini-pro")

    chain = prompt | chat
    res =chain.invoke({})
    print(res.content)
    return res.content
import time

# Assuming df_t is initialized somewhere above
df_t = []
for i in range(1, 95527):
    start_time = time.time()  # Capture start time
    # Your operation here
    time.sleep(5)  # Simulating a delay, replace this with your actual operation
    result = translation_df(i)  # Assuming this is your function call
    df_t.append(result)
    end_time = time.time()  # Capture end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Iteration {i}: Time taken = {elapsed_time} seconds")
df2 = pd.DataFrame(df_t)

df2.to_csv("final.csv")