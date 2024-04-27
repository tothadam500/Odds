# Odds Analysis

## Overview

This project involves scraping data about football matches, manipulating it, and storing it in a database. The process includes the following steps:

1. **Data Scraping**: Upon starting the scraper, a Graphical User Interface (GUI) appears where users can select football seasons from *2018-2019* to *2022-2023* across *15* different leagues. This totals to **75 total seasons** and **more than 24,000 matches** played.

   ![Scraper GUI](https://github.com/tothadam500/Odds/assets/129130362/b3924ac0-03f4-434d-b10b-fee1589f8629.png)

2. **Data Manipulation**: The program scrapes data about football matches and manipulates it, creating additional fields. For instance:

    | Home Team        | Home Team Goals | Result | Away Team | Home Odds | Draw Odds | Away Odds | Winner Odds |
    |------------------|-----------------|--------|-----------|------------|-----------|------------|-------------|
    | Athletic Bilbao | 2               | 2 - 1  | Leganes   | 1.83       | 3.90      | 6.00       | 1.83        |

3. **Optimized Subtables Creation**: After manipulating the dataframe, it creates five optimized subtables, each serving a specific purpose:

    - **Date Subtable**: Contains information about the date of the match.
    - **Teams Subtable**: Lists the teams involved in each match.

    <div style="display: flex; justify-content: space-between;">
      <div style="flex: 1;">
        <strong>Date Subtable</strong>                                  
        This subtable contains information about the date of the match.

        | Header  | Description                         |
        |---------|-------------------------------------|
        | ID      | Unique identifier for the match     |
        | Season  | The season of the match             |
        | Quarter | The quarter of the match            |
      </div>
    </div>

    <div style="display: flex; justify-content: space-between;">
      <div style="flex: 1;">
        <strong>Teams Subtable</strong>
        This subtable lists the teams involved in each match.

        | Header       | Description                         |
        |--------------|-------------------------------------|
        | ID           | Unique identifier for the match     |
        | Home Team    | The home team                       |
        | Away Team    | The away team                       |
        | Winner Team  | The winning team (if available)     |
      </div>
    </div>

4. **Database Integration**: Finally, the program inputs the tables into the specified database.

   ![Database Integration](https://github.com/tothadam500/Odds/assets/129130362/769fc295-1524-4408-a867-b719e807901e.png)

---

This README provides an overview of the project, including its workflow and key components.
