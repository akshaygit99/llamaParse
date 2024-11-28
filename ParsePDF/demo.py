import os
import nest_asyncio
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex

# Set API keys directly in the script
os.environ["LLAMA_CLOUD_API_KEY"] = "<your_llama_cloud_api_key>"
os.environ["OPENAI_API_KEY"] = "<your_openai_api_key>"

# Allow nested asyncio loops
nest_asyncio.apply()

# Load and process the document
document = LlamaParse(result_type="markdown").load_data("./data/MLFwk.pdf")

# Create the index and query engine
llama_parse_index = VectorStoreIndex.from_documents(document)
llama_parse_query_engine = llama_parse_index.as_query_engine()

# Execute queries
print(
    llama_parse_query_engine.query(
        "What is the Bill To Address?"
    )
)

print(
    llama_parse_query_engine.query(
        "What are the API usage credits?"
    )
)
