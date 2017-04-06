from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

d = webdriver.Firefox()
final = []

start = 608749
i = 0
delay = 3
while i< 26:
    print chr(ord('a')+i)
    d.get("https://www.thoughtco.com/a-organic-compounds-list-" + str(start+i))
    try:
        WebDriverWait(d, delay).until(EC.presence_of_element_located(d.find_element_by_id("flex_1-0")))
        f= d.find_element_by_id("flex_1-0")
        lines = f.text.splitlines()
        for x in lines:
            if '-' in x:
                final.append(x.split(' - '))
    except TimeoutException:
        #Ignore this case
        print 'Page not present'
    #print(f.text.splitlines())

    i += 1
"""
d.get("https://pubchem.ncbi.nlm.nih.gov/")
d.find_element_by_id("term").send_keys(final[0][0].strip())
d.find_element_by_id("go").click()
time.sleep(1)
print d.find_elements_by_class_name("rsltimg")
"""
