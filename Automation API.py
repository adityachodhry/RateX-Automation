from flask import Flask, request, jsonify
import threading
from seleniumwire import webdriver
from Dashboard import dashboard
from rateSuggestions import suggestionCalendar
from HI import hotelIntelligence
from rates_Inventory import Inventory
from compsetOverview import compsetInventory
from reservations import reservations

app = Flask(__name__)

def run_all_functions(username, password, userId, hId, chId):
    driver = webdriver.Chrome()

    try:
        dashboard(username, password, userId, hId, driver)
        suggestionCalendar(userId, hId, driver)
        hotelIntelligence(userId, hId, driver)
        Inventory(userId, hId, driver)
        compsetInventory(userId, hId, chId, driver)
        reservations(userId, hId, chId, driver)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

@app.route('/rateX/automation', methods=['POST'])
def run_functions():
    data = request.json

    username = data.get('username')
    password = data.get('password')
    hId = data.get('hId')
    chId = data.get('chId')
    userId = data.get('userId')

    if not all([username, password, hId, chId, userId]):
        return jsonify({"error": "Missing parameters"}), 400

    thread = threading.Thread(target=run_all_functions, args=(username, password, userId, hId, chId))
    thread.start()

    return jsonify({"message": "Functions executed successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
