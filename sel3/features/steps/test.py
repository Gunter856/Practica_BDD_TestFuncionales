from behave import given,when,then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@when(u'we visit "{website}"')
def step(context, website):
   context.browser.get(f"{website}")

@then('it should have a title "{title}"')
def step(context, title ):
    assert context.browser.title == f"{title}"

@when(u'we search "{AirFryer_product}"')
def step_impl(context, AirFryer_product):
   a=context.browser.find_element(By.ID, 'mainsearch-input') # busca la barra de busqueda
   a.send_keys(f'{AirFryer_product}' + Keys.ENTER) # escribe en la barra de busqueda y simula el "enter"

@then(u'it should be "{total_amount}"')
def step_impl(context, total_amount):
   productos = context.browser.find_elements(By.CLASS_NAME, 'product-grid-box-tile') # almacena los productos
   cuenta = len(productos) # cuenta la cantidad de productos
   assert cuenta == int(total_amount)

@then(u'it has to be "{website_title}"')
def step_impl(context, website_title):
   assert context.browser.title == f"{website_title}"

@when('add product "Air Fryer"')
def step_impl(context):
   context.browser.find_element(By.CLASS_NAME, 'product-grid-box-tile').click()
   context.browser.find_element(By.ID, 'add-to-cart').click()

@then(u'check "{message}"')
def step_impl(context, message):
   assert context.browser.find_element(By.CLASS_NAME, 'basket-overlay__title').text == f"{message}"