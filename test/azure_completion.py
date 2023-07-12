import openai
import sys

openai.api_type = "azure"
openai.api_base = sys.argv[1]
openai.api_version = sys.argv[2]
openai.api_key = sys.argv[3]
engine = sys.argv[4]
print(engine, openai.api_type, openai.api_key, openai.api_base, openai.api_version, openai.organization)
codex_query=open(sys.argv[5]).read()
response = openai.Completion.create(engine=engine, prompt=codex_query, stop="#")
print (response)
print (response['choices'][0]['text'])
