from flask import Flask, jsonify, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bezawada_deals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(150), nullable=False)  # ఉదా: Ra Brothers, PVP Mall, Potti Sri Ramulu St, etc.
    category = db.Column(db.String(50), nullable=False)     # Food, Clothes, Accessories, Games, Daily Needs
    title = db.Column(db.String(250), nullable=False)       # ఆఫర్ లేదా ఐటమ్ పేరు
    description = db.Column(db.Text, nullable=True)         # అట్రాెక్టివ్ డిస్క్రిప్షన్
    discount = db.Column(db.String(50), nullable=False)    # 50% OFF, Flat Rs.100 etc.
    price = db.Column(db.Float, nullable=False, default=0.0) # ధర (Low to High సాటింగ్ కోసం)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return render_template_string(f.read())
    except Exception as e:
        return "BezawadaDeals Premium Platform is Live!"

@app.route('/api/offers', methods=['GET'])
def get_offers():
    category_filter = request.args.get('category')
    sort_order = request.args.get('sort')
    
    query = Deal.query
    if category_filter and category_filter != 'All':
        query = query.filter_by(category=category_filter)
        
    if sort_order == 'low_to_high':
        query = query.order_by(Deal.price.asc())
    elif sort_order == 'high_to_low':
        query = query.order_by(Deal.price.desc())
        
    deals = query.all()
    result = [
        {
            "id": d.id,
            "place_name": d.place_name,
            "category": d.category,
            "title": d.title,
            "description": d.description or "Best quality deal available now in Vijayawada.",
            "discount": d.discount,
            "price": d.price
        } for d in deals
    ]
    return jsonify({"status": "success", "data": result})

@app.route('/api/offers', methods=['POST'])
def add_offer():
    data = request.json
    if not data or 'place_name' not in data or 'title' not in data:
        return jsonify({"error": "Place name and title are required!"}), 400
        
    new_deal = Deal(
        place_name=data.get('place_name'),
        category=data.get('category', 'General'),
        title=data.get('title'),
        description=data.get('description', ''),
        discount=data.get('discount', 'Special Offer'),
        price=float(data.get('price', 0.0))
    )
    db.session.add(new_deal)
    db.session.commit()
    
    return jsonify({"status": "success", "message": "Deal added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)


    
