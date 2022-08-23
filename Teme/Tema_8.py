from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


'''BY ID'''

# driver.get('https://www.phptravels.net/')
# email_address_input = driver.find_element(By.ID, 'exampleInputEmail1')
# email_address_input.send_keys('lzr.giulia@gmail.com')
# sleep(5)
# driver.quit()

# driver.get('http://automationpractice.com/index.php')
# search_input = driver.find_element(By.ID, 'search_query_top')
# search_input.send_keys('t-shirts')
# click_on_search = driver.find_element(By.CLASS_NAME,'button-search')
# click_on_search.click()
# newsletter_input = driver.find_element(By.NAME, 'newsletter-input')
# newsletter_input.send_keys('lzr.giulia@gmail.com')
# sleep(5)
# driver.quit()

# driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
# date_input = driver.find_element(By.ID, 'datepicker')
# date_input.send_keys('20/08/2022')
# sleep(5)
# driver.quit()


'''BY LINK_TEXT'''

# driver.get('https://formy-project.herokuapp.com/')
# link1 = driver.find_element(By.LINK_TEXT, 'Buttons')
# link1.click()
# sleep(5)
# driver.quit()

# driver.get('https://the-internet.herokuapp.com/')
# link3 = driver.find_element(By.LINK_TEXT, 'Dynamic Controls')
# link3.click()
# sleep(5)
# driver.quit()


# driver.get('http://automationpractice.com/index.php')
# link2 = driver.find_element(By.LINK_TEXT, 'Sign in')
# link2.click()
# sleep(5)
# driver.quit()


'''BY NAME'''

# driver.get('http://automationpractice.com/index.php')
# search_input = driver.find_element(By.NAME, 'search_query')
# search_input.send_keys('dresses')
# sleep(5)
# driver.quit()

# driver.get('https://the-internet.herokuapp.com/forgot_password')
# email_input = driver.find_element(By.NAME, 'email')
# email_input.send_keys('lzr.giulia@gmail.com')
# sleep(5)
# driver.quit()

# driver.get('http://automationpractice.com/index.php?controller=contact')
# message_input = driver.find_element(By.NAME, 'message')
# message_input.send_keys('Everything works just fine! :)')
# sleep(5)
# driver.quit()


'''BY TAG_NAME'''

# driver.get('http://automationpractice.com/index.php?controller=contact')
# list_inputs = driver.find_elements(By.TAG_NAME, "input")
# list_inputs[3].send_keys('dresses')
# sleep(5)
# driver.quit()

# driver.get('https://the-internet.herokuapp.com/login')
# list_inputs = driver.find_elements(By.TAG_NAME, "input")
# list_inputs[0].send_keys('lzr.giulia@gmail.com')
# list_inputs[1].send_keys('123456789')
# click_on_login = driver.find_element(By.CLASS_NAME,'fa-sign-in')
# click_on_login.click()
# sleep(5)
# driver.quit()

# driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
# list_inputs = driver.find_elements(By.TAG_NAME, "input")
# list_inputs[0].send_keys('Giulia')
# list_inputs[1].send_keys('Lazar')
# sleep(5)
# driver.quit()

# driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
# input = driver.find_element(By.TAG_NAME, 'input')
# input.send_keys('Giulia')
# sleep(5)
# driver.quit()


'''BY CLASS_NAME'''

# driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
# button_click = driver.find_element(By.CLASS_NAME, 'btn-info')
# button_click.click()
# sleep(5)
# driver.quit()

# driver.get('https://formy-project.herokuapp.com/form')
# button_click = driver.find_element(By.CLASS_NAME, 'btn-primary')
# button_click.click()
# sleep(5)
# driver.quit()

# driver.get('http://automationpractice.com/index.php')
# search_input = driver.find_element(By.ID, 'search_query_top')
# search_input.send_keys('alabala portocala')
# click_on_search = driver.find_element(By.CLASS_NAME,'button-search')
# click_on_search.click()
# sleep(5)
# driver.quit()


'''BY PARTIAL_LINK_TEXT'''

# driver.get('https://formy-project.herokuapp.com/')
# link1 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Butto')
# link1.click()
# sleep(5)
# driver.quit()

# driver.get('http://automationpractice.com/index.php')
# link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign i')
# link2.click()
# sleep(5)
# driver.quit()

# driver.get('https://the-internet.herokuapp.com/')
# link3 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Dynamic Contr')
# link3.click()
# sleep(5)
# driver.quit()

# driver.get('https://the-internet.herokuapp.com/')
# link3 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Dynamic C')
# link3.click()
# sleep(5)
# driver.quit()

