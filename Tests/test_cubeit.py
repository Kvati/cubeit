from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/113-index.html"

def test_cube(page: Page):
    page.goto(BASE_URL)

    input_field = page.get_by_placeholder("enter number...")
    button = page.get_by_role("button", name = "Cube")
    input_field.fill("5")
    button.click()

    result = page.locator("css=p#result")

    expect(result).to_contain_text("125")



def test_empty_input(page: Page):
    page.goto(BASE_URL)

    input_field = page.get_by_placeholder("enter number...")
    button = page.get_by_role("button", name="Cube")
    input_field.clear()
    button.click()

    result = page.locator("css=p#result")

    expect(result).to_have_text("Enter something!")


def test_negative_input(page: Page):
    page.goto(BASE_URL)

    input_field = page.get_by_placeholder("enter number...")
    button = page.get_by_role("button", name="Cube")
    input_field.fill("-4")
    button.click()

    result = page.locator("css=p#result")

    expect(result).to_contain_text("-64")

def test_letter_input(page: Page):
    page.goto(BASE_URL)

    input_field = page.get_by_placeholder("enter number...")
    button = page.get_by_role("button", name="Cube")
    input_field.fill("Some Text")
    button.click()

    result = page.locator("css=p#result")
    expect(input_field).to_be_empty()
    expect(result).to_have_text("Enter something!")