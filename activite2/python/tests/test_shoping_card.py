import pytest
import sys
import os
from unittest.mock import Mock
from shopping_cart import ShoppingCart
from model_objects import Product, ProductUnit, SpecialOfferType, Offer, Discount
from receipt import Receipt


class MockCatalog:
    """Mock du catalogue pour contrôler les prix"""
    def __init__(self, prices=None):
        self.prices = prices or {}
        self.unit_price_calls = []
    
    def unit_price(self, product):
        self.unit_price_calls.append(product)
        return self.prices.get(product.name, 1.0)


class TestShoppingCart:
    """Tests de la classe ShoppingCart avec pytest"""
    
    def setup_method(self):
        """Setup avant chaque test"""
        self.cart = ShoppingCart()
        self.apple = Product("apple", ProductUnit.EACH)
        self.banana = Product("banana", ProductUnit.EACH)

    def test_add_item(self):
        """Test d'ajout d'un article simple"""
        self.cart.add_item(self.apple)
        
        # Vérification que l'article est dans items (via ProductQuantity)
        assert len(self.cart.items) == 1
        assert self.cart.items[0].product == self.apple
        assert self.cart.items[0].quantity == 1.0
        
        # Vérification des quantités
        assert self.apple in self.cart.product_quantities
        assert self.cart.product_quantities[self.apple] == 1.0

    def test_add_item_quantity(self):
        """Test d'ajout avec quantité spécifique"""
        quantity = 2.5
        self.cart.add_item_quantity(self.apple, quantity)
        
        assert self.apple in self.cart.product_quantities
        assert self.cart.product_quantities[self.apple] == quantity
        
        # Vérification dans items
        assert len(self.cart.items) == 1
        assert self.cart.items[0].quantity == quantity
   
    def test_add_different_items(self):
        """Test d'ajout d'articles différents"""
        self.cart.add_item(self.apple)
        self.cart.add_item_quantity(self.banana, 3.0)
        
        assert len(self.cart.items) == 2
        assert self.cart.product_quantities[self.apple] == 1.0
        assert self.cart.product_quantities[self.banana] == 3.0

    def test_handle_offers_three_for_two(self):
        """Test de l'offre 3 pour 2"""
        receipt = Receipt()
        catalog = MockCatalog({"apple": 1.50})
        offer = Offer(SpecialOfferType.THREE_FOR_TWO, self.apple, 0)
        offers = {self.apple: offer}
        
        self.cart.add_item_quantity(self.apple, 3)
        self.cart.handle_offers(receipt, offers, catalog)
        
        assert len(receipt.discounts) == 1
        discount = receipt.discounts[0]
        assert discount.product == self.apple
        assert discount.description == "3 for 2"
        assert discount.discount_amount == pytest.approx(-1.50, abs=0.01)

    def test_handle_offers_ten_percent_discount(self):
        """Test de la remise pourcentage"""
        receipt = Receipt()
        catalog = MockCatalog({"apple": 10.0})
        offer = Offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, self.apple, 15.0)
        offers = {self.apple: offer}
        
        self.cart.add_item_quantity(self.apple, 2)
        self.cart.handle_offers(receipt, offers, catalog)
        
        assert len(receipt.discounts) == 1
        discount = receipt.discounts[0]
        assert discount.description == "15.0% off"
        # 15% de (2 * 10.0) = 3.0
        assert discount.discount_amount == pytest.approx(-3.0, abs=0.01)

# Tests avec des fixtures pytest
@pytest.fixture
def empty_cart():
    """Fixture pour un panier vide"""
    return ShoppingCart()


@pytest.fixture
def sample_products():
    """Fixture pour des produits d'exemple"""
    return {
        'apple': Product("apple", ProductUnit.EACH),
        'banana': Product("banana", ProductUnit.EACH),
        'milk': Product("milk", ProductUnit.EACH)
    }


def test_empty_cart_with_fixture(empty_cart):
    """Test utilisant une fixture"""
    assert len(empty_cart.items) == 0
    assert len(empty_cart.product_quantities) == 0


def test_add_items_with_fixtures(empty_cart, sample_products):
    """Test d'ajout d'articles avec fixtures"""
    empty_cart.add_item(sample_products['apple'])
    empty_cart.add_item_quantity(sample_products['banana'], 3)
    
    assert len(empty_cart.items) == 2
    assert empty_cart.product_quantities[sample_products['apple']] == 1.0
    assert empty_cart.product_quantities[sample_products['banana']] == 3.0