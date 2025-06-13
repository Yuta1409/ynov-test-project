import unittest
import pytest
from cart import add_item, get_total

class TestCart(unittest.TestCase):
    
    def test_add_item(self):
        panier = {}
        add_item(panier, "item1", 10, 2)
        self.assertIn("item1", panier)
        self.assertEqual(panier["item1"]["price"], 10)
        self.assertEqual(panier["item1"]["quantity"], 2)
        
    def test_get_total(self):
        panier = {"item1": {"price": 10, "quantity": 2}}
        total = get_total(panier)
        self.assertEqual(total, 20)

class TestCartPytest:
    
    def test_add_item(self):
        panier = {}
        add_item(panier, "item1", 10, 3)
        assert "item1" in panier
        assert panier["item1"]["price"] == 10
        assert panier["item1"]["quantity"] == 3
        add_item(panier, "item2", 20, 1)
        assert "item2" in panier
        assert panier["item2"]["price"] == 20
        assert panier["item2"]["quantity"] == 1
        
    def test_get_total(self):
        panier = {"item1": {"price": 10, "quantity": 2}, "item2": {"price": 20, "quantity": 1}}
        total = get_total(panier)
        assert total == 40
        
if __name__ == "__main__":
    pytest.main();
    #unittest.main()