from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from simpleeval import simple_eval

if __name__ == "__main__":
    # use selenium to screen grab the page
    url = "https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad"
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    screenshot = driver.save_screenshot('ss.png')
    driver.quit();
