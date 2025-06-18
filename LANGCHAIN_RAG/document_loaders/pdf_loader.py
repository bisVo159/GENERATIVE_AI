from langchain_community.document_loaders import PyPDFLoader

# only suitable for texual pdfs
# some pdf loader with usecase and examples
# PyPDFLoader is used to load PDF files into LangChain document objects
# PyMuPDFLoader is used to load PDF files into LangChain document objects with additional metadata
# PyPDFium2Loader is used to load PDF files into LangChain document objects with additional metadata and support for images

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)
# print(docs)