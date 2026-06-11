# Lazily load PDFs from a directory

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="../data/my_files",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

# Lazy loading
for doc in loader.lazy_load():
    print("\nFile:", doc.metadata.get("source"))
    print("Preview:", doc.page_content[:100])
    print("-" * 50)

    # In a real pipeline, we could split the document into smaller chunks,
    # generate embeddings for each chunk, store them in a vector database