import os.path
import pytest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import TestData


@pytest.fixture(autouse=True, scope="function")
def setup_browser(request):
    global driver
    match TestData.BROWSER:
        case "CHROME":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.headless = TestData.HEADLESS_BROWSER
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        case "FIREFOX":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.headless = TestData.HEADLESS_BROWSER
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        case "OPERA":
            opera_options = webdriver.ChromeOptions()
            opera_options.headless = TestData.HEADLESS_BROWSER
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opera_options)
        case default:
            raise Exception("Please specify the correct browser name " + TestData.BROWSER)

    driver.delete_all_cookies()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.get(TestData.BASE_URL)
    request.cls.driver = driver

    yield
    driver.quit()


"""
    This fixture is used to remove every file that is under the directory reports.
    This fixture will be executed only once, before tests start to execute (scope="session")
"""


@pytest.fixture(autouse=True, scope="session")
def clean_up_reports_folder():
    # IF statement is for checking that if you run tests directly from test file, it will redirect user on directory up
    # in order to find reports folder and delete its contents
    # If you run tests using the terminal command this IF statement will be ignored
    if "tests" in os.path.abspath(os.curdir):
        os.chdir("..")
    # Delete all files that are inside the reports directory
    for file in os.scandir(os.path.abspath(os.curdir) + "/reports"):
        os.remove(file.path)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        extra.append(pytest_html.extras.url(TestData.BASE_URL))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Get the directory where the Report is saved
            try:
                reports_directory = os.path.dirname(item.config.option.htmlpath)
            except TypeError:
                if "tests" in os.path.abspath(os.curdir):
                    os.chdir("..")
                reports_directory = os.path.abspath(os.curdir) + "/reports"
            # Set the name of the screenshot [failed_test_name] + [current_date] + [type of image]
            scr_file_name = \
                os.environ.get('PYTEST_CURRENT_TEST').replace('(call)', '').split(':')[-1].split('__')[0] \
                + datetime.now().strftime("%d-%m-%Y-%H-%M") + ".png"
            # Set the directory where the screenshot should be saved
            destination_file = os.path.join(reports_directory, scr_file_name)
            # Take the actual screenshot
            driver.save_screenshot(destination_file)
            if scr_file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % scr_file_name
                extra.append(pytest_html.extras.html(html))
                report.extra = extra


"""
@pytest.fixture(autouse=True, params=[TD.BROWSER], scope="function")
def setup_browser(request, browser):
    match browser:
        case "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.headless = TD.HEADLESS_BROWSER
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        case "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.headless = TD.HEADLESS_BROWSER
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        case "edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.use_chromium = TD.HEADLESS_BROWSER
            edge_options.headless = TD.HEADLESS_BROWSER
            driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
        case default:
            raise Exception("Please specify the correct browser name" + browser)

    driver.delete_all_cookies()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.get(TD.BASE_URL)
    request.cls.driver = driver

    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
"""
