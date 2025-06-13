/**
 * Ajouter une article
 * Supprimer un article
 * Modifier la quantité d'articles
 * Calculer le total du panier
 * Vider le panier
 */

class Cart {  

    constructor() {
        this.items = [];
    }
    
    addItem(item, price, quantity) {
        this.items.push({
            item: item,
            price: price,
            quantity: quantity
        });
    }
    
    getTotal() {
        return this.items.reduce((total, item) => total + item.price * item.quantity, 0);
    }
}

module.exports = { Cart };
