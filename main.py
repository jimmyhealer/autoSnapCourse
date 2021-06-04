from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import traceback
def getAlert(driver):
  try:
    Alert = driver.switch_to.alert
    AlertText = Alert.text
    return Alert, AlertText
  except:
    return None, 'None'
def main():
  errorMessage = False
  timesCount = 500
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
  i = 0
  while True:
    try:
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
    except:
      if errorMessage:
        print('Connected Error')
        print(time.ctime())
      time.sleep(2)
      continue
    print('begin')
    print(time.ctime())
    try:
      driver.find_element_by_id('Q_COSID').send_keys('B57021RP')
      driver.find_element_by_id('QUERY_COSID_BTN').click()
    except:
      if errorMessage:
        print('Search Cource Error')
        print(time.ctime())
      continue
    time.sleep(0.8)
    timeNow = time.time()
    timeOut = True
    while timeOut:
      time.sleep(0.2)
      if time.time() - timeNow > 30:
        print('Timeout, auto connect')
        timeOut = False
      if i % timesCount == 0: print(i)
      try:
        driver.find_element_by_id('DataGrid1_ctl02_edit').click()
        time.sleep(0.1)
      except Exception as e:
        if errorMessage:
          error_class = e.__class__.__name__
          detail = e.args[0]
          print('Error Code : 1, Error Class : {}'.format(error_class))
          print(detail)
        continue
      try:
        Alert, AlertText = getAlert(driver)
        errorCode = 2
        if AlertText == '本科目設有檢查人數下限。選本課程，在未達下限人數前時無法退選，確定加選?':
          Alert.accept()
          time.sleep(0.5)
          Alert, AlertText = getAlert(driver)
          errorCode = 3
        if AlertText == '年級不可加選！':
          Alert.accept()
          time.sleep(0.5)
          Alert, AlertText = getAlert(driver)
          errorCode = 4
        if AlertText == '衝堂不可選！':
          driver.find_element_by_id('DataGrid3_ctl05_del').click()
          time.sleep(0.5)
          Alert = driver.switch_to.alert
          Alert.accept()
          time.sleep(0.5)
          driver.find_element_by_id('DataGrid1_ctl02_edit').click()
          print('success')
          break
        timeNow = time.time()
      except Exception as e:
        if errorMessage:
          print(time.ctime())
          print(AlertText)
          error_class = e.__class__.__name__
          detail = e.args[0]
          print('Error Code : {}, Error Class : {}'.format(errorCode, error_class))
          print(detail)
        continue
      i += 1
  driver.save_screenshot('./ac.png')
  #input()
  driver.close()
  print('quit')

if __name__ == "__main__":
  print(time.ctime())
  main()
