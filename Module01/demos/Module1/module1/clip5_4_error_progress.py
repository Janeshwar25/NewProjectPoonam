# Load many PDFs with error skipping and progress tracking

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="../data/many_files",      
    glob="**/*.pdf",             
    loader_cls=PyPDFLoader,
    loader_kwargs={"mode": "single"},      
    silent_errors=True,         # Skip corrupted files instead of crashing
    show_progress=True          # Display progress bar during loading
)

documents = loader.load()

print("\nTotal Document objects loaded (pages):", len(documents))

for doc in documents:
    print("\nFile:", doc.metadata.get("source"))
    print("Preview:", doc.page_content[:150])
    print("-" * 50)