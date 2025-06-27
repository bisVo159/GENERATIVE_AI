from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
# from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_experimental.text_splitter import SemanticChunker
from langchain.retrievers.document_compressors.chain_extract import LLMChainExtractor
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever


def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

# Step 1a - Indexing (Document Ingestion)
video_id="MdeQMVBuGgY"
try:
    # If you don’t care which language, this returns the “best” one
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=["en"])

    # print(transcript_list)
    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    # print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")

# Step 1b - Indexing (Text Splitting)
# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splitter = splitter=SemanticChunker(
    GoogleGenerativeAIEmbeddings(model='models/embedding-001'),
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=2
)
chunks = splitter.create_documents([transcript])
print(len(chunks))
print(type(chunks[50]))

# Step 1c & 1d - Indexing (Embedding Generation and Storing in Vector Store)
embedding_model=GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vector_store = FAISS.from_documents(chunks, embedding_model)
# vector_store = Chroma.from_documents(
#                                     documents=chunks, 
#                                     embedding=embedding_model,
#                                     collection_name="youtube_transcript",
#                                     persist_directory="chroma_db"
#                                     )
# print(vectorstore.index_to_docstore_id)
# print(vector_store.get_by_ids(['ea7ece3d-5875-4fa7-9335-3f9c67152e67']))

# Step 2 - Retrieval
base_retriever = vector_store.as_retriever( search_kwargs={"k": 4})
# print(retriever)
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
compressor = LLMChainExtractor.from_llm(llm)
retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# Step 3 - Augmentation
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

question= "what is the topic of the video?"
# retrieved_docs    = retriever.invoke(question)
# context_text =format_docs(retrieved_docs)

# final_prompt = prompt.invoke({"context": context_text, "question": question})

# Step 4 - Generation
# answer = llm.invoke(final_prompt)
# print(answer.content)

# Building a Chain
parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})
parser = StrOutputParser()
main_chain = parallel_chain | prompt | llm | parser
result=main_chain.invoke('Can you summarize the video')
print(result)
