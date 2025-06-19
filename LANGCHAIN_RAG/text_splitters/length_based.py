from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('../document_loaders/dl-curriculum.pdf')

docs=loader.load()
splitter=CharacterTextSplitter(
    separator=' ',
    chunk_size=310,
    chunk_overlap=0,
)

print(len(docs))
# print(docs[0].page_content)
result = splitter.split_documents(docs)
print("*"*10)
print(len(result))
print(result[0].page_content)
print("*"*10)
print(result[1].page_content)