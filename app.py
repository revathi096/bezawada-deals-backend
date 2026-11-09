from flask import Flask, jsonify, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# SQLite డేటాబేస్ సెటప్
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bezawada_deals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# డేటాబేస్ టేబుల్ స్ట్రక్చర్ (మాల్స్ మరియు ఫుడ్ ఆఫర్స్ కోసం)
class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mall_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    discount = db.Column(db.String(50), nullable=False)

# అప్లికేషన్ స్టార్ట్ అయినప్పుడు డేటాబేస్ టేబుల్ క్రియేట్ అవుతుంది
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return render_template_string(f.read())
    except Exception as e:
        return "BezawadaDeals Database Backend is Live!"

# 1. అన్ని మాల్స్ & ఫుడ్ ఆఫర్లను చూడటానికి (GET API)
@app.route('/api/offers', methods=['GET'])
def get_offers():
    deals = Deal.query.all()
    result = [
        {
            "id": d.id,
            "mall_name": d.mall_name,
            "title": d.title,
            "discount": d.discount
        } for d in deals
    ]
    return jsonify({"status": "success", "data": result})

# 2. కొత్త మాల్ ఆఫర్‌ని ఆటోమేటిక్‌గా యాడ్ చేయడానికి (POST API)
@app.route('/api/offers', methods=['POST'])
def add_offer():
    data = request.json
    if not data or 'mall_name' not in data or 'title' not in data:
        return jsonify({"error": "Mall name and title are required!"}), 400
    
    new_deal = Deal(
        mall_name=data.get('mall_name'),
        title=data.get('title'),
        discount=data.get('discount', 'Special Offer')
    )
    db.session.add(new_deal)
    db.session.commit()
    
    return jsonify({
        "status": "success",
        "message": "Offer added successfully to database!",
        "data": {
            "id": new_deal.id,
            "mall_name": new_deal.mall_name,
            "title": new_deal.title,
            "discount": new_deal.discount
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True)

    
