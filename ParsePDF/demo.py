import openai
import os
import nest_asyncio
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex
from IPython.display import Markdown, display
# bring in deps
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


# Set API keys directly in the script
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-EnPWMfNOWREeRsaCECeWO7zGmVneB0owCJqU7xCk1NDnv4Ud"

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# Allow nested asyncio loops
nest_asyncio.apply()

parser = LlamaParse(
    api_key=llamaparse_api_key,
    result_type="markdown"  # "markdown" and "text" are available
)

# use SimpleDirectoryReader to parse our file
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(input_files=['data/test.pdf'], file_extractor=file_extractor).load_data()

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
