import time
from selenium import webdriver
from selenium.webdriver.common.by import By

version = "125.0.6422.141"

chrome_option = webdriver.ChromeOptions()
chrome_option.binary_location = "C:/ChromeDriver/chrome-win64/chrome.exe"
chrome_driver_path = "C:/ChromeDriver/chromedriver-win64/chromedriver.exe"

service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_option, service=service_options)

driver.get("https://fireant.vn/trang-chu")

time.sleep(5)

# Switch to the pop-up window
driver.switch_to.window(driver.window_handles[1])
# Close the pop-up window
driver.close()
# Switch back to the main window
driver.switch_to.window(driver.window_handles[0])


search_bar = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/header/nav/div[2]/div[2]/div/div/div/div/div/div[1]/div/input')
search_bar.send_keys("acb")
time.sleep(5)

search_result = driver.find_element(By.XPATH, '//div[@class="css-1pahdxg"]')
search_result.click()

so_lenh = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/button[2]')
so_lenh.click()
time.sleep(2)

