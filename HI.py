import time
import requests, json
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def hotelIntelligence(userId, hId, driver):

    try:
        hotel_intelligence_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/hotel_intelligence"]')))
        hotel_intelligence_link.click()
        print('Hotel Intelligence Page Opened Successfully')
    except TimeoutException:
        print("Hotel Intelligence Page not Found")

    time.sleep(10)

    sourcesSelectors = f'https://rxserver.retvenslabs.com/api/utils/getSourcesSelectors?hId={hId}'

    response = requests.request("GET", sourcesSelectors)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Sources Selectors Data is Available")
        else:
            print("Sources Selectors Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    sourceOverview = f'https://rxserver.retvenslabs.com/api/dashboard/getSourceOverview?userId={userId}&hId=20671&startDate=2023-06-01&endDate=2023-06-30&startDate1=2024-06-01&endDate1=2024-06-30&source='

    response_1 = requests.request("GET", sourceOverview)

    if response.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', {})
        
        if data_slot_1:
            print("Source Overview Data is Available")
        else:
            print("Source Overview Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    todaysOverview = f'https://rxserver.retvenslabs.com/api/dashboard/todaysOverview?userId={userId}&hId={hId}'

    response_2 = requests.request("GET", todaysOverview)

    if response.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', {})
        
        if data_slot_2:
            print("Todays Overview Data is Available")
        else:
            print("Todays Overview Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    Overview = f'https://rxserver.retvenslabs.com/api/dashboard/overview?hId={hId}&userId={userId}&chartData=revenue&startDate=2023-06-01&endDate=2023-06-30&startDate1=2024-06-01&endDate1=2024-06-30&source='

    response_3 = requests.request("GET", Overview)

    if response.status_code == 200:
        result_3 = response_3.json()
        data_slot_3 = result_3.get('data', {})
        
        if data_slot_3:
            print("Overview Data is Available")
        else:
            print("Overview Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")