from selenium import webdriver # Import for webdriver 
from selenium.webdriver.common.by import By # Import for webriver helper that locates specific elements 

chrome_options = webdriver.ChromeOptions() # adds specific options for chrome windows on open 
chrome_options.add_experimental_option("detach", True) # adds an customized option 

driver = webdriver.Chrome(options=chrome_options) # creates driver with customized options
driver.get("https://www.python.org/") # Goes to a specific website

pythonUpcomingEvents = {}

for i in range(1,5,1):
    date_tag = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[{i}]/time').text
    title_tag = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text

    pythonUpcomingEvents[i] = [date_tag , title_tag]

print(pythonUpcomingEvents)

driver.quit()


