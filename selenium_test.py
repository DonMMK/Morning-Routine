# import time

# from selenium import webdriver



# driver = webdriver.Chrome('Applications')  # Optional argument, if not specified will search path.

# driver.get('http://www.google.com/');

# time.sleep(5) # Let the user actually see something!

# search_box = driver.find_element_by_name('q')

# search_box.send_keys('ChromeDriver')

# search_box.submit()

# time.sleep(5) # Let the user actually see something!
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())


# import modules
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
  
# use chrome driver
driver = webdriver.Chrome("/Applications/chromedriver.exe")
  
# assign web page url
driver.get("http://demo.automationtesting.in/Windows.html")
  
# find XPath
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
  
# return all handles value of open browser window
handles = driver.window_handles
  
for i in handles:
    driver.switch_to.window(i)
  
    # close specified web page
    if driver.title == "Frames & windows":
        time.sleep(2)
        driver.close()

