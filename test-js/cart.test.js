const { Cart } = require('../test-js/cart');

beforeEach(() => {
    const cart = new Cart();
    cart.items = [];
});

test('Ajout d\'un article au panier', () => {
    const cart = new Cart();
    cart.addItem('apple', 1.00, 2);
    expect(cart.items.length).toBe(1);
    expect(cart.items[0].item).toBe('apple');
    expect(cart.items[0].price).toBe(1.00);
    expect(cart.items[0].quantity).toBe(2);
});

test('Calcule le prix total des articles dans le panier', () => {
    const cart = new Cart();
    cart.addItem('apple', 1.00, 2);
    cart.addItem('banana', 0.50, 4);
    expect(cart.getTotal()).toBe(4.00);
});