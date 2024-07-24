# Odds Analysis
This project involves scraping data about football matches, manipulating it, storing it in a database, and creating analysis about it.
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

# Overview

https://github.com/user-attachments/assets/b3388dab-9a2b-4906-b21c-5d627e397e05


The process includes the following steps:

<table>
  <tr valign="top">    
 <td><h2>1. Data Scraping</h2><br>Upon starting the scraper, a Graphical User Interface (GUI) appears where users can select football seasons from <strong>2018-2019</strong> to <strong>2022-2023</strong> across <strong>15</strong> different leagues. This totals to <strong>75 total seasons</strong> and <strong>more than 24,000 matches</strong> played.</td>
 <td width="480">
<img width="480" src="https://github.com/user-attachments/assets/975ad2de-1688-46ae-b3a8-cd523295fa26" alt="GUI">
</td>
  </tr>
</table> 

---

<h2>2. Data Manipulation</h2>The program scrapes data about football matches and manipulates it, creating additional fields. For instance:<br><br>
  
 <div>
<table>
  <tr align="center">
    <th>Home Team</th>
    <th>Home Team Goals</th>
    <th>Result</th>
    <th>Away Team</th>
    <th>Home Odds</th>
    <th>Draw Odds</th>
    <th>Away Odds</th>
    <th>Winner Odds</th>
  </tr>
<tr align="center">
    <td>Athletic Bilbao</td>
    <td>2</td>
    <td>2 - 1</td>
    <td>Leganes</td>
    <td>1.83</td>
    <td>3.90</td>
    <td>6.00</td>
    <td>1.83</td>
  </tr>
<tr align="center">
    <td>Valencia</td>
    <td>1</td>
    <td>1 - 1</td>
    <td>Sevilla</td>
    <td>2.10</td>
    <td>3.50</td>
    <td>4.50</td>
    <td>3.50</td>
  </tr>
</table>
 </div>
 
---

<h2>3. Subtables</h2> After manipulating the dataframe, it creates five optimized subtables, each serving a specific purpose:

   <br><br>
   
 <div align="center">
   <div>
     <strong>Date Subtable</strong>                                  
     This subtable contains information about the date of the match.
     <br><br>

  | Header  | Description                         |
  |---------|-------------------------------------|
  | ID      | Unique identifier for the match     |
  | Season  | The season of the match             |
  | Quarter | The quarter of the match            |
   </div>
 </div>
         <br><br>
         
 <div align="center">
   <div>
     <strong>Teams Subtable</strong>
     This subtable lists the teams involved in each match.
      <br><br>
      
  | Header       | Description                         |
  |--------------|-------------------------------------|
  | ID           | Unique identifier for the match     |
  | Home Team    | The home team                       |
  | Away Team    | The away team                       |
  | Winner Team  | The winning team (if available)     |
</div>
 </div>

---
 
<h2>4. Database Integration</h2> Then, the program inputs the tables into the specified database. <br><br>

<table>
  <tr>
    <td ><img src="https://github.com/tothadam500/Odds/assets/129130362/db9b8b5d-9ebc-4bd2-a98f-7a8e44992a81"></td>
    <td width="70%"><img src="https://github.com/tothadam500/Odds/assets/129130362/9abf34fc-f503-4344-9786-2046c9887abe" alt="database"></td>
  </tr>
</table>

---

<table>
  <tr valign="top">
    <td><h2>5. Data Visualization</h2> 
Use Tableau to generate three reports employing distinct strategies: exclusively betting on draws, on the greatest odd, or on a number.</td>
    <td width=500 ><img src="https://github.com/user-attachments/assets/270f8e31-2c7b-4f47-90bd-f66ffbb27fba" src="tableu_img"></td>
  </tr>
</table>

