from selenium import webdriver

driver = webdriver.Firefox() # executable_path=r'C:\geckodriver'
# driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
driver.get('https://stepik.org/lesson/25969/step/8')

driver.quit()



# from selenium import webdriver
#
# with webdriver.Firefox() as driver:
#     driver.get("http://google.com")
#     print("Page Title is : %s" %driver.title)
#     driver.quit()

# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
#
# options = Options()
# options.binary_location = r'C:\geckodriver'
# driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe', options=options)
# driver.get("https://stepik.org/lesson/25969/step/8")
# driver.quit()