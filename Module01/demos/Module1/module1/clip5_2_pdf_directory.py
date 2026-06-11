# Load all PDFs from a directory as single-document LangChain Documents

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = "../data/my_files",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader,
    loader_kwargs={"mode": "single"}
)

documents = loader.load()
print("Loaded:", len(documents))

for doc in documents:
    print("\nFile:", doc.metadata.get("source"))
    print("Preview:", doc.page_content[:150])