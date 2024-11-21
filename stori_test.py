import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print('TestCase 1: Go to open web page')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print("\tStatus [",datetime.datetime.now().time(),"]: Passed")

#______________________________________________________________________________________Suggession Class Example

try:
    print('TestCase 2: Select Mexico')
    driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("Me")
    time.sleep(2)
    driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")[5].click()
    print("\tStatus [",datetime.datetime.now().time(),"]: Passed")
except:
    print("\tStatus [",datetime.datetime.now().time(),"]: Fail")

#______________________________________________________________________________________Dropdown Example

try:
    print('TestCase 3.1: Select Option2')
    x = driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
    drop=Select(x)
    drop.select_by_visible_text("Option2")
    print("\tStatus [",datetime.datetime.now().time(),"]: Passed")
except:
    print("\tStatus [",datetime.datetime.now().time(),"]: Fail")

time.sleep(2)

#______________________________________________________________________________________Dropdown Example

try:
    print('TestCase 3.2: Select Option3')
    x = driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
    drop=Select(x)
    drop.select_by_visible_text("Option3")
    print("\tStatus [",datetime.datetime.now().time(),"]: Passed")
except:
    print("\tStatus [",datetime.datetime.now().time(),"]: Fail")

time.sleep(2)

#______________________________________________________________________________________Switch Window Example (No lo acabé)

try:
    print('TestCase 4: Switch Window Example')
    open_window = driver.find_element(By.ID, "openwindow")
    open_window.click()
    time.sleep(5)
    original_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
            time.sleep(3)
    try:
        print("\tStatus [",datetime.datetime.now().time(),"]:Passed")
    except:
        print("\tStatus [",datetime.datetime.now().time(),"]: Fail")
    driver.close()
    driver.switch_to.window(original_window)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    time.sleep(2)

#______________________________________________________________________________________Switch Tab Example (No lo acabé)

try:
    print('TestCase 5: Switch Tab Example')
    open_tab_button = driver.find_element(By.ID, "opentab")
    open_tab_button.click()
    time.sleep(5)
    original1_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original1_window:
            driver.switch_to.window(window_handle)
            break
            time.sleep(2)
    try:
        print("\tStatus [",datetime.datetime.now().time(),"]:Passed")
    except:
        print("\tStatus [",datetime.datetime.now().time(),"]: Fail")
    driver.close()
    driver.switch_to.window(original1_window)
except Exception as e:
    print("Status[",datetime.datetime.now().time(),"]: Fail")
finally:
    time.sleep(2)


    

#______________________________________________________________________________________Switch To Alert Example

try:
    print('TestCase 6: Switch To Alert Example')
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Stori Card")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
    time.sleep(2)
    response = driver.switch_to.alert 
    print("\t\t The alert message is: ",response.text)
    response.accept()
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Stori Card")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
    time.sleep(2
        )
    response = driver.switch_to.alert
    if response.text == "Hello Stori Card, Are you sure you want to confirm?":
        print("\t\t The confirm message is: ",response.text)
        print("\tStatus [",datetime.datetime.now().time(),"]: Passed")
        response.accept()
    else:
        print("\tStatus [",datetime.datetime.now().time(),"]: Fail, the message is: ", response.text)
        response.dismiss()
except Exception as error:
    print("\tStatus [",datetime.datetime.now().time(),"]: Fail", error)
    time.sleep(20)

#______________________________________________________________________________________Web Table Example (Conteo, No lo acabé)

print('TestCase 7.1: WTE Counter $25')
table = driver.find_element(By.XPATH, "//table[@id='product']/tbody")
rows = table.find_elements(By.CSS_SELECTOR, "tr")
count_25 = 0
for row in rows:
    columns = row.find_elements(By.CSS_SELECTOR, "td")
    if len(columns) > 3:
        price = columns[2].text
        if price == "25":
            count_25 += 1
print(f"Número de cursos con precio 25: {count_25}")
#No me esta realizando el conteo :/

#______________________________________________________________________________________Web Table Example

try:
    print('TestCase 7.2: WTE Find in table')
    for row in driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(5) > div:nth-child(1) > fieldset:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr"):
        if "Price" not in row.text:
            if "25" in row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text:                
                print("\t\tCourse name is :", row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text)
        
    print("\tStatus [",datetime.datetime.now().time(),"]: Passed")
except Exception as error:
    print("\tStatus [",datetime.datetime.now().time(),"]: Fail")

#______________________________________________________________________________________Web Table Fixed header

try:
    print('TestCase 8: Find in table fixed')
    for row in driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(5) > div:nth-child(2) > fieldset:nth-child(2) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr"):
        if "Engineer" in row.text:
            print("\t\tEngineer :", row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text)
        
    print("\tStatus [",datetime.datetime.now().time(),"]: Passed")
        
except Exception as error:
    print("\tStatus [",datetime.datetime.now().time(),"]: Fail by except ", error)

#______________________________________________________________________________________iFrame example

try:
    print('TestCase 9: IFrame get text')
    driver.switch_to.frame('courses-iframe')
    record = 1
    strings = ""
    for row in driver.find_elements(By.XPATH, "//ul[@class='list-style-two']//li"):
        if record % 2 != 0:
            strings = strings+" "+row.text+"\n\t\t" 
        if "His mentorship program is most after in the software testing community with long waiting period." in row.text:
            print("\tStatus [",datetime.datetime.now().time(),"]: Passed: ", row.text)
except Exception as error:
    print("\tStatus [",datetime.datetime.now().time(),"]: Fail ")