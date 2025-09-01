# Odds Analysis

End-to-end analytics project combining **Python**, **PostgreSQL**, and **Tableau**.  
The workflow covers **data scraping**, **transformation**, **relational database design**, and **interactive reporting**.  

<p>
  <span style="display: inline-block; margin-right: 20px; vertical-align: middle;">
    <img width="40" src="https://github.com/tothadam500/Odds/assets/129130362/00b2b9f2-5d3d-4f94-8579-050300b1ac88.png" alt="Python_Logo">
    <strong>Python</strong>
  </span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

  <span style="display: inline-block; margin-right: 20px; vertical-align: middle;">
    <img width="40" src="https://github.com/user-attachments/assets/47005b5c-6382-48c6-8a01-ef41b5a00511" alt="PostgreSQL_Logo">
    <strong>PostgreSQL</strong>
  </span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

  <span style="display: inline-block; vertical-align: middle;">
    <img width="40" src="https://github.com/tothadam500/Odds/assets/129130362/5dc5370c-3915-48ad-b574-438e64b38ad0.png" alt="Tableau_Logo">
    <strong>Tableau</strong>
  </span>
</p>

---

## 🔍 Highlights
- **Dynamic scraping** of 75 football seasons (2018–2023), covering **15 leagues** and **24K+ matches**.  
- **Automated data cleaning and enrichment** in Python (winner odds, goals, match metadata).  
- **Optimized subtables** designed in a relational schema for efficient queries.  
- **Database integration**: transformed data written to **PostgreSQL**.  
- **Visualization**: Tableau dashboards analyzing betting strategies (draws, max odds, specific numbers).  

---

## ⚙️ Project Steps

### 1) Data Scraping
Interactive **GUI** allows season/league selection.  
Covers 75 seasons (2018–2023) across 15 European leagues.  

<img width="480" src="https://github.com/user-attachments/assets/975ad2de-1688-46ae-b3a8-cd523295fa26" alt="GUI" />

---

### 2) Data Manipulation
Data scraped from match results and enriched with calculated fields (e.g., `Winner Odds`).  

Example records:  

| Home Team        | Result | Away Team | Home Odds | Draw Odds | Away Odds | Winner Odds |
|------------------|--------|-----------|-----------|-----------|-----------|-------------|
| Athletic Bilbao  | 2 - 1  | Leganes   | 1.83      | 3.90      | 6.00      | 1.83        |
| Valencia         | 1 - 1  | Sevilla   | 2.10      | 3.50      | 4.50      | 3.50        |

---

### 3) Subtables
The dataset is normalized into **five subtables** for optimized storage and analysis.  

**Date Subtable**  
| Header  | Description |
|---------|-------------|
| ID      | Unique match identifier |
| Season  | Match season |
| Quarter | Calendar quarter |

**Teams Subtable**  
| Header       | Description |
|--------------|-------------|
| ID           | Unique match identifier |
| Home Team    | Home team |
| Away Team    | Away team |
| Winner Team  | Winning team (if available) |

(Similar subtables exist for odds, results, and metadata.)

---

### 4) Database Integration
Transformed data is written into a **PostgreSQL** relational database.  
This ensures structured storage, indexing, and downstream BI access.  

<img src="https://github.com/tothadam500/Odds/assets/129130362/db9b8b5d-9ebc-4bd2-a98f-7a8e44992a81" width="300" />  
<img src="https://github.com/tothadam500/Odds/assets/129130362/9abf34fc-f503-4344-9786-2046c9887abe" width="500" />

---

### 5) Data Visualization
Three **Tableau dashboards** were created to test different betting strategies:  
- Betting only on **draws**  
- Betting on the **highest odd** available  
- Betting on a **specific number**  

<img width="500" src="https://github.com/user-attachments/assets/270f8e31-2c7b-4f47-90bd-f66ffbb27fba" alt="tableau_img" />

---

## 🛠️ Skills Demonstrated
- **Python**: web scraping (requests/selenium), pandas transformations, GUI with tkinter.  
- **SQL / PostgreSQL**: schema design, relational joins, efficient inserts.  
- **Data modeling**: normalized subtables for querying and reporting.  
- **Tableau**: interactive dashboards, strategy comparison, visualization design.  
- **End-to-end BI workflow**: from raw data → DB → dashboard.  

---

---

## 🐍 Example: Web Scraping with Selenium

The scraper uses **Selenium** to extract match data (teams, odds, results) from betting websites.  
Invalid or extreme values are filtered out before loading into PostgreSQL.  

```python
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

# Basic match validation
def is_valid(match_item):
    max_odds_threshold = 20
    r = match_item["Result"]
    if r == "-" or "" in [match_item["Home Team"], match_item["Away Team"]]:
        return False
    odds = [match_item["Home Odds"], match_item["Draw Odds"], match_item["Away Odds"]]
    if sum(1 for odd in odds if odd >= 3) == 3 or any(odd > max_odds_threshold for odd in odds):
        return False
    if 0 in odds or 1 in odds:
        return False
    return True

# Scraper class (simplified)
class Scraper:
    def __init__(self, urls):
        self.urls = urls
        self.driver = Webdriver().get_driver()
        self.columns = ["Home Team", "Away Team", "Home Odds", "Draw Odds", "Away Odds", "Result", "URL"]

    def start_scraper(self, url):
        df = pd.DataFrame(columns=self.columns)
        self.driver.get(url)

        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="events-tab-future"]'))
        ).click()

        for i, row in enumerate(self.driver.find_elements(By.TAG_NAME, 'tr')):
            try:
                xpath = f'/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{i}]/td'
                home_team = self.driver.find_element(By.XPATH, xpath + '[4]/a/span').text
                away_team = self.driver.find_element(By.XPATH, xpath + '[6]/a').text
                home_odds = float(self.driver.find_element(By.XPATH, xpath + '[8]').text)
                draw_odds = float(self.driver.find_element(By.XPATH, xpath + '[9]').text)
                away_odds = float(self.driver.find_element(By.XPATH, xpath + '[10]').text)
                result = self.driver.find_element(By.XPATH, xpath + '[5]/a').text

                match = {"Home Team": home_team, "Away Team": away_team,
                         "Home Odds": home_odds, "Draw Odds": draw_odds,
                         "Away Odds": away_odds, "Result": result, "URL": url}

                if is_valid(match):
                    df.loc[len(df)] = list(match.values())

            except NoSuchElementException:
                pass
        return df
```

## 📌 Notes
- Covers 24K+ football matches from 2018–2023.  
- Code structured for scalability (adding more seasons/leagues easily).  
- PostgreSQL schema designed for downstream analytics or integration with BI tools.  

