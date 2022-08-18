# OddsPortalScrape
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
A python script for scraping oddsportal.com

:information_source: Oddsportal.com is sports odds comparison service at Odds Portal lets you compare sports betting odds & betting lines from 80+ major bookmakers.

:information_source: Functionalities :

- Scraping sports: football (all leagues), [more sports will be add soon]
- Scraping options: multiple seasons, only one season, actual season, next matches, any number of pages
- Collects odds from 12 bookmachers: 1xBet, bet-at-home, bet365, Betsson, Betway, bwin, eFortuna.pl, Marathonbet, Pinnacle, STS.pl, Unibet, William Hill (Bookmakers can be edited)
- Script collects: id, date, home team name, away team name, match result, win home odds, draw odds and win away odds for 12 bookmakers

:information_source: Main function example:

```python
scrape_football_seasons(country = "england", league = "premier-league", nseasons = 6, start_season = "2011-2012", pages = 8, file_name = "premier_league_scrape_2011.csv", actual_season = "no", next_matches = "no", username_data = "username_data_ff", password_data = "password_data_ff")
```
- country - the country the league comes from
- league - league name (must be with "-" e.g. ligue-1, serie-a)
- nseasons - number of seasons to scrape
- start_season - season/year first to scrape
- pages - number of pages to scrape per season
- file_name - name of .csv file (if in file any data, scraping will be delete it)
- actual_season - responsible for scraping the current season ("yes" - if you want scrape | "no" - if you not want scrape )
- next_matches - responsible for scraping the next matches ("yes" - if you want scrape | "no" - if you not want scrape )
- username_data - username to login to oddsportal.com
- password_data - password to login to oddsportal.com

:information_source: Scrape actual season function example:

```python
scrape_football_actual_season(country = "england", league = "premier-league", pages = 8, file_name = "premier_league_scrape.csv", id_counter = 0)
```
- country - the country the league comes from
- league - league name (must be with "-" e.g. ligue-1, serie-a)
- pages - number of pages to scrape per season
- file_name - name of .csv file (if in file any data, scraping will be delete it)
- id_counter - number of first id

For working separately, needed to uncomment:

```python
# save data to csv
    #save_csv(file_name)
```
```python
# save data to csv
    save_csv(file_name)
```

:information_source: Scrape next matches function example:

```python
scrape_football_next_matches(country = "germany", league = "bundesliga", file_name = "bundesliga_scrape.csv", id_counter = 0, only = "yes", username_data = username_data_ff, password_data = password_data_ff)
```
- country - the country the league comes from
- league - league name (must be with "-" e.g. ligue-1, serie-a)
- file_name - name of .csv file
- id_counter - number of first id
- only - for working separately set "yes"
- username_data - username to login to oddsportal.com
- password_data - password to login to oddsportal.com

For more efficient scraping and for reducing the risk of error My Bookmakers settings should be edited for:

Settings -> My Bookamkers

![screencapture-oddsportal-my-bookmakers-2022-08-18-20_53_31](https://user-images.githubusercontent.com/50412393/185472473-c4d0bf02-762b-48d2-9b50-efca7590bcf5.png)

:information_source: Scraped data, saved in .csv file example:

![image](https://user-images.githubusercontent.com/50412393/185475568-a8d2ca63-dad4-4b1a-8340-a2615422564a.png)

Extra-documentation can be found in the comments in Scraper.py script.

:information_source: Please report any bug/issue in the issues section or directly at karol.sebastian.kotewicz@gmail.com. Any feedback is really appreciated 💬 👍.
