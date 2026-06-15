from framework.ui.pages.add_remove_page import AddRemovePage


def test_add_element(driver):
    page = AddRemovePage(driver)

    page.open()

    page.add_element()
    page.add_element()
    page.add_element()

    buttons = page.get_delete_buttons()

    assert len(buttons) == 3


def test_delete_button_text(driver):
    page = AddRemovePage(driver)

    page.open()
    page.add_element()
    buttons = page.get_delete_buttons()
    assert buttons[0].text == "Delete"