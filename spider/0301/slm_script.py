from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
for i in range(0,5000):
    sc = 'window.scrollTo(0,'+str(i)+')'
    browser.execute_script(sc)
browser.execute_script('alert("完成")')
