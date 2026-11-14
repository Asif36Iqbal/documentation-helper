import asyncio
import os
import ssl
from typing import Any, Dict, List

import certifi
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_tavily import TavilyCrawl, TavilyExtract, TavilyMap

from logger import (Colors, log_error, log_header, log_info, log_success,
                    log_warning)

load_dotenv()

# Configuring SSL context to use certifi certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())
os.environ["SSL_CERT_FILE"]=certifi.where()
os.environ["REQUESTS_CA_BUNDLE"]=certifi.where()

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

chroma = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
tavily_extract = TavilyExtract()
tavily_map = TavilyMap(max_depth = 5, max_breadth = 20, max_pages = 1000)
tavilty_crawl = TavilyCrawl()


async def main():
    """Main async function to orchestrate the entire process"""
    log_header("DOCUMENTATION INGESTION PIPELINE")

    log_info("🗺️  TavilyCrawl: Starting to crawl the documentation site", Colors.PURPLE)

if __name__ == "__main__":
    asyncio.run(main())