# beautifulsoup4==4.12.3
# selenium==4.12.0
# webdriver-manager==4.0.0
# pandas==1.4.1

import time
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class FundVoefService:
    @classmethod
    def crawl_fund_voef(cls):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_page_load_timeout(30)

        try:
            driver.get("https://wm.vinacapital.com/investment-solutions/onshore-funds/veof/")
        except TimeoutException:
            print('TimeoutException')
            driver.quit()
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        contents = soup.find('ul', {'id': 'lsvvfff'}).find_all('li')

        for c in contents[::-1]:  # c = contents[0]
            link = c.find('div', {'class': 'w65 rpvbntitle'}).find('a').get('href')
            headline = c.find('div', {'class': 'w65 rpvbntitle'}).find('a').text.strip().replace('Mới', '')
            source = 'voef'
            date = pd.to_datetime(c.find('div', {'class': 'w35 rpvdate'}).find('a').text.strip(), format='%d/%m/%Y').strftime('%Y-%m-%d')
            content = ''


            print(link)
            data = {'source': source,
                    'date': date,
                    'headline': headline,
                    'content': content,
                    'linkWeb': link,
                    }


            time.sleep(1)
        driver.quit()
        print('Done voef')
        return



FundVoefService().crawl_fund_voef()