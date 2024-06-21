import time
import requests
import selenium
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains

def suggestionCalendar(userId, hId, driver):

    today = datetime.now()
    fromDate = today.strftime("%Y-%m-%d")
    toDate = (today + timedelta(days=5)).strftime("%Y-%m-%d")

    try:
        rateSuggestionsComponents = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flex.items-center.w-full.gap-3.ml-3[href="/rate_suggestions"]'))
        )
        rateSuggestionsComponents.click()
        print('Rate Suggestions page opened successfully')
    except TimeoutException:
        print("Rate Suggestions page not found")
        return

    time.sleep(10)

    try:
        suggestedRate = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@title='Suggested Rate' and contains(@class, 'text-white') and contains(@class, 'flex') and contains(@class, 'text-xs') and contains(@class, 'text-start') and contains(@class, 'w-full')]"))
        )
        suggestedRates = [element.text for element in suggestedRate]
        print('Suggested Rates:', suggestedRates)
    except TimeoutException:
        print("Suggested Rate elements not found")
        suggestedRates = []

    rateSuggestionCalendar = f'https://rxserver.retvenslabs.com/api/dashboard/rateSuggestionCalendar?userId={userId}&hId={hId}&startDate={fromDate}&endDate={toDate}&type=suggestion'
    response = requests.get(rateSuggestionCalendar)

    if response.status_code == 200:
        result = response.json()
        data_slot = result.get('data', {})
        
        if data_slot:
            print("Suggestion Calendar Data is Available")
        else:
            print("Suggestion Calendar Data is not Available")
    else:
        print(f"Request failed with status code: {response.status_code}")

    try:
        rateAnalysis = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.p-2.bg-blue-500'))
        )
        rateAnalysis.click()
        print("Rate Analysis opened Successfully")
    except TimeoutException:
        print("Rate Analysis Page not found")
        return

    time.sleep(10)

    try:
        rateAnalysisrateSuggestedPrice = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[div[@class='text-[14px]' and text()='Rate Suggestion']]//div[@class='text-[#29CC39] text-[17px] font-semibold']"))
        )
        rate_suggestion_value = rateAnalysisrateSuggestedPrice.text
        print('Rate Suggestion:', rate_suggestion_value)
    except TimeoutException:
        print("Rate Suggestion element not found")
        rate_suggestion_value = ""

    try:
        rate_suggestion_elementSecond = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.flex.w-full.gap-2.whitespace-nowrap.justify-end.items-center.font-medium.group-hover\\:bg-\\[\\#CCD6E5\\].group-hover\\:px-2 p"))
        )
        rate_suggestion_value_Second = rate_suggestion_elementSecond.text
        print('Rate Suggestion Second:', rate_suggestion_value_Second)
    except TimeoutException:
        print("Rate Suggestion Second element not found")
        rate_suggestion_value_Second = ""

    all_suggestions_match = True

    for suggested_rate in suggestedRates:
        if suggested_rate != rate_suggestion_value or suggested_rate != rate_suggestion_value_Second:
            all_suggestions_match = False
            break

    if all_suggestions_match:
        print("All suggested rates are the same")
    else:
        print("Suggested rates do not match")
        print(f"Suggested Rates: {suggestedRates}")
        print(f"Rate Suggestion: {rate_suggestion_value}")
        print(f"Rate Suggestion Second: {rate_suggestion_value_Second}")

    rate_suggestion_on_day_url = f'https://rxserver.retvenslabs.com/api/dashboard/rateSuggestionOnDay?hId={hId}&userId={userId}&date={fromDate}&type=suggestion'
    response_1 = requests.get(rate_suggestion_on_day_url)

    if response_1.status_code == 200:
        result_1 = response_1.json()
        data_slot_1 = result_1.get('data', [])
        
        if data_slot_1:
            print("Rate Suggestion On Day Data is Available")
        else:
            print("Rate Suggestion On Day Data is not Available")
    else:
        print(f"Request failed with status code: {response_1.status_code}")

    toDate_1 = (today + timedelta(days=1)).strftime("%Y-%m-%d")

    actual_and_suggested_rates_url = f'https://rxserver.retvenslabs.com/api/dashboard/getActualAndSuggestedRates?userId={userId}&startDate={fromDate}&endDate={toDate_1}&hId={hId}'
    response_2 = requests.get(actual_and_suggested_rates_url)

    if response_2.status_code == 200:
        result_2 = response_2.json()
        data_slot_2 = result_2.get('data', [])
        
        if data_slot_2:
            print("Get Actual And Suggested Rates Data is Available")
        else:
            print("Get Actual And Suggested Rates Data is not Available")
    else:
        print(f"Request failed with status code: {response_2.status_code}")

    suggested_rate_vs_competition_url = f'https://rxserver.retvenslabs.com/api/dashboard/suggestedRateVsCompetition?hId={hId}&userId={userId}&date={fromDate}'
    response_3 = requests.get(suggested_rate_vs_competition_url)

    if response_3.status_code == 200:
        result_3 = response_3.json()
        data_slot_3 = result_3.get('data', {})
        
        if data_slot_3:
            print("Suggested Rate Vs Competition Data is Available")
        else:
            print("Suggested Rate Vs Competition Data is not Available")
    else:
        print(f"Request failed with status code: {response_3.status_code}")
    
    try:
        overrideRates = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'px-3') and contains(@class, 'py-1') and contains(@class, 'rounded-lg') and contains(@class, 'text-white') and contains(@class, 'bg-[#3361ff]') and contains(@class, 'cursor-pointer') and contains(@class, 'text-center') and text()='Override Rates']"))
        )
        overrideRates.click()
        print("Override Rates Page Open Successfully")

    except TimeoutException:
        print("Override Rates Page Open not found")
    
    time.sleep(10)
