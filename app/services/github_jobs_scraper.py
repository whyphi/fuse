from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
from typing import List, Dict
import re

class GitHubJobsScraper:
    def __init__(self):
        pass  # No persistent driver

    def _create_webdriver(self, *chrome_args: str) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        default_args = ["--headless", "--disable-gpu", "--no-sandbox"]
        args_to_use = chrome_args if chrome_args else default_args
        for arg in args_to_use:
            options.add_argument(arg)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def get_jobs(self, urlStr) -> List[Dict]:
        driver = self._create_webdriver()
        try:
            driver.get(urlStr)
            table = driver.find_element(By.TAG_NAME, "table")
            body = table.find_element(By.TAG_NAME, "tbody")
            rows = body.find_elements(By.TAG_NAME, "tr")

            prevRowCompany = ""
            jobs = []
            for row in rows:
                cols = row.find_elements(By.XPATH, "td")
                date = cols[-1].text
                if self.is_more_than_one_week_ago(date):
                    break

                company = ""
                role = ""
                link = ""

                try:
                    company = (
                        cols[0]
                        .find_element(By.TAG_NAME, "strong")
                        .find_element(By.TAG_NAME, "a")
                        .text
                    )
                    prevRowCompany = company
                except NoSuchElementException:
                    try:
                        company = cols[0].text
                        if company == "↳":
                            company = prevRowCompany
                        else:
                            prevRowCompany = company
                    except Exception:
                        company = "N/A"

                try:
                    role = (
                        cols[1]
                        .find_element(By.TAG_NAME, "strong")
                        .find_element(By.TAG_NAME, "a")
                        .text
                    )
                    link = (
                        cols[1]
                        .find_element(By.TAG_NAME, "strong")
                        .find_element(By.TAG_NAME, "a")
                        .get_attribute("href")
                    )
                except NoSuchElementException:
                    role = cols[1].text

                if link == "":
                    link = cols[3].find_element(By.TAG_NAME, "a").get_attribute("href")

                newJob = {"company": company, "role": role, "link": link, "date": date}
                jobs.append(newJob)

            return jobs
        finally:
            driver.quit()

    def is_more_than_one_week_ago(self, dateStr: str) -> bool:
        try:
            current_year = datetime.today().year
            today = datetime.today()
            date_obj = datetime.strptime(f"{dateStr} {current_year}", "%b %d %Y")
            one_week_ago = today - timedelta(days=8)
            if date_obj < one_week_ago:
                return True
            return False
        except ValueError as e:
            # Hotfix: if dateStr is not in the format "Mon DD", but instead in the format 'DDd', i.e. "15d"
            try:
                date_obj = dateStr[:-1]
                if int(date_obj) >= 7:
                    return True
                return False
            except (ValueError, IndexError):
                return False 