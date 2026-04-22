import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pathlib import Path

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate()
    return lp

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture(scope="session")
def test_users():
    data_file = Path(__file__).parent / "test-data" / "users.json"
    with open(data_file) as f:
        return json.load(f)
    
@pytest.fixture(scope="session")
def test_products():
    data_file = Path(__file__).parent /  "test-data" / "product_prices.json"
    with open(data_file) as f:
        return json.load(f)

@pytest.fixture
def logged_in_inventory(page, test_users):
    lp = LoginPage(page)
    lp.navigate()
    user = test_users["valid_user"]
    lp.login(user["username"], user["password"])
   
    inventory = InventoryPage(page)
    inventory.should_be_loaded()  

    return inventory

@pytest.fixture
def inventory_with_item(logged_in_inventory, test_products):
        product = test_products["test_product"]
        logged_in_inventory.add_to_cart(product)
        return logged_in_inventory