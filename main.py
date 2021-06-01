from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time
def main():
  f = open('./user.txt')
  username = f.readline().strip()
  password = f.readline().strip()
  capa = DesiredCapabilities.CHROME
  capa["pageLoadStrategy"] = "none"
  ch_options = Options()
  ch_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  ch_options.add_argument('--headless')

  # for linux
  #driver = webdriver.Chrome('./chromedriver', options = ch_options)

  # for windows
  driver = webdriver.Chrome(options = ch_options, desired_capabilities=capa)

  driver.get('https://ais.ntou.edu.tw/Default.aspx')
  driver.implicitly_wait(4)
  driver.find_element_by_name('M_PW').send_keys(password)
  driver.find_element_by_id('M_PORTAL_LOGIN_ACNT').send_keys(username)
  driver.find_element_by_id('LGOIN_BTN').click()
  driver.switch_to.frame('menuFrame')
  driver.find_element_by_id('Menu_TreeViewt1').click()
  driver.find_element_by_id('Menu_TreeViewt30').click()
  driver.find_element_by_id('Menu_TreeViewt40').click()
  driver.switch_to.default_content()
  driver.switch_to.frame('mainFrame')
  print('begin')
  i = 0
  print(time.ctime())
  driver.find_element_by_id('Q_COSID').send_keys('B57021RP')
  driver.find_element_by_id('QUERY_COSID_BTN').click()
  time.sleep(1)
  while True:
    if i % 50 == 0: print(i)
    try:
      driver.find_element_by_id('DataGrid1_ctl02_edit').click()
      Alert = driver.switch_to.alert
      AlertText = Alert.text
      Alert.accept()
      time.sleep(1)
      try:
        Alert.accept()
      except:
        time.sleep(1)
        Alert.accpet()
    except:
      print(time.ctime())
      print(AlertText)
      if AlertText == '衝堂不可選!':
        driver.find_element_by_id('DataGrid3_ctl05_del').click()
        Alert = driver.switch_to.alert
        Alert.accpet()
        driver.find_element_by_id('DataGrid1_ctl02_edit').click()
        print('success')
      else:
        print('error')
      break
    i += 1
  driver.save_screenshot('./ac.png')
  #input()
  driver.close()
  print('quit')

if __name__ == "__main__":
  main()
