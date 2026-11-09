import os
from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'bezawada_secret_admin_key_2026'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bezawada_deals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=True)
    discount = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    image_url = db.Column(db.String(500), nullable=True)
    terms = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(300), nullable=True)

ADMIN_CREDENTIALS = {
    "username": "revathi",
    "password": "secure123"
}

with app.app_context():
    db.create_all()
    if Deal.query.count() < 6:
        initial_deals = [
            # PVP Square Mall Multiple Deals
            Deal(
                place_name="PVP Mall", 
                category="Clothes", 
                title="PVP Mall Designer Ethnic Saree Sale", 
                description="Flat 50% discount on Silk & Festive collections.", 
                discount="50% OFF", 
                price=1499.0,
                image_url="https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=600&q=80",
                terms="Valid at PVP Mall 2nd Floor outlet.",
                address="MG Road, Vijayawada, AP 520010"
            ),
            Deal(
                place_name="PVP Mall", 
                category="Food", 
                title="PVP Mall Food Court Family Combo", 
                description="Burgers, Pizzas, and Cold Drinks combo pack.", 
                discount="Buy 1 Get 1 Free", 
                price=399.0,
                image_url="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80",
                terms="Valid on weekdays at PVP Mall Food Court.",
                address="3rd Floor Food Court, PVP Square, Vijayawada"
            ),

            # Trendset Mall Deals
            Deal(
                place_name="Trendset Mall", 
                category="Clothes", 
                title="Trendset Mall Branded Footwear Fest", 
                description="Top sneaker and footwear brands special discount sale.", 
                discount="Flat 40% OFF", 
                price=999.0,
                image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&q=80",
                terms="Offer valid till stocks last at Benz Circle Trendset Mall.",
                address="Benz Circle, MG Road, Vijayawada"
            ),

            # Supermarkets
            Deal(
                place_name="Governorpet", 
                category="Supermarkets", 
                title="DMart Wholesale Grocery Savings", 
                description="Rice, pulses, oils, and kitchen staples at wholesale prices.", 
                discount="Wholesale Rate", 
                price=199.0,
                image_url="https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&q=80",
                terms="Valid at Bavajipet DMart store.",
                address="Samba Murthy Road, Governorpet, Vijayawada"
            ),

            # Eluru Road Electronics Hub
            Deal(
                place_name="Eluru Road", 
                category="Electronics", 
                title="NTR Complex Fast Charger & Screen Guard Combo", 
                description="Tempered glass, back cases, 65W fast chargers set.", 
                discount="Special Pack", 
                price=199.0,
                image_url="https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=600&q=80",
                terms="30 days replacement warranty.",
                address="NTR Complex, Eluru Road, Vijayawada"
            ),

            # Food / Mess Joints
            Deal(
                place_name="Governorpet", 
                category="Food", 
                title="Sai Charanam Aritaku Mess Meals", 
                description="Authentic Andhra unlimited meals served on traditional banana leaf.", 
                discount="Best Price", 
                price=90.0,
                image_url="https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=600&q=80",
                terms="Lunch time only (12 PM to 3:30 PM).",
                address="Near Santhi Theatre, Governorpet, Vijayawada"
            )
        ]
        for d in initial_deals:
            exists = Deal.query.filter_by(title=d.title).first()
            if not exists:
                db.session.add(d)
        db.session.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/customer-service')
def customer_service():
    return render_template('customer_service.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if session.get('is_admin'):
        success_msg = None
        error_msg = None
        if request.method == 'POST':
            action = request.form.get('action')
            if action == 'change_password':
                old_pass = request.form.get('old_password')
                new_pass = request.form.get('new_password')
                if old_pass == ADMIN_CREDENTIALS['password']:
                    ADMIN_CREDENTIALS['password'] = new_pass
                    success_msg = "Password updated successfully!"
                else:
                    error_msg = "Incorrect old password!"
            else:
                new_deal = Deal(
                    place_name=request.form.get('place_name'),
                    category=request.form.get('category'),
                    title=request.form.get('title'),
                    description=request.form.get('description'),
                    discount=request.form.get('discount'),
                    price=float(request.form.get('price', 0.0)),
                    image_url=request.form.get('image_url') or "https://images.unsplash.com/photo-1555529771-835f59fc5efe?w=500&q=80",
                    terms=request.form.get('terms') or "Standard store terms apply.",
                    address=request.form.get('address') or "Vijayawada, AP"
                )
                db.session.add(new_deal)
                db.session.commit()
                return redirect(url_for('admin'))
        deals = Deal.query.order_by(Deal.id.desc()).all()
        return render_template('admin.html', deals=deals, success_msg=success_msg, error_msg=error_msg)
    
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == ADMIN_CREDENTIALS['username'] and password == ADMIN_CREDENTIALS['password']:
            session['is_admin'] = True
            return redirect(url_for('admin'))
        else:
            error = "Invalid Username or Password!"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('is_admin', None)
    return redirect(url_for('admin'))

@app.route('/api/offers', methods=['GET'])
def get_offers():
    category_filter = request.args.get('category')
    search_query = request.args.get('search')
    query = Deal.query

    if category_filter and category_filter != 'All':
        query = query.filter_by(category=category_filter)
    if search_query and search_query != 'All':
        query = query.filter(Deal.title.ilike(f"%{search_query}%") | Deal.place_name.ilike(f"%{search_query}%"))

    deals = query.order_by(Deal.id.desc()).all()
    result = [{
        "id": d.id,
        "place_name": d.place_name,
        "category": d.category,
        "title": d.title,
        "description": d.description,
        "discount": d.discount,
        "price": d.price,
        "image_url": d.image_url,
        "terms": d.terms,
        "address": d.address
    } for d in deals]
    return jsonify({"status": "success", "data": result})

if __name__ == '__main__':
    app.run(debug=True)
