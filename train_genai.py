import os
from pathlib import Path

from haystack import Pipeline
from haystack.components.converters import TextFileToDocument
from haystack.components.writers import DocumentWriter

from haystack_integrations.document_stores.chroma import ChromaDocumentStore
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

file_paths = [str(Path("data") / name) for name in os.listdir("data")]

embedding_fn = SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/all-MiniLM-L6-v2")


document_store = ChromaDocumentStore()

indexing = Pipeline()
indexing.add_component("converter", TextFileToDocument())
indexing.add_component("writer", DocumentWriter(document_store))
indexing.connect("converter", "writer")
indexing.run({"converter": {"sources": file_paths}})
