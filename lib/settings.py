from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def _init(headless = True):
  capa = DesiredCapabilities.CHROME
  capa["pageLoadStrategy"] = "none"
  ch_options = Options()
  ch_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  if headless : ch_options.add_argument('--headless')
  driver = webdriver.Chrome(options = ch_options, desired_capabilities=capa)
  return driver