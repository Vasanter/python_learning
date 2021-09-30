from selenium.webdriver.chrome.webdriver import WebDriver


def test_yandex_search():
    driver = WebDriver(executable_path='C:\selenium\chromedriver.exe')
    driver.get('http://yandex.ru')
    print(None)

    ...
