from framework.ui.pages.checkboxes_page import CheckboxesPage


def test_checkbox_selected(driver):
    page = CheckboxesPage(driver)

    page.open()

    checkboxes = page.get_checkboxes()

    assert checkboxes[0].is_selected() is False
    assert checkboxes[1].is_selected() is True