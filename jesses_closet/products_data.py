from collections import defaultdict
from urllib.parse import urlparse

def get_products():
    products = [
        # Hoodies
        {"category": "Hoodies", "name": "Black and White Hoodie", "description": "SOUTHPOLE Vintage Y2K Rare Men White Skull Paisley AOP Jesse Pinkman Hoodie XL", "price": 85, "image": "hoodie.jpg", "purchase_link": "https://www.ebay.com/itm/135558928900", "source": "eBay"},
        {"category": "Hoodies", "name": "Colorful Grunge Hoodie", "description": "Y2K Hoodie Mens Large Tan Crazy Rare AOP Reversible Grunge Jesse Pinkman Skater", "price": 200, "image": "grungehoodie.jpg", "purchase_link": "https://www.ebay.com/itm/335782560890", "source": "eBay"},
        {"category": "Hoodies", "name": "Classic Yellow Hoodie", "description": "Aaron Paul Breaking Bad Jesse Pinkman Yellow Hoodie", "price": 179, "image": "yellow_hoodie.jpg", "purchase_link": "https://celebsleatherjackets.com/products/aaron-paul-breaking-bad-jesse-pink-man-yellow-hoodie.html", "source": "Celebs Leather Jackets"},

        # Shirts
        {"category": "Shirts", "name": "Black Skull Shirt", "description": "Skull With Tongue T-Shirt", "price": 21.95, "image": "skull_shirt.jpg", "purchase_link": "https://cineattire.com/product/skull-with-tongue-t-shirt-jesse-pinkman-breaking-bad/", "source": "CineAttire"},
        {"category": "Shirts", "name": "Yellow Symbols Shirt", "description": "Golden Funny Symbol Skull Snake T-Shirt", "price": 21.95, "image": "tshirt.jpg", "purchase_link": "https://cineattire.com/product/golden-funny-symbol-skull-snake-t-shirt-jesse-pinkman-breaking-bad/", "source": "CineAttire"},

        # Pants
        {"category": "Pants", "name": "Depop Baggy Affliction Jeans", "description": "Affliction Men's Black Jeans XXL", "price": 250, "image": "affliction_jeans.jpg", "purchase_link": "https://www.depop.com/products/alex718128-jesse-pinkman-type-shi-looking/", "source": "Depop"},
        {"category": "Pants", "name": "Imperious x Jnco x Southpole Jeans", "description": "Vintage Delf Imperious Baggy Goth Winged Jeans", "price": 135, "image": "jnco_jeans.jpg", "purchase_link": "https://www.grailed.com/listings/73012463-imperious-x-jnco-x-southpole-vintage-delf-imperious-baggy-goth-winged-jeans-jesse-pinkman", "source": "Grailed"},

        # Shoes
        {"category": "Shoes", "name": "Black Star Sneakers", "description": "Goat.com Bapesta 'Black'", "price": '700-1100', "image": "bapesta_black.jpg", "purchase_link": "https://www.goat.com/sneakers/bapesta-black-1h70191001-blk", "source": "GOAT"},
        {"category": "Shoes", "name": "Red Air Jordan Sneakers", "description": "RIOT Skateshop x Dunk Low SB 'Mahogany Dark Beetroot'", "price": '120-150', "image": "red_jordans.jpg", "purchase_link": "https://www.goat.com/sneakers/riot-skateshop-x-dunk-low-sb-mahogany-dark-beetroot-fz1289-200", "source": "GOAT"},

        # Accessories
        {"category": "Accessories", "name": "Season 1 Beanie", "description": "Sportsman Bottom Striped Knit Beanie One Size Black/ Red", "price": 7.89, "image": "beanie.jpg", "purchase_link": "https://www.amazon.com/Sportsman-Bottom-Stripe-Knit-Black/dp/B00CT4JCKO", "source": "Amazon"},
        {"category": "Accessories", "name": "Silver Chain", "description": "Rope Chain - Silver (3mm)", "price": 49, "image": "silver_chain.jpg", "purchase_link": "https://jvillion.com/products/rope-necklace-silver-3mm?variant=41299251658961", "source": "JVillion"},
    ]

    categorized_products = defaultdict(list)
    for product in products:
        categorized_products[product["category"]].append(product)

    return categorized_products
