from langchain import LLMChain
from langchain.llms import Ollama

def get_onboarding_recommendation(user_input):
    llm = Ollama(api_key='your-api-key')
    chain = LLMChain(llm=llm)
    response = chain.run(f"Help onboard a new user with the following input: {user_input}")
    return response
