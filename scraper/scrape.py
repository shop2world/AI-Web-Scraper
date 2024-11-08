from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import logging

# 셀레니움 로깅 레벨 설정
logging.getLogger('selenium').setLevel(logging.WARNING)

load_dotenv()

def scrape_website(website):
    print("Connecting to Chrome Browser...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 헤드리스 모드
    chrome_options.add_argument('--log-level=3')  # 로그 레벨 최소화
    chrome_options.add_argument('--disable-logging')  # 로깅 비활성화
    chrome_options.add_argument('--disable-dev-shm-usage')  # 공유 메모리 사용 비활성화
    chrome_options.add_argument('--no-sandbox')  # 샌드박스 비활성화
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # DevTools 로깅 비활성화
    
    service = Service(
        executable_path=os.getenv("SBR_WEBDRIVER"),
        log_output=os.devnull  # 서비스 로그 출력 무시
    )
    
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(website)
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html
    except Exception as e:
        print(f"Error during scraping: {str(e)}")
        raise
    finally:
        try:
            driver.quit()
        except:
            pass

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ] 