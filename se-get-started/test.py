# Import a few things from the Selenium package.

import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as expects
from selenium.webdriver.common.by import By

# Next, we'll give our script access to the Chrome web driver so that we can
# interact with the browser.

driver = webdriver.Chrome('./chromedriver')

# Before we can test our page, we must load it in the browser. We'll start a
# web server on localhost later, so we'll load `http://localhost:8000`.

driver.get('http://localhost:8000')


# Since we don't know when the page will complete loading, we'll have to make
# our script wait. Specifically, we'll wait for the text in the body of our
# page to be visible. To do this, we'll create a function called
# `wait_for_element_has_text` that takes the tag name of an element, a web
# driver object, and the text we want to wait for.

def wait_for_element_has_text(element, driver, text):
    # In this function, we'll create an object that represents the maximum
    # amount of time we're willing to wait. This is called a *timeout*. We'll
    # choose 10 seconds for our timeout.

    wait = ui.WebDriverWait(driver, 10)

    # Next, we need a way to tell Selenium how to find an element. We do this
    # by creating a tuple which says we should use CSS selectors to find the
    # element (`By.CSS_SELECTOR`) and contains the selector we want to use
    # (`element`).

    selector = (By.CSS_SELECTOR, element)

    # Now, we need an object that represents what we are waiting for and
    # expecting to happen in the web browser--that there should be visible text
    # in our chosen element. We can do that using
    # `expects.text_to_be_present_in_element`.

    expectation = expects.text_to_be_present_in_element(selector, text)

    # Finally, we'll tell Selenium to wait for our expectation to be fulfilled,
    # or for the 10-second timeout to expire (whichever comes first).

    wait.until(expectation)


# After writing that function, we can use it to wait for the correct text to
# appear in the body of our page.

text = 'Test that this text is here!'
wait_for_element_has_text('body', driver, text)

# Lastly, we'll assert that the text we expect in the body element is there.

body = driver.find_element_by_tag_name('body')
assert body.text == text

driver.quit()
