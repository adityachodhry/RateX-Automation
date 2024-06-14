import time
import requests, json
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def dashboard(username, password, userId, hId, driver):

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

    days_7 = f'https://rxserver.retvenslabs.com/api/dashboard/next7DaysPricing?hId={hId}&userId={userId}'

    response = requests.request("GET", days_7)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("7 Days Data is Available")
        else:
            print("7 Days Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    performaceMatrix = f'https://rxserver.retvenslabs.com/api/dashboard/performaceMatrix?hId={hId}&userId={userId}&timePeriod=past30Days&chartData=revenue'

    response_1 = requests.request("GET", performaceMatrix)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("performace Matrix Data is Available")
        else:
            print("performace Matrix Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    ForecastedData = f'https://rxserver.retvenslabs.com/api/dashboard/getForecastedData?userId={userId}&hId={hId}&rangeType=7D'

    response_2 = requests.request("GET", ForecastedData)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("Forecasted Data is Available")
        else:
            print("Forecasted Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    SentimentAnalysis = f'https://rxserver.retvenslabs.com/api/dashboard/getSentimentAnalysisData?userId={userId}&hId={hId}'

    response_3 = requests.request("GET", SentimentAnalysis)

    if response.status_code == 200:
        result_3 = response_3.json()
        data_slot_3 = result_3.get('data', {})
        
        if data_slot_3:
            print("Sentiment Analysis Data is Available")
        else:
            print("Sentiment Analysis Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    Notifications = f'https://rxserver.retvenslabs.com/api/notifications/getNotifications?hId={hId}'

    response_4 = requests.request("GET", Notifications)

    if response.status_code == 200:
        result_4 = response_4.json()
        data_slot_4 = result_4.get('data', {})
        
        if data_slot_4:
            print("Notifications Data is Available")
        else:
            print("Notifications Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    

    takeActions = f'https://rxserver.retvenslabs.com/api/dashboard/getActionsToTake?hId={hId}&userId={userId}'

    response_5 = requests.request("GET", takeActions)

    if response.status_code == 200:
        result_5 = response_5.json()
        data_slot_5 = result_5.get('data', {})
        
        if data_slot_5:
            print("Take Actions Data is Available")
        else:
            print("Take Actions Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    Reputation = f'https://rxserver.retvenslabs.com/api/dashboard/getReputationWidgetData?hId={hId}&userId={userId}'

    response_6 = requests.request("GET", Reputation)

    if response.status_code == 200:
        result_6 = response_6.json()
        data_slot_6 = result_6.get('data', {})
        
        if data_slot_6:
            print("Reputation Data is Available")
        else:
            print("Reputation Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    Cancellation = f'https://rxserver.retvenslabs.com/api/dashboard/getCancellationWidgetData?userId={userId}&hId={hId}'

    response_7 = requests.request("GET", Cancellation)

    if response.status_code == 200:
        result_7 = response_7.json()
        data_slot_7 = result_7.get('data', {})
        
        if data_slot_7:
            print("Cancellation Data is Available")
        else:
            print("Cancellation Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    
