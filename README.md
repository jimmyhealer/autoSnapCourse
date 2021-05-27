# AutoSnapCourse
## 自動搶課系統
## 教學

1. 首先您要有Windows。因為這是windows才能用，而且wsl也不行喔。
2. 還要有Chrome 並更新到最新，然後安裝 selenium。
3. 在 main.py 輸入您的帳號密碼
```python=
  driver.find_element_by_name('M_PW').send_keys('這裡輸入您的密碼')
  driver.find_element_by_id('M_PORTAL_LOGIN_ACNT').send_keys('這裡輸入您的學號')
```
4. 然後 點擊他 或 ```python3 main.py```
5. 跑一下就到了，就醬，沒開放我也不知道怎麼做，我應該在一階的時候做QQ
