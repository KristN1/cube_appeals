import undetected_chromedriver.v2 as uc

def new():
    options = uc.ChromeOptions()
    #options.headless=True
    driver = uc.Chrome(options=options)

    return driver