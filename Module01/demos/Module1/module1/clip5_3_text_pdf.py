# Load text and PDF files from a directory as LangChain Documents

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader

text_loader = DirectoryLoader(
    "../data/my_files",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)

pdf_loader = DirectoryLoader(
    path = "../data/my_files",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader,
    loader_kwargs={"mode": "single"}
)

documents = text_loader.load() + pdf_loader.load()

print("Total documents loaded:", len(documents))

for doc in documents:
    print("\nSource:", doc.metadata.get("source"))
    print("Preview:", doc.page_content[:150])