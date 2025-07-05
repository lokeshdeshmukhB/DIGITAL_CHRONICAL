"""
THE DIGITAL CHRONICLER
An AI Author of Our Times

"In an age of information abundance, the true art lies not in finding stories,
but in telling them in ways that stir the soul and illuminate the mind."
"""

import os
import re
import time
import json
import random
import requests
import datetime
import argparse
import threading
import queue
import logging
import hashlib
import csv
import nltk
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Tuple, Optional, Union, Set
from dataclasses import dataclass, field
from newspaper import Article, ArticleException
from concurrent.futures import ThreadPoolExecutor
from langchain_groq import ChatGroq  # Import Groq integration

# Try to download NLTK resources if not already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

from nltk.sentiment import SentimentIntensityAnalyzer

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("chronicler.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("DigitalChronicler")

# ======================================================================
# CONFIGURATION: THE WRITER'S TOOLS
# ======================================================================

@dataclass
class ChroniclerConfig:
    """The sacred configuration that guides our digital author's journey."""
    # API credentials - Using a list of tokens for rotation
    groq_api_tokens: List[str] = field(default_factory=lambda: [
        os.environ.get("GROQ_API_KEY", ""),
        # You can add backup tokens here if needed
    ])
    current_token_index: int = 0
    news_api_key: str = os.environ.get("NEWS_API_KEY", "")
    serper_api_key: str = os.environ.get("SERPER_API_KEY", "")
    
    # Groq model parameters
    primary_model: str = "llama-3.3-70b-versatile"
    backup_model: str = "mistral-saba-24b"
    
    # Content parameters
    topics_of_interest: List[str] = field(default_factory=lambda: ["technology", "science", "politics", "business"])
    writing_style: str = "literary"  # Options: literary, journalistic, academic
    article_length: str = "short"    # Options: short, medium, long
    include_quotes: bool = True
    include_analysis: bool = True
    
    # Technical parameters
    max_articles_to_fetch: int = 5
    max_articles_to_generate: int = 2
    request_timeout: int = 30
    max_retries: int = 3
    retry_delay: int = 2
    
    # Output parameters
    output_directory: str = "generated_chronicles"
    save_source_data: bool = True
    output_format: str = "markdown"  # Options: markdown, html, json, txt, csv
    
    # Direct input mode
    direct_input: bool = False
    input_title: str = ""
    input_content: str = ""
    input_topic: str = ""
    
    # Memory parameters
    memory_file: str = "chronicler_memory.json"
    memory_expiry_days: int = 7  # How long to remember stories to avoid duplication
    reset_memory: bool = False   # Whether to reset memory on startup
    
    # Model parameters
    use_local_model: bool = False  # Whether to use local model or API
    
    # Advanced features
    enable_sentiment_analysis: bool = True
    enable_topic_clustering: bool = True
    enable_summarization: bool = True
    enable_related_stories: bool = True
    enable_image_extraction: bool = False  # Requires additional dependencies
    
    # Performance parameters
    max_threads: int = 8
    cache_timeout: int = 3600  # 1 hour
    
    def get_current_groq_token(self) -> str:
        """Get the current Groq token and rotate if needed."""
        if not self.groq_api_tokens:
            return ""
        return self.groq_api_tokens[self.current_token_index]
    
    def rotate_groq_token(self) -> str:
        """Rotate to the next Groq token."""
        if len(self.groq_api_tokens) > 1:
            self.current_token_index = (self.current_token_index + 1) % len(self.groq_api_tokens)
            logger.info(f"Rotated to Groq token index {self.current_token_index}")
        return self.get_current_groq_token()

# ======================================================================
# SIMPLIFIED DIGITAL CHRONICLER CLASS
# ======================================================================

class DigitalChronicler:
    """
    The Digital Chronicler: An AI Author of Our Times
    Simplified version for GitHub deployment
    """
    
    def __init__(self, config_path: str = None):
        """Initialize the Digital Chronicler with configuration."""
        self.config = ChroniclerConfig()
        self.articles_generated = 0
        self.articles_researched = 0
        self.start_time = datetime.datetime.now()
        self.generated_articles = []
        self.researched_stories = []
        
        # Initialize AI model if API key is available
        self.model = None
        if self.config.get_current_groq_token():
            try:
                self.model = ChatGroq(
                    api_key=self.config.get_current_groq_token(),
                    model_name=self.config.primary_model
                )
                logger.info(f"Initialized AI model: {self.config.primary_model}")
            except Exception as e:
                logger.error(f"Error setting up AI model: {str(e)}")
        
        logger.info("Digital Chronicler initialized")
    
    def run_cycle(self) -> List[Dict[str, Any]]:
        """Run a complete cycle of news generation."""
        try:
            # For demo purposes, return sample articles
            sample_articles = [
                {
                    "generated_title": "AI Revolution in News Generation",
                    "generated_content": "The Digital Chronicler represents a new era in automated journalism, where artificial intelligence transforms raw news data into compelling narratives. This innovative platform demonstrates the potential of AI to enhance rather than replace human journalism.",
                    "topic": "technology",
                    "source_name": "Demo Source",
                    "url": "https://example.com",
                    "generation_timestamp": datetime.datetime.now().isoformat(),
                    "image_url": ""
                }
            ]
            
            self.articles_generated += len(sample_articles)
            return sample_articles
            
        except Exception as e:
            logger.error(f"Error in run_cycle: {str(e)}")
            return []
    
    def process_direct_input(self, title: str, topic: str, content: str) -> Dict[str, Any]:
        """Process direct user input into an article."""
        try:
            if not self.model:
                # Return a simple processed version if no AI model
                return {
                    "generated_title": f"Custom Article: {title}",
                    "generated_content": f"**{title}**\n\n{content}\n\nThis article was created using the Digital Chronicler platform.",
                    "topic": topic,
                    "source_name": "Direct Input",
                    "url": "",
                    "generation_timestamp": datetime.datetime.now().isoformat(),
                    "image_url": ""
                }
            
            # Use AI to enhance the content
            prompt = f"""Transform this user input into a well-structured article:

Title: {title}
Topic: {topic}
Content: {content}

Create an engaging article with proper formatting and structure."""
            
            response = self.model.invoke(prompt)
            
            return {
                "generated_title": title,
                "generated_content": response.content,
                "topic": topic,
                "source_name": "Direct Input",
                "url": "",
                "generation_timestamp": datetime.datetime.now().isoformat(),
                "image_url": ""
            }
            
        except Exception as e:
            logger.error(f"Error processing direct input: {str(e)}")
            return None
    
    def generate_similar_articles(self, article_name: str) -> List[Dict[str, Any]]:
        """Generate articles similar to the given topic."""
        try:
            # For demo purposes, return sample similar articles
            similar_articles = [
                {
                    "generated_title": f"Related Story: {article_name} Analysis",
                    "generated_content": f"This article explores topics related to '{article_name}' and provides additional context and analysis on the subject matter.",
                    "topic": "general",
                    "source_name": "Similar Articles Search",
                    "url": "https://example.com",
                    "generation_timestamp": datetime.datetime.now().isoformat(),
                    "image_url": "",
                    "search_query": article_name
                }
            ]
            
            return similar_articles
            
        except Exception as e:
            logger.error(f"Error generating similar articles: {str(e)}")
            return []
    
    def get_stats(self) -> Dict[str, Any]:
        """Get system statistics."""
        runtime_hours = (datetime.datetime.now() - self.start_time).total_seconds() / 3600
        
        return {
            "articles_generated": self.articles_generated,
            "articles_researched": self.articles_researched,
            "articles_per_hour": self.articles_generated / max(runtime_hours, 0.01),
            "run_time_hours": runtime_hours,
            "memory_stories": 0,
            "memory_urls": 0,
            "memory_titles": 0,
            "topic_trends": {"technology": 5, "science": 3, "politics": 2}
        }

# For backward compatibility
class ChroniclerMemory:
    """Simplified memory class."""
    def __init__(self, config):
        self.config = config
    
    def reset_memory(self):
        """Reset memory."""
        logger.info("Memory reset")