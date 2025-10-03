from haystack import Pipeline
from haystack.components.generators import HuggingFaceLocalGenerator
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.builders import PromptBuilder
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.dataclasses import Document
import warnings
from transformers import logging as hf_logging
import logging


warnings.filterwarnings("ignore")
hf_logging.set_verbosity_error()
logging.getLogger("haystack").setLevel(logging.ERROR)


doc_store = InMemoryDocumentStore()
retriever = InMemoryBM25Retriever(document_store=doc_store)

doc_store.write_documents([
    Document(content="Haystack is a framework for building search and question answering systems."),
    Document(content="It supports both extractive and generative QA."),
    Document(content="Your name is TaxScope AI."),
    Document(content="You are a multi-modal AI system."),
])

prompt_template = """
Answer the question based on the following documents if the question is connected.:
{% for doc in documents %}
- {{ doc.content }}
{% endfor %}

Answer the user's question ONLY using the information provided in the following 'CONTEXT' section. 
If the answer is not found in the context, state clearly, 'I don't have enough information in my 
documents to answer that question.' Do not use any external knowledge

Question: {{ query }}
Answer:
"""



prompt_builder = PromptBuilder(template=prompt_template)

generator = HuggingFaceLocalGenerator(
    # model="google/flan-t5-small", 
    model="google/flan-t5-base", 
    task="text2text-generation",
    huggingface_pipeline_kwargs={"framework": "pt"} 
)

pipe = Pipeline()
pipe.add_component("retriever", retriever)
pipe.add_component("prompt_builder", prompt_builder)
pipe.add_component("generator", generator)

pipe.connect("retriever.documents", "prompt_builder.documents")
pipe.connect("prompt_builder", "generator")

result = pipe.run(
    {
        "retriever": {"query": " what is music?"},
        "prompt_builder": {"query": " what is music?"},
        "generator": {"generation_kwargs": {"max_new_tokens": 50, "temperature": 0.7}}
    }
)

print(result["generator"]["replies"][0])
