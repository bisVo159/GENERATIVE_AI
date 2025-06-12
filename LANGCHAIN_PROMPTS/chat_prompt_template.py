from langchain.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('user', 'Explain in simple terms, what is {topic}')
])

prompt=chat_template.invoke({
    'domain':'cricket','topic':'dusra'
})

print(prompt)