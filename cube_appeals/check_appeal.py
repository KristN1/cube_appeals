from cube_appeals import driver_gen, exceptions
from selenium.webdriver.common.by import By

def java(ign):
    driver = driver_gen.new()

    with driver:
        driver.get(f"https://appeals.cubecraft.net/find_appeals/{ign}/JAVA")

    try:
        if "Current infractions" in driver.find_element(By.CLASS_NAME, "card-header").text:
            driver.quit()
            return True

    except:
        driver.quit()
        return java(ign)

    else:
        if "has never joined the server" in driver.find_element(By.CLASS_NAME, "alert").text:
            driver.quit()
            raise exceptions.PlayerNeverJoined(ign)

        driver.quit()
        return False

def bedrock(ign):
    driver = driver_gen.new()

    with driver:
        driver.get(f"https://appeals.cubecraft.net/find_appeals/{ign}/MCO")

    if "Current infractions" in driver.find_element(By.CLASS_NAME, "card-header").text:
        driver.quit()
        return True
    else:
        if "has never joined the server" in driver.find_element(By.CLASS_NAME, "alert").text:
            driver.quit()
            raise exceptions.PlayerNeverJoined(ign)

        driver.quit()
        return False