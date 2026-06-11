# Load all text files from a directory as LangChain Documents

from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path ="../data/my_files",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)

documents = loader.load()

print("Total Documents Loaded:", len(documents))

for doc in documents:
    print("\nFile:", doc.metadata.get("source"))
    print("Preview:", doc.page_content[:150])
    print(50 * "-")

