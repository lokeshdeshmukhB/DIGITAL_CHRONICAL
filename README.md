# 📰 Digital Chronicler - AI-Powered News Generation Platform

> *"In an age of information abundance, the true art lies not in finding stories, but in telling them in ways that stir the soul and illuminate the mind."*

## 🌟 Overview

Digital Chronicler is an advanced AI-powered news generation platform that researches trending stories from multiple sources and transforms them into compelling, original narratives. Using state-of-the-art natural language processing and machine learning, it creates engaging articles in various writing styles while maintaining journalistic integrity.

## ✨ Features

### 🔍 **Multi-Source News Gathering**
- **News API Integration**: Real-time access to global news sources
- **Google News RSS**: Trending stories from Google News
- **Reddit News**: Community-driven news discovery
- **Hacker News**: Tech-focused story aggregation
- **Serper API**: Enhanced search capabilities

### 🤖 **AI-Powered Content Generation**
- **Groq LLM Integration**: Advanced language model for content creation
- **Multiple Writing Styles**: Literary, journalistic, and academic formats
- **Customizable Article Length**: Short, medium, and long-form content
- **Sentiment Analysis**: Emotional tone detection and analysis
- **Entity Extraction**: Automatic identification of people, organizations, and locations

### 🎨 **Interactive Web Interface**
- **Streamlit-based UI**: Beautiful, responsive web interface
- **Real-time Generation**: Live article creation with progress tracking
- **Multiple Export Formats**: HTML, Markdown, JSON, and plain text
- **Topic Filtering**: Focus on specific news categories
- **Similar Article Discovery**: Find related content automatically

### 🧠 **Smart Memory System**
- **Duplicate Prevention**: Avoids regenerating similar content
- **Topic Trending**: Tracks popular subjects over time
- **Sentiment History**: Monitors emotional trends in news
- **URL Tracking**: Prevents processing the same sources repeatedly

### 📊 **Analytics & Insights**
- **Generation Statistics**: Track articles created and processed
- **Topic Distribution**: Visual representation of content categories
- **Performance Metrics**: Monitor system efficiency and output quality
- **Memory Analytics**: Understand content patterns and trends

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key (for AI content generation)
- News API key (optional, for enhanced news gathering)
- Serper API key (optional, for Google search integration)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/DIGITAL_CHRONICAL.git
   cd DIGITAL_CHRONICAL
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional but recommended)
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   export NEWS_API_KEY="your_news_api_key_here"
   export SERPER_API_KEY="your_serper_api_key_here"
   ```

4. **Run the application**
   ```bash
   streamlit run Streamlit_main.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 🎯 Usage

### Basic News Generation
1. **Configure Topics**: Select your preferred news categories (Technology, Science, Politics, etc.)
2. **Set Parameters**: Choose writing style, article length, and output format
3. **Generate Content**: Click "Generate News Articles" to create original content
4. **Download Results**: Export articles in your preferred format

### Custom Article Creation
1. **Navigate to "Direct Input" tab**
2. **Enter Details**: Provide title, topic, and content notes
3. **Generate**: Let AI transform your input into a polished article
4. **Export**: Download the generated content

### Finding Similar Articles
1. **Use "Similar Articles" tab**
2. **Enter Topic**: Specify the subject you're interested in
3. **Discover**: Find and generate articles on related topics
4. **Compare**: Analyze different perspectives on the same subject

## 🛠️ Configuration

### Core Settings
```python
# In Digital_chronical_backend.py
@dataclass
class ChroniclerConfig:
    # API Configuration
    groq_api_tokens: List[str] = ["your_groq_key"]
    news_api_key: str = "your_news_api_key"
    serper_api_key: str = "your_serper_key"
    
    # Content Parameters
    topics_of_interest: List[str] = ["technology", "science", "politics"]
    writing_style: str = "literary"  # literary, journalistic, academic
    article_length: str = "short"    # short, medium, long
    
    # Output Settings
    output_format: str = "html"      # html, markdown, json, txt
    max_articles_to_generate: int = 2
    max_articles_to_fetch: int = 5
```

### Available Topics
- 📱 Technology
- 🔬 Science  
- 🏛️ Politics
- 💼 Business
- 🏥 Health
- 🎭 Entertainment
- 🏆 Sports
- 🪖 War
- 📚 Education
- 🌳 Environment

### Writing Styles
- **Literary**: Rich metaphors and vivid descriptions
- **Journalistic**: Clear, concise, fact-focused reporting
- **Academic**: Formal language with analytical depth

## 📁 Project Structure

```
DIGITAL_CHRONICAL/
├── Streamlit_main.py              # Main web interface
├── Digital_chronical_backend.py   # Core AI and processing logic
├── generated_chronicles/          # Output directory for articles
│   ├── *.html                    # Generated articles
│   ├── *.json                    # Source data files
│   └── chronicler_memory.json    # Memory system data
├── __pycache__/                  # Python cache files
├── chronicler.log                # Application logs
└── README.md                     # This file
```

## 🔧 API Keys Setup

### Groq API (Required)
1. Visit [Groq Console](https://console.groq.com/)
2. Create an account and generate an API key
3. Add to environment variables or update the config

### News API (Optional)
1. Visit [NewsAPI.org](https://newsapi.org/)
2. Register for a free account
3. Get your API key and add to configuration

### Serper API (Optional)
1. Visit [Serper.dev](https://serper.dev/)
2. Sign up for an account
3. Generate API key for enhanced search capabilities

## 🎨 Features in Detail

### Memory System
The Digital Chronicler includes an intelligent memory system that:
- **Prevents Duplicates**: Tracks processed URLs and content hashes
- **Maintains Context**: Remembers generated titles and topics
- **Tracks Trends**: Monitors topic frequency and sentiment over time
- **Expires Old Data**: Automatically cleans up outdated information

### Content Generation Pipeline
1. **News Gathering**: Collect stories from multiple sources
2. **Content Extraction**: Extract full article text and metadata
3. **Research Enhancement**: Add related stories and entity extraction
4. **AI Generation**: Transform raw content into engaging narratives
5. **Quality Assurance**: Ensure uniqueness and relevance
6. **Publishing**: Format and save in multiple output formats

### Export Formats
- **HTML**: Web-ready format with styling and metadata
- **Markdown**: Clean, readable format for documentation
- **JSON**: Structured data with full metadata
- **Plain Text**: Simple, universal format

## 📊 Statistics & Analytics

The platform provides comprehensive analytics including:
- **Generation Metrics**: Articles created per hour
- **Topic Trends**: Most popular subjects over time
- **Memory Statistics**: Processed URLs and content tracking
- **Performance Data**: System efficiency and processing times

## 🔒 Privacy & Ethics

Digital Chronicler is designed with responsible AI principles:
- **Source Attribution**: Always credits original news sources
- **Content Transformation**: Creates original narratives, not copies
- **Respectful Crawling**: Uses appropriate delays and user agents
- **Transparency**: Clear indication of AI-generated content

## 🐛 Troubleshooting

### Common Issues

**"No articles generated"**
- Check your API keys are valid
- Ensure internet connectivity
- Verify selected topics have recent news

**"Groq API Error"**
- Confirm API key is correct
- Check rate limits haven't been exceeded
- Try rotating to backup API keys

**"Memory file errors"**
- Delete `chronicler_memory.json` to reset
- Check file permissions in output directory
- Ensure sufficient disk space

### Logs
Check `chronicler.log` for detailed error information and debugging.

## 🤝 Contributing

We welcome contributions! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Format code
black *.py

# Type checking
mypy *.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq**: For providing advanced language model capabilities
- **Streamlit**: For the excellent web framework
- **NewsAPI**: For comprehensive news data access
- **Newspaper3k**: For article extraction capabilities
- **NLTK**: For natural language processing tools

## 📞 Support

For support, questions, or feature requests:
- 📧 Email: [your-email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/DIGITAL_CHRONICAL/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/DIGITAL_CHRONICAL/discussions)

## 🔮 Roadmap

### Upcoming Features
- [ ] **Multi-language Support**: Generate content in multiple languages
- [ ] **Image Generation**: AI-created images for articles
- [ ] **Audio Narration**: Text-to-speech for generated articles
- [ ] **Social Media Integration**: Direct publishing to social platforms
- [ ] **Advanced Analytics**: Deeper insights into content performance
- [ ] **Custom Models**: Support for local and custom AI models
- [ ] **Collaborative Features**: Multi-user content creation
- [ ] **API Endpoints**: RESTful API for programmatic access

---

**Digital Chronicler** - *Transforming information into inspiration, one story at a time.*

