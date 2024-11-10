# AI-JARVIS

API-based web scraping and AI analysis system (PythonAnywhere compatible version of AI Web Scraper)

## Major Changes (API Version vs Local Selenium Version)

### API Version (Current)
- Stable server-side scraping using ScrapingBee API
- No browser/driver installation required
- Full PythonAnywhere compatibility
- Cloud environment support
- API call costs apply

### Selenium Version ([Original Project](https://github.com/shop2world/AI-Web-Scraper))
- Requires local Chrome WebDriver
- Uses system resources
- Limited on PythonAnywhere free accounts
- Free to use
- System dependencies required

## Project Structure
```
AI-JARVIS/
├── ai_web_scraper/        # Main project directory
├── scraper/              # Main app directory
├── requirements.txt      # Project dependencies
├── .env.example         # Example environment variables
├── README.md            # Project documentation
└── deployment.md        # Deployment guide
```

## Features
- Web scraping via ScrapingBee API
- Content analysis with OpenAI GPT
- Cloud environment support
- Simple user interface

## Prerequisites
- Python 3.8+
- ScrapingBee API key
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shop2world/Ai-JARVIS.git
cd Ai-JARVIS
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Copy .env.example to .env
cp .env.example .env

# Add your API keys to .env file
OPENAI_API_KEY=your_openai_api_key
SCRAPINGBEE_API_KEY=your_scrapingbee_api_key
```

## API Usage and Costs
- ScrapingBee: 
  - Free trial: 1,000 credits
  - Basic plan: $49/month (10,000 credits)
- OpenAI:
  - GPT-3.5-turbo: $0.002/1K tokens

## Performance Comparison
| Feature | API Version | Selenium Version |
|---------|-------------|------------------|
| Speed | Faster | Slower |
| Cost | Paid | Free |
| Reliability | High | Medium |
| Cloud Support | Yes | Limited |

## Security
- Maintain API key security
- Proper environment variable management
- HTTPS recommended
- Never commit .env file
- Set DEBUG=False in production

## License
MIT License

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## Support
For any inquiries or support:
- Contact: Frank Kim
- Email: info@shop2world.com
- Twitter: [@salecoupon](https://x.com/salecoupon)
- Issue Tracker: Use the GitHub issue tracker for technical questions

## Acknowledgments
- OpenAI for GPT API
- ScrapingBee for web scraping API
- Django framework
- Original AI-Web-Scraper project
```



