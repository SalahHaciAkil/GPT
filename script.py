# Import the OpenAI library
import openai


# Set the API key

key ="key"

openai.api_key = key

# ask the user what he want to search on the internet
search = input("What do you want to search on the internet? ")
# go and get the first result from google 
firstResult = googleSearch(search)
