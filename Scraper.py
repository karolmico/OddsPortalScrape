import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from openpyxl import Workbook
from selenium.common.exceptions import WebDriverException
import pandas as pd
import csv

# AdBlock extension for chrome
path_to_extension = r'E:\Python\OddsPortalScrape\1.43.0_0'

# setups for selenium
options = Options()
options.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=options, executable_path="E:\Python\OddsPortalScrape\chromedriver.exe", )


xBet_H = []
xBet_X = []
xBet_A = []
bet_at_home_H = []
bet_at_home_X = []
bet_at_home_A = []
bet365_H = []
bet365_X = []
bet365_A = []
Betsson_H = []
Betsson_X = []
Betsson_A = []
Betway_H = []
Betway_X = []
Betway_A = []
bwin_H = []
bwin_X = []
bwin_A = []
eFortuna_pl_H = []
eFortuna_pl_X = []
eFortuna_pl_A = []
Marathonbet_H = []
Marathonbet_X = []
Marathonbet_A = []
Pinnacle_H = []
Pinnacle_X = []
Pinnacle_A = []
STS_pl_H = []
STS_pl_X = []
STS_pl_A = []
Unibet_H = []
Unibet_X = []
Unibet_A = []
WilliamHill_H = []
WilliamHill_X = []
WilliamHill_A = []
season = []
home = []
away = []
date = []
score_home = []
score_away = []
id =[]




def scrape_football_seasons(country = "england", league = "premier-league", nseasons = 5, start_season = "2020-2021", pages = 8, file_name = "premier_league_scrape.csv"):
    # Creating web link
    driver.get(f'https://www.oddsportal.com/soccer/{country}/{league}-{start_season}/results/'.format(country = country, league = league, start_season = start_season))
    # function to create header in csv file
    csv_header(file_name)
    id_counter = 0
    xBet_t = 0
    bet_at_home_t = 0
    bet365_t = 0
    Betsson_t = 0
    Betway_t = 0
    bwin_t = 0
    eFortuna_pl_t = 0
    Marathonbet_t = 0
    Pinnacle_t = 0
    STS_pl_t = 0
    Unibet_t = 0
    WilliamHill_t = 0
    # number of pages
    for j in range(pages):

        # number of games per page
        for k in range(4, 85):
            # Accept cookies
            if driver.find_elements(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'):
                cookies_accept_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
            if driver.find_elements(By.XPATH, '//*[@id="tournamentTable"]/tbody/tr[%d]/td[2]/a' % k):
                match_details_link = driver.find_element(By.XPATH,
                                              '//*[@id="tournamentTable"]/tbody/tr[%d]/td[2]/a' % k).click()
                id_counter = id_counter + 1
                id.append(id_counter)
            if driver.find_elements(By.XPATH, '//*[@id="col-content"]/h1[contains(text(), " - ")]'):
                home_t = driver.find_element(By.XPATH, '//*[@id="col-content"]/h1')
                #home_t.text.replace(' - ', ' ')
                temp = home_t.text.split(" - ")
                home.append(temp[0])
                away.append(temp[1])
                temp.clear()

            if driver.find_elements(By.XPATH, '//*[@id="col-content"]/p[1][contains(text(), ",")]'):
                date_t = driver.find_element(By.XPATH, '//*[@id="col-content"]/p[1]')
                date.append(date_t.text)

            if driver.find_elements(By.XPATH, '//*[@id="event-status"]/p/strong'):
                score_home_t = driver.find_element(By.XPATH, '//*[@id="event-status"]/p/strong')
                #score_home_t.text.replace(':', ' ')
                temp2 = score_home_t.text.split(":")
                score_home.append(temp2[0])
                score_away.append(temp2[1])
                temp2.clear()

            # scrape odds
            for m in range(25):
                if driver.find_elements(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[1]/div/a[2]' % m):
                    test_value = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[1]/div/a[2]' % m).text
                    if (test_value == "1xBet") :
                        xBet_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        xBet_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        xBet_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        xBet_H.append(xBet_H_t.text.replace('.', ','))
                        xBet_X.append(xBet_X_t.text.replace('.', ','))
                        xBet_A.append(xBet_A_t.text.replace('.', ','))
                        xBet_t = 1
                    if (test_value == "bet-at-home"):
                        bet_at_home_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        bet_at_home_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        bet_at_home_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        bet_at_home_H.append(bet_at_home_H_t.text.replace('.', ','))
                        bet_at_home_X.append(bet_at_home_X_t.text.replace('.', ','))
                        bet_at_home_A.append(bet_at_home_A_t.text.replace('.', ','))
                        bet_at_home_t = 1
                    if (test_value == "bet365"):
                        bet365_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        bet365_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        bet365_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        bet365_H.append(bet365_H_t.text.replace('.', ','))
                        bet365_X.append(bet365_X_t.text.replace('.', ','))
                        bet365_A.append(bet365_A_t.text.replace('.', ','))
                        bet365_t = 1
                    if (test_value == "Betsson"):
                        Betsson_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        Betsson_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        Betsson_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        Betsson_H.append(Betsson_H_t.text.replace('.', ','))
                        Betsson_X.append(Betsson_X_t.text.replace('.', ','))
                        Betsson_A.append(Betsson_A_t.text.replace('.', ','))
                        Betsson_t = 1
                    if (test_value == "Betway"):
                        Betway_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        Betway_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        Betway_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        Betway_H.append(Betway_H_t.text.replace('.', ','))
                        Betway_X.append(Betway_X_t.text.replace('.', ','))
                        Betway_A.append(Betway_A_t.text.replace('.', ','))
                        Betway_t = 1
                    if (test_value == "bwin"):
                        bwin_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        bwin_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        bwin_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        bwin_H.append(bwin_H_t.text.replace('.', ','))
                        bwin_X.append(bwin_X_t.text.replace('.', ','))
                        bwin_A.append(bwin_A_t.text.replace('.', ','))
                        bwin_t = 1
                    if (test_value == "eFortuna.pl"):
                        eFortuna_pl_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        eFortuna_pl_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        eFortuna_pl_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        eFortuna_pl_H.append(eFortuna_pl_H_t.text.replace('.', ','))
                        eFortuna_pl_X.append(eFortuna_pl_X_t.text.replace('.', ','))
                        eFortuna_pl_A.append(eFortuna_pl_A_t.text.replace('.', ','))
                        eFortuna_pl_t = 1
                    if (test_value == "Marathonbet"):
                        Marathonbet_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        Marathonbet_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        Marathonbet_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        Marathonbet_H.append(Marathonbet_H_t.text.replace('.', ','))
                        Marathonbet_X.append(Marathonbet_X_t.text.replace('.', ','))
                        Marathonbet_A.append(Marathonbet_A_t.text.replace('.', ','))
                        Marathonbet_t = 1
                    if (test_value == "Pinnacle"):
                        Pinnacle_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        Pinnacle_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        Pinnacle_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        Pinnacle_H.append(Pinnacle_H_t.text.replace('.', ','))
                        Pinnacle_X.append(Pinnacle_X_t.text.replace('.', ','))
                        Pinnacle_A.append(Pinnacle_A_t.text.replace('.', ','))
                        Pinnacle_t = 1
                    if (test_value == "STS.pl"):
                        STS_pl_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        STS_pl_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        STS_pl_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        STS_pl_H.append(STS_pl_H_t.text.replace('.', ','))
                        STS_pl_X.append(STS_pl_X_t.text.replace('.', ','))
                        STS_pl_A.append(STS_pl_A_t.text.replace('.', ','))
                        STS_pl_t = 1
                    if (test_value == "Unibet"):
                        Unibet_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        Unibet_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        Unibet_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        Unibet_H.append(Unibet_H_t.text.replace('.', ','))
                        Unibet_X.append(Unibet_X_t.text.replace('.', ','))
                        Unibet_A.append(Unibet_A_t.text.replace('.', ','))
                        Unibet_t = 1
                    if (test_value == "William Hill"):
                        WilliamHill_H_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[2]/div' % m)
                        WilliamHill_X_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[3]/div' % m)
                        WilliamHill_A_t = driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/tbody/tr[%d]/td[4]/div' % m)
                        WilliamHill_H.append(WilliamHill_H_t.text.replace('.', ','))
                        WilliamHill_X.append(WilliamHill_X_t.text.replace('.', ','))
                        WilliamHill_A.append(WilliamHill_A_t.text.replace('.', ','))
                        WilliamHill_t = 1
                    driver.back()

            if (xBet_t == 1):
                xBet_t = 0
            else:
                xBet_H.append(" ")
                xBet_X.append(" ")
                xBet_A.append(" ")
            if (bet_at_home_t == 1):
                bet_at_home_t = 0
            else:
                bet_at_home_H.append(" ")
                bet_at_home_X.append(" ")
                bet_at_home_A.append(" ")
            if (bet365_t == 1):
                bet365_t = 0
            else:
                bet365_H.append(" ")
                bet365_X.append(" ")
                bet365_A.append(" ")
            if (Betway_t == 1):
                Betway_t = 0
            else:
                Betway_H.append(" ")
                Betway_X.append(" ")
                Betway_A.append(" ")
            if (Betsson_t == 1):
                Betsson_t = 0
            else:
                Betsson_H.append(" ")
                Betsson_X.append(" ")
                Betsson_A.append(" ")
            if  (bwin_t == 1):
                bwin_t = 0
            else:
                bwin_H.append(" ")
                bwin_X.append(" ")
                bwin_A.append(" ")
            if  (eFortuna_pl_t == 1):
                eFortuna_pl_t = 0
            else:
                eFortuna_pl_H.append(" ")
                eFortuna_pl_X.append(" ")
                eFortuna_pl_A.append(" ")
            if (Marathonbet_t == 1):
                Marathonbet_t = 0
            else:
                Marathonbet_H.append(" ")
                Marathonbet_X.append(" ")
                Marathonbet_A.append(" ")
            if (Pinnacle_t == 1):
                Pinnacle_t = 0
            else:
                Pinnacle_H.append(" ")
                Pinnacle_X.append(" ")
                Pinnacle_A.append(" ")
            if (STS_pl_t == 1):
                STS_pl_t = 0
            else:
                STS_pl_H.append(" ")
                STS_pl_X.append(" ")
                STS_pl_A.append(" ")
            if (Unibet_t == 1):
                Unibet_t = 0
            else:
                Unibet_H.append(" ")
                Unibet_X.append(" ")
                Unibet_A.append(" ")
            if (WilliamHill_t == 1):
                WilliamHill_t = 0
            else:
                WilliamHill_H.append(" ")
                WilliamHill_X.append(" ")
                WilliamHill_A.append(" ")


    save_csv(file_name)




def csv_header(file_name):
    header = ['Id' + ";" + 'Date' + ";" + 'Home' + ";" + 'Away' + ";" + 'Score_Home' + ";" + 'Score_Away' + ";" + '1xBet_H' + ";" + '1xBet_X' + ";" + '1xBet_A' + ";" + 'bet-at-home_H' + ";" + 'bet-at-home_X' + ";" + 'bet-at-home_A' + ";" + 'bet365_H' + ";" + 'bet365_X' + ";" + 'bet365_A' + ";" + 'Betsson_H' + ";" + 'Betsson_X' + ";" + 'Betsson_A' + ";" + 'Betway_H' + ";" + 'Betway_X' + ";" + 'Betway_A' + ";" + 'bwin_H' + ";" + 'bwin_X' + ";" + 'bwin_A' + ";" + 'eFortuna.pl_H' + ";" + 'eFortuna.pl_X' + ";" + 'eFortuna.pl_A' + ";" + 'Marathonbet_H' + ";" + 'Marathonbet_X' + ";" + 'Marathonbet_A' + ";" + 'Pinnacle_H' + ";" + 'Pinnacle_X' + ";" + 'Pinnacle_A' + ";" + 'STS.pl_H' + ";" + 'STS.pl_X' + ";" + 'STS.pl_A' + ";" + 'Unibet_H' + ";" + 'Unibet_X' + ";" + 'Unibet_A' + ";" + 'WilliamHill_H' + ";" + 'WilliamHill_X' + ";" + 'WilliamHill_A']

    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)

def save_csv(file_name):
    # Save results to excel
    with open(file_name, 'a') as file:
        for i in range(len(id)):
            file.write(
                str(id[i]) + ";" + date[i] + ";" + home[i] + ";" + away[i] + ";" + score_home[i] + ";" + score_away[i] + ";" + xBet_H[i] + ";" + xBet_X[i] + ";" + xBet_A[i] + ";" + bet_at_home_H[i] + ";" + bet_at_home_X[i] + ";" +  bet_at_home_A[i] + ";" + bet365_H[i] + ";" + bet365_X[i] + ";" + bet365_A[i] + ";" + Betsson_H[i] + ";" + Betsson_X[i] + ";" + Betsson_A[i] + ";" + Betway_H[i] + ";" + Betway_X[i] + ";" + Betway_A[i] + ";" + bwin_H[i] + ";" + bwin_X[i] + ";" + bwin_A[i] + ";" + eFortuna_pl_H[i] + ";" + eFortuna_pl_X[i] + ";" + eFortuna_pl_A[i] + ";" + Marathonbet_H[i] + ";" + Marathonbet_X[i] + ";" + Marathonbet_A[i] + ";" + Pinnacle_H[i] + ";" + Pinnacle_X[i] + ";" + Pinnacle_A[i] + ";" + STS_pl_H[i] + ";" + STS_pl_X[i] + ";" + STS_pl_A[i] + ";" + Unibet_H[i] + ";" + Unibet_X[i] + ";" + Unibet_A[i] + ";" + WilliamHill_H[i] + ";" + WilliamHill_X[i] + ";" + WilliamHill_A[i] + "\n")
        file.close()

scrape_football_seasons("england", "premier-league", 1, "2018-2019", 1, "test.csv")