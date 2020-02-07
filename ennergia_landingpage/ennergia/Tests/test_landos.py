from pytest_bdd import scenario, when, then


@scenario('../Features/landos.feature', "When phone entered incorrectly error notification appears")
def test_landos():
    pass

@when("open the main page")
def open_main_page(driver, home_page):
    home_page.open("https://m.ennergiia.com/")


@when("open menu")
def choose_section(driver, home_page):
    home_page.open_menu()


@when("choose menu block")
def choose_menu_block(driver, home_page):
    home_page.choose_menu_block()

@when("scroll down")
def jumpdown_button(driver, landos_page):
    landos_page.jumpdown_button()

@when("enter email")
def choose_email(driver, landos_page):
    landos_page.choose_email()


@when("enter name")
def choose_name(driver, landos_page):
    landos_page.choose_name()

@when("enter surname")
def choose_surname(driver, landos_page):
    landos_page.choose_surname()

@when("enter incorrect phone number")
def choose_phone(driver, landos_page):
    landos_page.choose_phone()


@when("enter city")
def choose_city(driver, landos_page):
    landos_page.choose_city()

@when("enter info")
def choose_info(driver, landos_page):
    landos_page.choose_info()

@when("press rule button")
def press_galka(driver, landos_page):
    landos_page.press_galka()

@when("press send button")
def press_ok(driver, landos_page):
    landos_page.press_ok()

@then("see the error notification")
def see_notification(driver, landos_page):
    landos_page.see_notification()
