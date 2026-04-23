import pytest
from playwright.sync_api import expect

def test_add_cart(logged_in_inventory):
   logged_in_inventory.add_to_cart("sauce-labs-backpack")
   logged_in_inventory.add_to_cart("sauce-labs-bike-light")
   expect(logged_in_inventory.cart_badge).to_contain_text("2")

@pytest.mark.parametrize("product", [
   "sauce-labs-backpack",
   "sauce-labs-bike-light",
   "sauce-labs-bolt-t-shirt",
   "sauce-labs-fleece-jacket",
   "sauce-labs-onesie",
   "test.allthethings()-t-shirt-(red)"
])
def test_add_various_products(logged_in_inventory, product):
   logged_in_inventory.add_to_cart(product)
   expect(logged_in_inventory.cart_badge).to_contain_text("1")

def test_remove_from_cart(inventory_with_item, test_products):
   product = test_products["test_product"]
   inventory_with_item.remove_from_cart(product)
   assert inventory_with_item.cart_badge_count() == 0

def test_all_product_have_prices(logged_in_inventory):
   prices = logged_in_inventory.get_all_prices()
   assert len(prices) > 0
   for price in prices:
      assert price.startswith("$")
      assert len(price) > 1
    
def test_product_prices(logged_in_inventory, test_products):
   for product in test_products["products"]:
      price = logged_in_inventory.get_price_for(product["name"])
      assert price is not None, f"Product '{product['name']}' not found on page"
      assert price == product["price"]

def test_single_sorting_button(logged_in_inventory):
   before_sort = logged_in_inventory.get_product_names()
   logged_in_inventory.sort_product("za")
   after_sort = logged_in_inventory.get_product_names()
   expected = sorted(before_sort, reverse=True)
   assert after_sort == expected

@pytest.mark.parametrize("value, reverse", [
    ("az", False),
    ("za", True),
])
def test_sorting_by_name(logged_in_inventory, value, reverse):
   before = logged_in_inventory.get_product_names()
   logged_in_inventory.sort_product(value)
   after = logged_in_inventory.get_product_names()
   expected = sorted(before, reverse=reverse)

   assert after == expected

def test_sorting_by_price_lohi(logged_in_inventory):
   before_sort = logged_in_inventory.get_prices_as_number()
   logged_in_inventory.sort_product("lohi")
   after_sort = logged_in_inventory.get_prices_as_number()
   assert after_sort == sorted(before_sort)

@pytest.mark.parametrize("value, reverse", [
   ("lohi", False),
   ("hilo", True)
])
def test_sorting_by_price(logged_in_inventory, value, reverse):
   before_sort = logged_in_inventory.get_prices_as_number()
   logged_in_inventory.sort_product(value)
   after_sort = logged_in_inventory.get_prices_as_number()
   expected = sorted(before_sort, reverse=reverse)

   assert after_sort == expected