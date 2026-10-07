from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def ticket_analysis(query):
    response = client.responses.create(
        model="gpt-6-luna",
        instructions="""
        You are a customer supper helper and assistant
        you need to analyse the ticket given and provide the following:

        1) a small summary of the problem
        2) the customers sentiment
        3) provide a recomendation to the support team on what to do

        dont make anything up, use only the details of the ticket provided
        """,
        input=query
    )
    return response.output_text

query = """"""

answer = ticket_analysis(query)
print(answer)