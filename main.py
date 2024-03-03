from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a driver for Chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open website
driver.get("https://www.coinbase.com/")

# Get current window's handle
current_handle = driver.current_window_handle

# Click on Explore
driver.find_element(By.LINK_TEXT, "Explore").click()

time.sleep(5)

# Reject cookies
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/button[1]').click()

# Click on Bitcoin
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div/div/a/span/div/h2').click()

time.sleep(5)

# Get all windows' handles
all_handles = driver.window_handles

for handle in all_handles:
    driver.switch_to.window(handle)

    # Close the window which we are not working in
    if handle == current_handle:
        driver.close()

# Print current price of Bitcoin
bitcoin_price = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div/main/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div/span')
print(f"The current price of Bitcoin is {bitcoin_price.text}.\n")

# Scroll down until we reach News section
news = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div/main/div[2]/div[4]/div[1]/h3')
driver.execute_script("arguments[0].scrollIntoView();", news)

# Find all article elements
articles = driver.find_elements(By.TAG_NAME, "article")
article_titles = [article.find_element(By.CLASS_NAME, "cds-typographyResets-t1xhpuq2.cds-headline-hb7l4gg.cds-foreground-f1yzxzgu.cds-transition-txjiwsi.cds-start-s1muvu8a.cds-numberOfLines-n6pg8f8").text for article in articles]
print(article_titles)

# Ask user which article they want to read
choose_article = input("Which article do you want to read? ")

for article in articles:
    if article.find_element(By.CLASS_NAME, "cds-typographyResets-t1xhpuq2.cds-headline-hb7l4gg.cds-foreground-f1yzxzgu.cds-transition-txjiwsi.cds-start-s1muvu8a.cds-numberOfLines-n6pg8f8").text == choose_article:
        article.click()

# # Closes all tabs
# driver.quit()