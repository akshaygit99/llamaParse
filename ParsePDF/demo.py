from dotenv import load_dotenv
load_dotenv()

import nest_asyncio
nest_asyncio.apply()


from llama_parse import LlamaParse
document=LlamaParse(result_type="markdown").load_data("./data/MLFwk.pdf")

from llama_index.core import VectorStoreIndex
llama_parse_inex=VectorStoreIndex.from_documents(document)

llama_parse_query_engine=llama_parse_inex.as_query_engine()

print(llama_parse_query_engine.query
      (
          "What is the Bill To Address?"
        
      ))

print(llama_parse_query_engine.query
      (
          "What are the API usage credits?'"
        
      ))
