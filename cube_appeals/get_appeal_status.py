from cube_appeals import driver_gen, exceptions
from selenium.webdriver.common.by import By

def java(ign):
    driver = driver_gen.new()

    with driver:
        driver.get(f"https://appeals.cubecraft.net/find_appeals/{ign}/JAVA")
    
    try:
        card_text = driver.find_element(By.CLASS_NAME, "col-sm-8").text
    except:
        if "has never joined the server" in driver.find_element(By.CLASS_NAME, "alert").text:
            driver.quit()
            raise exceptions.PlayerNeverJoined(ign)
        else:
            driver.quit()
            raise exceptions.PlayerNotPunished(ign)

    driver.quit()
    return determine_status(card_text)
    
def bedrock(ign):
    driver = driver_gen.new()

    with driver:
        driver.get(f"https://appeals.cubecraft.net/find_appeals/{ign}/MCO")

    try:
        card_text = driver.find_element(By.CLASS_NAME, "col-sm-8").text
    except:
        if "has never joined the server" in driver.find_element(By.CLASS_NAME, "alert").text:
            driver.quit()
            raise exceptions.PlayerNeverJoined(ign)
        else:
            driver.quit()
            raise exceptions.PlayerNotPunished(ign)

    driver.quit()
    return determine_status(card_text)

def determine_status(card_text):
    if "Appeal Denied" in card_text:
        return "Appeal Denied"
    elif "Appeal" in card_text:
        return "Appeal Available"