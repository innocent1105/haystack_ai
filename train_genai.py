from haystack.document_stores import FAISSDocumentStore
from haystack.dataclasses import Document

doc_store = FAISSDocumentStore(
    sql_url="sqlite:///my_docs.db", 
    faiss_index_factory_str="Flat"
)

documents = [
    Document(content="Haystack is a framework for building QA systems."),
    Document(content="It supports both extractive and generative QA.")
]
doc_store.write_documents(documents)



















