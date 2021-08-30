import driver_gen
import exceptions
from selenium.webdriver.common.by import By

def java(ign):
    driver = driver_gen.new()

    with driver:
        driver.get(f"https://appeals.cubecraft.net/find_appeals/{ign}/JAVA")

    try:
        appeal_link = driver.find_element(By.CLASS_NAME, "btn").get_attribute("href")
    except:
        appeal_link = None

    if appeal_link is not None:
        return appeal_link

    else:
        if "has never joined the server" in driver.find_element(By.CLASS_NAME, "alert").text:
            raise exceptions.PlayerNeverJoined(ign)

        raise exceptions.AppealUrlUnavailable(ign)

def bedrock(ign):
    driver = driver_gen.new()

    with driver:
        driver.get(f"https://appeals.cubecraft.net/find_appeals/{ign}/MCO")

    try:
        appeal_link = driver.find_element(By.CLASS_NAME, "btn").get_attribute("href")
    except:
        appeal_link = None

    if appeal_link is not None:
        driver.quit()
        return appeal_link

    else:
        if "has never joined the server" in driver.find_element(By.CLASS_NAME, "alert").text:
            driver.quit()
            raise exceptions.PlayerNeverJoined(ign)

        driver.quit()
        raise exceptions.AppealUrlUnavailable(ign)