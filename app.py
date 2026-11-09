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

with app.app_context():
    db.create_all()
    if Deal.query.count() == 0:
        sample_deals = [
            Deal(place_name="PVP Mall (MG Road)", category="Clothes", title="Branded Designer Sarees & Kurtis", description="Flat 50% off on top ethnic wear brands at PVP Mall.", discount="50% OFF", price=1499.0),
            Deal(place_name="Benz Circle Local Hub", category="Food", title="Special Bezawada Chicken Biryani Combo", description="Family pack biryani with starters at unbelievable budget price.", discount="Flat Rs.100 OFF", price=399.0),
            Deal(place_name="Eluru Road Fashion Store", category="Clothes", title="Men's Casual Shirts & Denims", description="Buy 1 Get 1 Free on all branded shirts near Eluru Road.", discount="Buy 1 Get 1", price=799.0),
            Deal(place_name="MG Road Electronics", category="Electronics", title="Smartwatches & Audio Gadgets", description="Best discount deals on smart accessories in heart of Vijayawada.", discount="30% OFF", price=1299.0),
            Deal(place_name="Governorpet Jewellers", category="Accessories", title="Silver & Fancy Jewellery Collections", description="Latest designer silver items starting from budget range.", discount="Special Deal", price=850.0)
        ]
        db.session.bulk_save_objects(sample_deals)
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
            price=float(request.form.get('price', 0.0))
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

    query = Deal.query
    if category_filter and category_filter != 'All':
        query = query.filter_by(category=category_filter)
    
    if search_query:
        query = query.filter(Deal.title.ilike(f"%{search_query}%") | Deal.place_name.ilike(f"%{search_query}%"))

    deals = query.all()
    result = [{
        "id": d.id,
        "place_name": d.place_name,
        "category": d.category,
        "title": d.title,
        "description": d.description,
        "discount": d.discount,
        "price": d.price
    } for d in deals]
    
    return jsonify({"status": "success", "data": result})

if __name__ == '__main__':
    app.run(debug=True)
