# Ajouter une article 
# Supprimer un article
# Modifier la quantité d'articles
# Calculer le total du panier
# Vider le panier

def add_item(cart, item, price, quantity):
    """Ajoute un article au panier"""
    if item in cart:
        cart[item]['quantity'] += quantity
    else:
        cart[item] = {'price': price, 'quantity': quantity}

def get_total(panier):
    """Calcule le total du panier"""
    total = 0
    for item in panier.values():
        total += item['price'] * item['quantity']
    return total
