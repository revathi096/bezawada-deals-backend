
from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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

with app.app_context():
    db.create_all()
    
    # విజయవాడ లోకల్ మార్కెట్ సీడ్ డేటా (Low to High Price Range)
    initial_deals = [
        # Food & Mess (Low Budget)
        Deal(
            place_name="Governorpeta, Vijayawada", 
            category="Food", 
            title="Sai Charanam Aritaku Tiffins And Mess", 
            description="Traditional Andhra tiffins & banana leaf meals. Authentic Bezawada flavor.", 
            discount="Budget Friendly", 
            price=90.0,
            image_url="https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=600&q=80",
            terms="Valid on all days. Dine-in only. Offer applies to standard thali.",
            address="Governorpeta, near Santhi Theatre road, Vijayawada, AP 520002"
        ),
        Deal(
            place_name="Gandhi Nagar, Vijayawada", 
            category="Food", 
            title="Sarovar Mess Veg Meals", 
            description="Pure vegetarian Andhra meals served hot on banana leaf.", 
            discount="Special Meal Pass", 
            price=140.0,
            image_url="https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=600&q=80",
            terms="Valid during lunch hours 12 PM - 3:30 PM. Taxes applicable.",
            address="26-3-44, Nageswara Rao Pantulu Rd, Near Santhi Theatre, Gandhi Nagar, Vijayawada 520003"
        ),
        Deal(
            place_name="Gandhi Nagar, Vijayawada", 
            category="Food", 
            title="040 Biryani Special Family Combo", 
            description="Hyderabadi & Spicy Bezawada style Biryani with starters.", 
            discount="15% OFF", 
            price=299.0,
            image_url="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&q=80",
            terms="Applicable on takeaway and dine-in. Cannot be combined with other coupons.",
            address="26-1-3, Opp Sailaja Theater, Gandhi Nagar, Vijayawada 520003"
        ),

        # Supermarkets & Online Groceries
        Deal(
            place_name="Bavajipet - Samba Murthy Road", 
            category="Supermarkets", 
            title="DMart Hypermarket Daily Needs", 
            description="Daily groceries, rice, pulses, cooking oils, and home essentials at wholesale prices.", 
            discount="Wholesale Rates", 
            price=199.0,
            image_url="https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&q=80",
            terms="Prices subject to daily stock availability. Limited quantity per customer.",
            address="Bavajipet, Samba Murthy Road, Vijayawada 520003"
        ),
        Deal(
            place_name="Bavajipet, Vijayawada", 
            category="Online Groceries", 
            title="Boomers Mart Wholesale Grocery", 
            description="Online wholesale grocery store with free home delivery across Vijayawada.", 
            discount="Free Delivery", 
            price=299.0,
            image_url="https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=600&q=80",
            terms="Free delivery on orders above Rs. 499. Same-day delivery available.",
            address="Lanka Nilayam, 1st Floor, Bavaji Peta, 3rd line, Samba Murthy Rd, Vijayawada 520003"
        ),
        Deal(
            place_name="Governorpet - Gopala Reddy Road", 
            category="Supermarkets", 
            title="Reliance SMART Bazaar Grocery Combo", 
            description="Groceries, clothing, household items under one roof.", 
            discount="Flat 20% Savings", 
            price=499.0,
            image_url="https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=600&q=80",
            terms="Offer valid on select grocery brands. Show bill at customer desk.",
            address="Gopala Reddy Road, Governorpet, Vijayawada 520002"
        ),

        # Electronics & Gadgets
        Deal(
            place_name="Governorpet - NTR Complex", 
            category="Electronics", 
            title="NTR Complex Mobile Accessories Hub", 
            description="Screen guards, back covers, fast chargers, cables, and earphone repair kits.", 
            discount="Up to 40% OFF", 
            price=150.0,
            image_url="https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=600&q=80",
            terms="Warranty valid for 30 days on selected accessories against manufacturing defects.",
            address="Gopala Reddy Road, NTR Complex Market, Governorpet, Vijayawada 520002"
        ),
        Deal(
            place_name="Eluru Road, Governorpet", 
            category="Electronics", 
            title="Vijay Sales Electronics Festival", 
            description="Discounts on Smart TVs, ACs, Washing Machines, and Laptops.", 
            discount="Exchange Bonus", 
            price=8999.0,
            image_url="https://images.unsplash.com/photo-1526738549149-8e07eca6c147?w=600&q=80",
            terms="0% Interest EMI options available via major bank credit cards.",
            address="Eluru Road, Near Governorpet Junction, Vijayawada 520002"
        ),
        Deal(
            place_name="LEPL Centro Mall, MG Road", 
            category="Electronics", 
            title="Reliance Digital Laptops & Mobiles", 
            description="Latest 5G smartphones, gaming laptops, and wireless soundbars.", 
            discount="Instant Cashback", 
            price=12499.0,
            image_url="https://images.unsplash.com/photo-1498049794561-7780e7231661?w=600&q=80",
            terms="Includes official manufacturer warranty. Valid till end of month.",
            address="LEPL Centro Mall, MG Road, Vijayawada 520010"
        ),

        # Shopping Malls & Accessories
        Deal(
            place_name="Kaleswara Rao Market (Old City)", 
            category="Clothes", 
            title="Kaleswara Rao Wholesale Sarees & Fabrics", 
            description="Traditional Vijayawada cotton sarees, dress materials at wholesale prices.", 
            discount="Wholesale Rate", 
            price=350.0,
            image_url="https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?w=600&q=80",
            terms="Minimum purchase requirement for wholesale discount rates.",
            address="Kaleswara Rao Market, Tarapet, Old City, Vijayawada 520001"
        ),
        Deal(
            place_name="PVP Square Mall (MG Road)", 
            category="Clothes", 
            title="PVP Mall Branded Ethnic Wear", 
            description="Designer sarees, lehengas, and festival wear collections.", 
            discount="Flat 50% OFF", 
            price=1499.0,
            image_url="https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=600&q=80",
            terms="No returns on clearance items. Offer valid on select tags.",
            address="PVP Square Mall, MG Road, Vijayawada 520010"
        ),
        Deal(
            place_name="Trendset Mall (Benz Circle)", 
            category="Clothes", 
            title="Trendset Mall International Fashion Brands", 
            description="Casual shirts, denims, activewear, and party dresses.", 
            discount="Buy 1 Get 1", 
            price=1999.0,
            image_url="https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600&q=80",
            terms="Buy 1 Get 1 offer applicable on equal or lower value items.",
            address="Trendset Mall, Benz Circle, MG Road, Vijayawada 520010"
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

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        new_deal = Deal(
            place_name=request.form.get('place_name'),
            category=request.form.get('category'),
            title=request.form.get('title'),
            description=request.form.get('description'),
            discount=request.form.get('discount'),
            price=float(request.form.get('price', 0.0)),
            image_url=request.form.get('image_url', ''),
            terms=request.form.get('terms', 'Standard store terms apply.'),
            address=request.form.get('address', 'Vijayawada, AP')
        )
        db.session.add(new_deal)
        db.session.commit()
        return redirect(url_for('admin'))
    
    deals = Deal.query.all()
    return render_template('admin.html', deals=deals)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/offers', methods=['GET'])
def get_offers():
    category_filter = request.args.get('category')
    search_query = request.args.get('search')
    sort_order = request.args.get('sort')

    query = Deal.query
    if category_filter and category_filter != 'All':
        query = query.filter_by(category=category_filter)
    
    if search_query:
        query = query.filter(Deal.title.ilike(f"%{search_query}%") | Deal.place_name.ilike(f"%{search_query}%"))

    if sort_order == 'low_to_high':
        query = query.order_by(Deal.price.asc())
    elif sort_order == 'high_to_low':
        query = query.order_by(Deal.price.desc())

    deals = query.all()
    result = [{
        "id": d.id,
        "place_name": d.place_name,
        "category": d.category,
        "title": d.title,
        "description": d.description,
        "discount": d.discount,
        "price": d.price,
        "image_url": d.image_url or "https://images.unsplash.com/photo-1555529771-835f59fc5efe?w=500&q=80",
        "terms": d.terms or "Standard terms apply.",
        "address": d.address or "Vijayawada, Andhra Pradesh"
    } for d in deals]
    
    return jsonify({"status": "success", "data": result})

if __name__ == '__main__':
    app.run(debug=True)
