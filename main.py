from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
search_term = "Donald Trump"
boosted_site = "The Propaganda Model – Media Studies 101"

iterations = 0
while True:
    driver.get("https://www.google.com")
    driver.find_element_by_class_name("gLFyf").send_keys(search_term + Keys.ENTER)
    elements = driver.find_elements_by_class_name("LC20lb")
    if len(elements) == 0:
        driver.close()
        driver = webdriver.Chrome(ChromeDriverManager().install())
    # elements[[e.text for e in elements].index(boosted_site)].click()
    print("Iteration #{} Done!".format(iterations))
    iterations += 1