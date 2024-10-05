from selene import browser, be, have


def test_positive_search():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_negative_search():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('hsdfgsdgsdgfsdgfsdgfsdfgsdgfsdgsdg').press_enter()
    browser.element('.card-section').should(have.text("Your search - hsdfgsdgsdgfsdgfsdgfsdfgsdgfsdgsdg - did not match any documents."))
