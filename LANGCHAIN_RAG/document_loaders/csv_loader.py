from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(
    file_path='social_network_ads.csv'
)

docs = loader.load()
print(f"Number of documents loaded: {len(docs)}")
for i, doc in enumerate(docs):
    print(f"Document {i+1}:")
    print(f"Content: {doc.page_content[:100]}...")  
    print(f"Metadata: {doc.metadata}")
    print("-" * 40)