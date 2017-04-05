from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
d = webdriver.Firefox()
final = []

start = 608749
while start < 608771:
    print (start)
    d.get("https://www.thoughtco.com/a-organic-compounds-list-" + str(start))
    try:
        f= d.find_element_by_id("flex_1-0")
        lines = f.text.splitlines()
        for x in lines:
            if '-' in x:
                final.append(x.split(' - '))
    except NoSuchElementException:
        #Ignore this case
        print 'Page not present'
    #print(f.text.splitlines())

    start += 1

print final
d.get("https://pubchem.ncbi.nlm.nih.gov/")
d.quit()
