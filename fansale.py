import os
import requests
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_discord_message(webhook_url, message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        raise ValueError(f"Request to Discord returned an error: {response.status_code}, {response.text}")

url = "https://www.fansale.fi/fansale/tickets/hard-amp-heavy/rammstein/188180/15753054"

# Replace with your Discord webhook URL & user ID
discord_webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
discord_user_id = "YOUR_DISCORD_USER_ID"

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

# Fetch the webpage
driver.get(url)

# Check if the specified xpath exists with the given value
try:
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="pageContent"]/main/section[6]/div/div/div/div[2]/div[3]/div[@class="js-AvailabilityInfo-TextOfferList AvailabilityInfo-Text AvailabilityInfo-TextOfferList AvailabilityInfo-TextOfferList-isVisible"]'),
            "Valitettavasti sopivia tarjouksia ei löytynyt."
        )
    )
    print("No tickets")
except:
    print("Found tickets")
    # If the xpath does not exist or the value is different, process the required elements
    elements = driver.find_elements(By.XPATH, '//*[@id="pageContent"]/main/section[6]/div/div/div/div[2]/div[3]/div[3]/div[@data-fairdeal="true"]')

    # Convert elements to a list of text values
    new_data = [element.find_element(By.XPATH, './/div[2]/div[1]/span[1]').text for element in elements]

    # Read the existing data from the file
    file_path = str(Path(__file__).parent) + "/data.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            old_data = [line.strip() for line in file.readlines()]
    else:
        old_data = []

    # Compare the new_data and old_data lists
    if new_data != old_data:
        # If the new data does not match the old data, overwrite the file
        with open(file_path, "w") as file:
            for data in new_data:
                file.write(data + "\n")
        
        # Send a Discord message with the new data
        message = f"<@{discord_user_id}> {new_data}\n\nhttps://www.fansale.fi/fansale/tickets/hard-amp-heavy/rammstein/188180/15753054"
        send_discord_message(discord_webhook_url, message)

# Close the WebDriver
driver.quit()
