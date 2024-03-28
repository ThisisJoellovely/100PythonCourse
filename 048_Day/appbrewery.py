from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

First_Name = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
Last_Name = driver.find_element(By.XPATH, value="/html/body/form/input[2]")
Email_Address = driver.find_element(By.XPATH, value="/html/body/form/input[3]")
Button = driver.find_element(By.XPATH, "/html/body/form/button")

First_Name.send_keys("Joel")
Last_Name.send_keys("Lovely")
Email_Address.send_keys("Joellovely0717@gmail.com")
Button.click()

driver.close()
