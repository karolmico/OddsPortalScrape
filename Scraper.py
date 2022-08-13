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
import pandas as pd

# AdBlock extension for chrome
path_to_extension = r'E:\Python\OddsPortal Scrape\1.43.0_0'

# setups for selenium
options = Options()
options.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=options, executable_path="E:\Python\OddsPortal Scrape\chromedriver.exe", )

driver.get('https://www.oddsportal.com/soccer/england/premier-league/results/')