import threading
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def iterate(max_iterations, search_term, boosted_site):
    iterations = 1
    driver = webdriver.Chrome(ChromeDriverManager().install())
    start = datetime.now()
    while iterations < max_iterations:
        driver.get("https://www.google.com")
        driver.find_element_by_class_name("gLFyf").send_keys(search_term + Keys.ENTER)
        elements = driver.find_elements_by_class_name("LC20lb")
        if len(elements) == 0:
            driver.close()
            driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            elements[[e.text for e in elements].index(boosted_site)].click()
            print("Iteration #{} done!".format(iterations))
            iterations += 1
    end = datetime.now()
    print("Time for {} iterations: {}".format(iterations-1, end-start))


new_search_term = "The Propaganda Model"
new_boosted_site = "The Propaganda Model – Media Studies 101"

print("Starting the code!")
threads = [threading.Thread(target=iterate, args=(100, new_search_term, new_boosted_site)) for _ in range(4)]
[thread.start() for thread in threads]
