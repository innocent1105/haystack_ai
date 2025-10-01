from haystack import Document, Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.readers import ExtractiveReader

doc_store = InMemoryDocumentStore()
documents = [
    Document(content="The Eiffel Tower is in Paris."),
    Document(content="The Colosseum is in Rome."),
]
doc_store.write_documents(documents)

retriever = InMemoryBM25Retriever(document_store=doc_store)
reader = ExtractiveReader(model="deepset/roberta-base-squad2")

pipeline = Pipeline()
pipeline.add_component("retriever", retriever)
pipeline.add_component("reader", reader)
pipeline.connect("retriever", "reader")

result = pipeline.run({
    "retriever": {"query": "Where is the Eiffel Tower?"},
    "reader": {"query": "Where is the Eiffel Tower?"}
})

print(result["reader"]["answers"][0].data)  
