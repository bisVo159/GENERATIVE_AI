from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader= DirectoryLoader(
    'Books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
# print(f"Number of documents loaded: {len(docs)}")
for i, doc in enumerate(docs):
    print(f"Document {i+1}:")
    print(f"Content: {doc.page_content[:100]}...")  # Print first 100 characters
    print(f"Metadata: {doc.metadata}")
    print("-" * 40)