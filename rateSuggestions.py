import time
import requests, json
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def suggestionCalendar(userId, hId, driver):

    try:
        rate_suggestions_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/rate_suggestions"]'))
        )
        rate_suggestions_link.click()
        print('Rate Suggestions page Opened Successfully')
    except TimeoutException:
        print("Rate Suggestions page not found")

    time.sleep(10)

    suggestionCalendar = f'https://rxserver.retvenslabs.com/api/dashboard/rateSuggestionCalendar?userId={userId}&hId={hId}&startDate=2024-06-12&type=suggestion'

    response = requests.request("GET", suggestionCalendar)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Suggestion Calendar Data is Available")
        else:
            print("Suggestion Calendar Data is not available")
    else:
        print(f"Request failed with status code: {response.status_code}")

