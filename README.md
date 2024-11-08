# AI Web Scraper

A Django-based web scraper that uses AI to analyze web content.

## Features
- Web content scraping
- AI-powered content analysis using OpenAI GPT
- Clean and simple user interface

## Prerequisites
- Python 3.8+
- Chrome WebDriver
- OpenAI API key

## Installation

1. Clone the repository:

git clone https://github.com/shop2world/AI-Web-Scraper.git


2. Create and activate virtual environment:


# Windows

python -m venv venv


macOS/Linux
python -m venv venv
source venv/bin/activate


3. Install required packages:

pip install -r requirements.txt

4. Set up environment variables:
- Copy `.env.example` to `.env`
- Update `.env` with your actual credentials:


5. Run migrations:

python manage.py migrate

6. Start the development server:

python manage.py runserver

## Usage
1. Access the application at `http://localhost:8000`
2. Enter the URL you want to scrape
3. Describe what you want to analyze
4. Click "Scrape and Parse" to get results

## Environment Variables
| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | Your OpenAI API key |
| `SBR_WEBDRIVER` | Path to Chrome WebDriver |

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security Notice
- Never commit your `.env` file
- Keep your API keys private
- Regularly rotate your credentials

## License
This project is licensed under the MIT License 

## Acknowledgments
- OpenAI for providing the GPT API
- Beautiful Soup for web scraping capabilities
- Django framework
