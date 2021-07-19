import time
import lib.globalvar as gl

def get_time():
  return time.time()

def get_ctime():
  return time.ctime()

def get_alert(driver):
  try:
    Alert = driver.switch_to.alert
    AlertText = Alert.text
    return Alert, AlertText
  except:
    return None, 'None'

def accept_alert(driver):
  infos = ['本科目設有檢查人數下限。選本課程，在未達下限人數前時無法退選，確定加選?', '年級不可加選！', '衝堂不可選！']
  try:
    Alert, AlertText = get_alert(driver)
    errorCode = 2
    if AlertText == infos[2]:
      drop_course(driver)     
      time.sleep(0.5)
      driver.find_element_by_id('DataGrid1_ctl02_edit').click()
      print('success')
    elif AlertText in infos:
      Alert.accept()
      time.sleep(0.5)
      Alert, AlertText = get_alert(driver)
      errorCode = 3
    return True
  except Exception as e:
    if gl.get('errorMessage'):
      print(time.ctime())
      print(AlertText)
      print('Error Code : {}\nError Info : {}'.format(errorCode, e))
    return False

def get_course(driver, course, types = 1):
  if types == 1:
    try:
      driver.find_element_by_id('Q_COSID').send_keys(course)
      driver.find_element_by_id('QUERY_COSID_BTN').click()
      return True
    except Exception as e:
      if gl.get('errorMessage', False):
        print('Search Cource Error')
        print(e)
        print(time.ctime())
      return False
  elif types == 2:
    driver.finds_element_by_id('Q_NOT_MAX_ST').click()
    driver.finds_element_by_id('QUERY_BTN1').click()
    time.sleep(1)
    return True

def choose_course(driver):  
  try:
    time.sleep(0.1)
    driver.find_element_by_id('DataGrid1_ctl02_edit').click()
    return True
  except Exception as e:
    if gl.get('errorMessage', False):
      print('Error Code : 1\nError Info : {}'.format(e))
    return False

def drop_course(driver):
  driver.find_element_by_id('DataGrid3_ctl05_del').click()
  time.sleep(0.5)
  Alert = driver.switch_to.alert
  Alert.accept()

def connect():
  driver = gl.get('driver', None)
  if not driver: return False
  try:
    driver.get('https://ais.ntou.edu.tw/Default.aspx')
    driver.implicitly_wait(4)
    driver.find_element_by_name('M_PW').send_keys(gl.get('password'))
    driver.find_element_by_id('M_PORTAL_LOGIN_ACNT').send_keys(gl.get('username'))
    driver.find_element_by_id('LGOIN_BTN').click()
    driver.switch_to.frame('menuFrame')
    driver.find_element_by_id('Menu_TreeViewt1').click()
    driver.find_element_by_id('Menu_TreeViewt30').click()
    driver.find_element_by_id('Menu_TreeViewt40').click()
    driver.switch_to.default_content()
    driver.switch_to.frame('mainFrame')
    return True
  except Exception as e:
    if gl.get('errorMessage', False):
      print('Connect Error')
      print(e)
      print(time.ctime())
    time.sleep(2)
    return False

def auto_snap(courseId):
  driver = gl.get('driver')
  i = gl.get('times', 0)
  timesCount = gl.get('timesCount', 10)
  if i == 0: print('begin')
  print(time.ctime())
  if not get_course(driver, courseId): return False
  time.sleep(0.8)
  timeNow = time.time()
  while True:
    time.sleep(0.2)
    if time.time() - timeNow > 30:
      print('Timeout, auto connecting')
      break
    if i % timesCount == 0: print(i)
    if not choose_course(driver): continue
    time.sleep(0.1)
    if not accept_alert(driver): continue
    i += 1
  gl.set('i', i)