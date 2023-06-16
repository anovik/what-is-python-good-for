import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  max_tokens=256,
  prompt="What is Python good for?"
)

#print(response)
print(response['choices'][0]['text'])

response = openai.Completion.create(
  model="text-davinci-003",
  max_tokens=256,
  prompt="What is Python bad for?"
)

#print(response)
print(response['choices'][0]['text'])

response = openai.Completion.create(
  model="text-davinci-003",
  max_tokens=256,
  prompt="Create Python code for web scraping of wiki page"
)

#print(response)
print(response['choices'][0]['text'])

input("Press Enter to continue...")

