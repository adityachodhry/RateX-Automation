import time
import requests, json
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

username = 'support@retvenstechnologies.com'
password = 'Retvens@9feb'

driver = webdriver.Chrome()

login_url = 'https://ratex.retvenslabs.com/login'

driver.get(login_url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))

driver.find_element(By.NAME, 'email').send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)

driver.find_element(By.XPATH, '//button[text()="Log-in"]').click()

WebDriverWait(driver, 10).until(EC.url_changes(login_url))

def take_screenshot_and_save_as(filename):
    driver.save_screenshot(filename + '.png')
    print(f"Screenshot saved as {filename}.png")

try:
    close_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.absolute.right-2.top-4.bg-red-50.text-red-600.text-sm.py-1.px-2.rounded-lg.hover\\:bg-red-500.hover\\:text-white.cursor-pointer'))
    )
    close_button.click()
    print("Closed popup successfully")
except TimeoutException:
    print("No popup found")

if "Invalid username or password" in driver.page_source:
    print("Login Unsuccessful")
    driver.quit()
else:
    print("Login Successful")

time.sleep(10)

try:
    sidebar_toggle_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.sidebar_toggle'))
    )
    sidebar_toggle_button.click()
    print('Sidebar opened successfully')
    take_screenshot_and_save_as('sidebar')
except TimeoutException:
    print("Sidebar toggle button not found")

time.sleep(2)

try:
    rate_suggestions_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/rate_suggestions"]'))
    )
    rate_suggestions_link.click()
    print('Rate Suggestions Opened Successfully')
    take_screenshot_and_save_as('rate_suggestions')
except TimeoutException:
    print("Rate Suggestions link not found")

time.sleep(10)

try:
    hotel_intelligence_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/hotel_intelligence"]'))
    )
    hotel_intelligence_link.click()
    print('Hotel Intelligence Opened Successfully')
    take_screenshot_and_save_as('hotel_intelligence')
except TimeoutException:
    print("Hotel Intelligence link not found")

time.sleep(10)

try:
    rates_inventory_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/rates_&_inventory"]'))
    )
    rates_inventory_link.click()
    print('Rates & Inventory Opened Successfully')
    take_screenshot_and_save_as('rates_inventory')
except TimeoutException:
    print("Rates & Inventory link not found")

time.sleep(10)

try:
    compset_overview_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/compset_overview"]'))
    )
    compset_overview_link.click()
    print('Compset Overview Opened Successfully')
    take_screenshot_and_save_as('compset_overview')
except TimeoutException:
    print("Compset Overview link not found")

time.sleep(10)

try:
    reservations_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/reservations"]'))
    )
    reservations_link.click()
    print('Reservations Opened Successfully')
    take_screenshot_and_save_as('reservations')
except TimeoutException:
    print("Reservations link not found")

time.sleep(10)

try:
    custom_report = 'https://ratex.retvenslabs.com/Report/Custom'
    driver.get(custom_report)
    print('Custom Report Open Sucessfully')
    take_screenshot_and_save_as('custom_report')
except TimeoutException:
    print("Custom Report not Open")

time.sleep(10)

try:
    ratePulse_TemplateReport = 'https://ratex.retvenslabs.com/Report/TemplateReport'
    driver.get(ratePulse_TemplateReport)
    print('Template Report Open Sucessfully')
    take_screenshot_and_save_as('TemplateReport')
except TimeoutException:
    print("Template Report not Open")

time.sleep(10)

try:
    ratePulse_dashboard_url = 'https://ratex.retvenslabs.com/rate-pulse/dashboard'
    driver.get(ratePulse_dashboard_url)
    print('Rate Pulse Dashboard Open Sucessfully')
    take_screenshot_and_save_as('ratePulseDasboard')
except TimeoutException:
    print("Rate Pulse Dashboard not Open")

time.sleep(10)

try:
    ratePulse_rate_monitor = 'https://ratex.retvenslabs.com/rate-pulse/rate_monitor'
    driver.get(ratePulse_rate_monitor)
    print('Rate Monitor Open Sucessfully')
    take_screenshot_and_save_as('ratemonitor')
except TimeoutException:
    print('Rate Monitor not Open')

time.sleep(10)

try:
    ratePulse_rate_fluctuation = 'https://ratex.retvenslabs.com/rate-pulse/rate_fluctuation'
    driver.get(ratePulse_rate_fluctuation)
    print('Rate Fluctuation Open Sucessfully')
    take_screenshot_and_save_as('rate_fluctuation')
except TimeoutException:
    print('Rate Fluctuation not Open')

time.sleep(10)

try:
    ratePulse_reputation = 'https://ratex.retvenslabs.com/rate-pulse/reputation'
    driver.get(ratePulse_reputation)
    print('Rate Reputation Open Sucessfully')
    take_screenshot_and_save_as('Reputation')
except TimeoutException:
    print('Rate Reputation not Open')

time.sleep(10)

try:
    ratePulse_visibility = 'https://ratex.retvenslabs.com/rate-pulse/visibility'
    driver.get(ratePulse_visibility)
    print('Rate Visibility Open Sucessfully')
    take_screenshot_and_save_as('Reputation')
except TimeoutException:
    print('Rate Visibility not Open')

time.sleep(10)

driver.quit()
