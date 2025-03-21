from flask import Flask, render_template, request, redirect, url_for, session
from products_data import get_products

app = Flask(__name__)
app.secret_key = "realkey"

def get_saved_items():
    saved_items = session.get("saved_items", [])
    saved_items_count = len(saved_items)
    return saved_items, saved_items_count

@app.route('/')
def home():
    products = get_products()
    saved_items, saved_items_count = get_saved_items()
    return render_template('index.html', products=products, saved_items_count=saved_items_count)

@app.route('/shop')
def shop():
    products = get_products()
    saved_items, saved_items_count = get_saved_items()
    return render_template('shop.html', products=products, saved_items=saved_items, saved_items_count=saved_items_count)

@app.route('/about')
def about():
    saved_items, saved_items_count = get_saved_items()
    return render_template('about.html', saved_items_count=saved_items_count)

@app.route('/contact')
def contact():
    saved_items, saved_items_count = get_saved_items()
    return render_template('contact.html', saved_items_count=saved_items_count)

@app.route('/saved_items')
def saved_items_page():
    saved_items = session.get("saved_items", [])
    saved_items_count = len(saved_items)
    return render_template('saved_items.html', saved_items=saved_items, saved_items_count=saved_items_count)


@app.route('/save_item', methods=['POST'])
def save_item():
    product_name = request.form['product_name']
    purchase_link = request.form['purchase_link']
    saved_items = session.get("saved_items", [])
    product = None

    for category, items in get_products().items():
        product = next((item for item in items if item['name'] == product_name), None)
        if product:
            break
    if product:
        image = product['image']
        price = product.get('price', 'Price unavailable')
        source = product.get('source', 'Website')  # Gets 'source', default to 'Website' if not found
    else:
        image = None
        price = 'Price unavailable'
        source = 'Website'

    # Only adds the item if it's not already saved
    if not any(item['name'] == product_name for item in saved_items):
        saved_items.append({
            'name': product_name,
            'purchase_link': purchase_link,
            'image': image,
            'price': price,
            'source': source,
        })
        session["saved_items"] = saved_items

    # Reloads the page
    return render_template('shop.html', products=get_products(), saved_items=saved_items, saved_items_count=len(saved_items))

@app.route('/remove_saved_item', methods=['POST'])
def remove_saved_item():
    product_name = request.form['product_name']
    saved_items = session.get("saved_items", [])

    # Remove the item based on the name
    saved_items = [item for item in saved_items if item['name'] != product_name]
    session["saved_items"] = saved_items

    return redirect(url_for('saved_items_page'))

if __name__ == '__main__':
    app.run(debug=True)
