#
# #initializam un browser
#
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.common.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# # s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# # chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome.get('www.google.com')


from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('https://formy-project.herokuapp.com/form')
first_name_input = chrome.find_element(By.ID, "first-name")
# dupa id,dupa class name, dupa tagname,dupa name, dupa linktext, dupa partial text, dupa css selector, dupa xpath
first_name_input.send_keys("petruta")
first_name_input.clear()
first_name_input.send_keys("ioana")
last_name_input = chrome.find_element(By.ID, "last-name")
last_name_input.send_keys("morar")
sleep(5)
chrome.quit()

'''
Pe o pagina avem mai multe elemente:
- cele care au un spatiu de completat, sunt input-uri
- cele care au cerculete (adica sa alegi o varianta din mai multe), sunt radio button
- cele pe care le dam check, sunt check box-uri
- cele pe care dai click si ti se afiseaza o lista din care sa alegi, sunt drop down-uri
- cele de tip calendar
- cele pe care dai ckick pe ele (ex: Submit, Continue, etc.) sunt ori butoane ori link-uri

Ca sa aflam selectorul unui element > dam click pe patrat+sageata, identificam ce element vrem sa aflam

- tip de element (primul scris dupa semnul <; ex: input)
- atribut (ex: type, class, id, placeholder)

cautam dupa selectori, XPATH sau atribute

ca sa vedem daca un atribut este unic:
- dam ctrl+f
- verificam cu # doar pt id (ex: #first-name)
- verificam cu . doar la clasa (ex: .btn.btn-lg.btn-success), adica punem . in fata si in locul spatiilor
- verificam genral cu: [id = ...], [class = ...] sau class = '...'
ex: [id = first-name]; [class = form-control]; class = 'form-control'
'''