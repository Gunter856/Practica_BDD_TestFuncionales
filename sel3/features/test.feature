Feature: Shopping Cart Functionality

Scenario Outline: visit "<website>" and check "<title>"
    When we visit "<website>"
    Then it should have a title "<title>"

    Examples: 
        | website                     | title |
        | https://www.lidl.es         | Compra Online \| Lidl |


Scenario Outline: search "<AirFryer_product>" and count "<total_amount>"
    When we search "<AirFryer_product>"
    Then it should be "<total_amount>"

    Examples: 
        | AirFryer_product   | total_amount |
        | Air Fryer          | 21           |


Scenario Outline: "Air Fryers" are searched check "<website_title>"
    Then it has to be "<website_title>"

    Examples: 
        | website_title   |
        | Resultado de búsqueda \| Lidl |

Scenario Outline: add product "Air Fryer" to "shopping cart" and check "<message>"
    When add product "Air Fryer"
    Then check "<message>"

    Examples:
        | message |
        | ¡Buena elección! El artículo ha sido añadido a tu cesta de la compra. |
