import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


######## PYTEST HTML REPORT GENERATION #######

#Hook for adding env info in html report
def pytest_configure(config):
    if config.pluginmanager.getplugin("metadata"):
        config.stash[metadata_key]['Project Name'] = "Sauce Demo"
        config.stash[metadata_key]['Author'] = "Ibrahim"

#Hook for deleting/modify env info in html report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None) 