from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time
def main():
  f = open('./user.txt')
  username = f.readline().strip()
  password = f.readline().strip()
  print(username, password)
  capa = DesiredCapabilities.CHROME
  capa["pageLoadStrategy"] = "none"
  ch_options = Options()
  ch_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  #ch_options.add_argument('--headless')

  #driver = webdriver.Chrome('./chromedriver', options = ch_options)
  driver = webdriver.Chrome(options = ch_options, desired_capabilities=capa)

  driver.get('https://ais.ntou.edu.tw/Default.aspx')
  driver.implicitly_wait(5)
  driver.find_element_by_name('M_PW').send_keys(password)
  driver.find_element_by_id('M_PORTAL_LOGIN_ACNT').send_keys(username)
  driver.find_element_by_id('LGOIN_BTN').click()
  driver.switch_to.frame('menuFrame')
  driver.find_element_by_id('Menu_TreeViewt1').click()
  driver.find_element_by_id('Menu_TreeViewt30').click()
  driver.find_element_by_id('Menu_TreeViewt40').click()
  driver.save_screenshot('./ac.png')
  driver.close()
  print('quit')

if __name__ == "__main__":
  main()
