from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def ticket_analysis_2(query):
    response = client.responses.create(
        model="gpt-6-luna",
        instructions="""
        You are a customer support helper and assistant
        you need to analyse the ticket given and provide the following:

        1) a small summary of the problem (start with "Summary:")
        2) the customers sentiment (start with "Sentiment:")
        3) provide a recomendation to the support team on what to do (start with "reccomendation:")

        dont make anything up, and do not assume (for example the refund process), use only the details of the ticket provided

        if the question is off topic, meaning it does not relate to customer service, then just skip part 1 and part 2 and say that it is a irrelevant query and show it
        """,
        input=query
    )
    return response.output_text

query = """I want to know when the sun sets on september 21st"""

answer = ticket_analysis_2(query)
print(answer)