from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

from webdriver import Webdriver
from transformData import TransformData


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

base_xpath = '/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/div[3]/table/tbody/tr'


def is_valid(match_item):
    max_odds_threshold = 20

    r = match_item["Result"]
    if r == "-":
        return False

    teams = [match_item["Home Team"], match_item["Away Team"]]
    if "" in teams:
        return False

    odds = [match_item["Home Odds"], match_item["Draw Odds"], match_item["Away Odds"]]
    valid_odds_count = sum(1 for odd in odds if odd >= 3)
    if valid_odds_count == 3:
        return False
    if any(odd > max_odds_threshold for odd in odds):
        return False
    if 0 in odds or 1 in odds:
        return False
    return True


class Scraper:
    def __init__(self, urls):
        self.urls = urls
        self.driver = Webdriver().get_driver()
        self.columns = ["Home Team", "Away Team", "Home Odds", "Draw Odds", "Away Odds", "Result", "URL"]
        for url in self.urls:
            print(f"Currently scraping -> {url}")
            self.start_scraper(url)
        self.driver.quit()

    def start_scraper(self, url):
        df = pd.DataFrame(columns=self.columns)

        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, '//*[@id="events-tab-future"]'))).click()
        except Exception as e:
            print(e)

        max_range = len(self.driver.find_elements(By.TAG_NAME, 'tr'))
        for i in range(max_range):
            try:
                xpath = f'{base_xpath}[{i}]/td'
                home_team = self.driver.find_element(by=By.XPATH, value=xpath + '[4]/a/span').text
                away_team = self.driver.find_element(by=By.XPATH, value=xpath + '[6]/a').text
                home_odds = float(self.driver.find_element(by=By.XPATH, value=xpath + '[8]').text)
                draw_odds = float(self.driver.find_element(by=By.XPATH, value=xpath + '[9]').text)
                away_odds = float(self.driver.find_element(by=By.XPATH, value=xpath + '[10]').text)
                result = self.driver.find_element(by=By.XPATH, value=xpath + '[5]/a').text

                match = {
                    "Home Team": home_team,
                    "Away Team": away_team,
                    "Home Odds": home_odds,
                    "Draw Odds": draw_odds,
                    "Away Odds": away_odds,
                    "Result": result,
                    "URL": url
                }

                if is_valid(match):
                    match_values = list(match.values())
                    df.loc[len(df)] = match_values

            except NoSuchElementException:
                pass
            except Exception as e:
                print('Error:', str(e))

        df.reset_index(drop=True, inplace=True)
        TransformData(df)
