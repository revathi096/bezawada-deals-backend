from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'bezawada_secret_admin_key_2026' # సెషన్ సెక్యూరిటీ కోసం కీ

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
    if Deal.query.count() == 0:
        initial_deals = [
            Deal(
                place_name="PVP Square Mall (MG Road)", 
                category="Clothes", 
                title="PVP Mall Branded Ethnic Wear", 
                description="Designer sarees, lehengas, and festival wear collections.", 
                discount="Flat 50% OFF", 
                price=1499.0,
                image_url="https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=600&q=80",
                terms="Valid till stocks last at PVP Mall.",
                address="MG Road, Vijayawada, AP 520010"
            ),
            Deal(
                place_name="Governorpeta, Vijayawada", 
                category="Food", 
                title="Sai Charanam Aritaku Tiffins And Mess", 
                description="Traditional Andhra tiffins & banana leaf meals.", 
                discount="Budget Friendly", 
                price=90.0,
                image_url="https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=600&q=80",
                terms="Valid during lunch hours.",
                address="Governorpeta, Vijayawada, AP 520002"
            )
        ]
        db.session.bulk_save_objects(initial_deals)
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

# --- SECURE ADMIN LOGIN & DASHBOARD ROUTE ---
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # ఒకవేళ లాగిన్ అయి ఉంటే నేరుగా అడ్మిన్ పేజీకి పంపుతుంది
    if session.get('is_admin'):
        if request.method == 'POST':
            new_deal = Deal(
                place_name=request.form.get('place_name'),
                category=request.form.get('category'),
                title=request.form.get('title'),
                description=request.form.get('description'),
                discount=request.form.get('discount'),
                price=float(request.form.get('price', 0.0)),
                image_url=request.form.get('image_url') or "https://images.unsplash.com/photo-1555529771-835f59fc5efe?w=500&q=80",
                terms=request.form.get('terms') or "Standard store terms apply.",
                address=request.form.get('address') or "Vijayawada, Andhra Pradesh"
            )
            db.session.add(new_deal)
            db.session.commit()
            return redirect(url_for('admin'))
        
        deals = Deal.query.order_by(Deal.id.desc()).all()
        return render_template('admin.html', deals=deals)
    
    # ఒకవేళ లాగిన్ అవ్వకపోతే POST ద్వారా పాస్‌వర్డ్ చెక్ చేస్తుంది
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # ఇక్కడ మీ యూజర్‌నేమ్ మరియు పాస్‌వర్డ్ సెట్ చేసుకోండి (ఉదాహరణకు: revathi మరియు secure123)
        if username == 'revathi' and password == 'secure123':
            session['is_admin'] = True
            return redirect(url_for('admin'))
        else:
            error = "Invalid Username or Password! Access Denied."
            
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('is_admin', None)
    return redirect(url_for('admin'))

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
    else:
        query = query.order_by(Deal.id.desc())

    deals = query.all()
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
