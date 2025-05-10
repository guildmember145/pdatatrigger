from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura el driver de Selenium (asegúrate de tenerlo instalado y en el PATH)
driver = webdriver.Chrome()


@given("the user is on the Pdatatrigger frontend")
def user_on_frontend(context):
    driver.get("http://localhost:8501")  # Puerto por defecto de Streamlit


@when('the user enters "{url}" in the target URL field')
def enter_target_url(context, url):
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input")
        )  # Ajusta el selector según la estructura de Streamlit
    )
    input_field.send_keys(url)


@when('the user clicks the "Scan" button')
def step_impl(context):
    scan_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[text()='Scan']")
        )  # Ajusta el selector
    )
    scan_button.click()


@then('the user should see the scan results for "{url}"')
def step_impl(context, url):
    results_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//h3[contains(text(), 'Scan Results for: {url}')]")
        )  # Ajusta el selector
    )
    assert results_header.is_displayed()


@then("the user should see a list of vulnerabilities")
def step_impl(context):
    vulnerability_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Vulnerabilities Found:')]")
        )  # Ajusta el selector
    )
    assert vulnerability_list.is_displayed()


# Asegúrate de cerrar el driver al final de las pruebas (en environment.py)
