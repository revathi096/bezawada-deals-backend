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
    if Deal.query.count() < 10:
        initial_deals = [
            # PVP Mall Multiple Offers
            Deal(
                place_name="PVP Mall", 
                category="Clothes", 
                title="PVP Mall Designer Ethnic Saree Sale", 
                description="Designer sarees, lehengas, and festival wear collections starting at flat rates.", 
                discount="Flat 50% OFF", 
                price=1499.0,
                image_url="https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=600&q=80",
                terms="Valid till stocks last at PVP Mall 2nd Floor.",
                address="MG Road, Vijayawada, AP 520010"
            ),
            Deal(
                place_name="PVP Mall", 
                category="Clothes", 
                title="PVP Mall Branded Western & Casual Wear", 
                description="Trendy shirts, jeans, and party wear outfits from top international brands.", 
                discount="Buy 1 Get 1 Free", 
                price=999.0,
                image_url="https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600&q=80",
                terms="Valid on select clothing brands inside PVP Square Mall.",
                address="MG Road, Vijayawada, AP 520010"
            ),
            Deal(
                place_name="PVP Mall", 
                category="Food", 
                title="PVP Mall Food Court Family Combo", 
                description="Delicious burgers, cheesy pizzas, French fries, and cool beverages combo pack.", 
                discount="20% OFF", 
                price=399.0,
                image_url="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&q=80",
                terms="Valid on weekdays at PVP Mall 3rd Floor Food Court.",
                address="3rd Floor Food Court, PVP Square, Vijayawada"
            ),

            # Kalamandir Offers
            Deal(
                place_name="Kalamandir", 
                category="Clothes", 
                title="Kalamandir Kanchi Pattu Sarees Mega Offer", 
                description="Pure silk sarees, bridal wear, and festival sarees ranging from ₹499 to ₹5000+.", 
                discount="Up to 40% OFF", 
                price=499.0,
                image_url="https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=600&q=80",
                terms="Special festival gift voucher on purchases above ₹2000.",
                address="MG Road, Near Benz Circle, Vijayawada"
            ),

            # Trendset Mall Offers
            Deal(
                place_name="Trendset Mall", 
                category="Clothes", 
                title="Trendset Mall Branded Footwear Festival", 
                description="Top sneaker and footwear collections special clearance discount sale.", 
                discount="Flat 40% OFF", 
                price=899.0,
                image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&q=80",
                terms="Offer valid till stocks last at Benz Circle Trendset Mall.",
                address="Benz Circle, MG Road, Vijayawada"
            ),

            # Food & Mess Offers
            Deal(
                place_name="Sai Charanam Mess", 
                category="Food", 
                title="Sai Charanam Traditional Banana Leaf Meals", 
                description="Authentic Andhra unlimited meals served with hot rice, dal, curries, and ghee.", 
                discount="Budget Friendly", 
                price=90.0,
                image_url="https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?w=600&q=80",
                terms="Lunch time only (12 PM to 3:30 PM).",
                address="Near Santhi Theatre, Governorpet, Vijayawada"
            ),
            Deal(
                place_name="040 Biryani", 
                category="Food", 
                title="040 Biryani Special Family Combo", 
                description="Spicy Hyderabadi and Bezawada style chicken dum biryani with starters.", 
                discount="15% OFF", 
                price=299.0,
                image_url="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&q=80",
                terms="Applicable on dine-in and takeaway.",
                address="Gandhi Nagar, Vijayawada"
            ),

            # Supermarkets
            Deal(
                place_name="DMart", 
                category="Supermarkets", 
                title="DMart Hypermarket Monthly Grocery Pack", 
                description="Rice, pulses, cooking oils, and home cleaning essentials at wholesale prices.", 
                discount="Wholesale Rates", 
                price=199.0,
                image_url="https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&q=80",
                terms="Prices subject to daily stock availability.",
                address="Bavajipet, Samba Murthy Road, Vijayawada"
            ),

            # Electronics
            Deal(
                place_name="NTR Complex", 
                category="Electronics", 
                title="NTR Complex Mobile Accessories & Repair Kit", 
                description="Screen guards, back covers, fast chargers, and earphone kits.", 
                discount="Up to 40% OFF", 
                price=150.0,
                image_url="https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=600&q=80",
                terms="30 days replacement warranty.",
                address="Gopala Reddy Road, Governorpet, Vijayawada"
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
                    success_msg = "Admin password updated successfully!"
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
                    address=request.form.get('address') or "Vijayawada, Andhra Pradesh"
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
    
    if search_query and search_query != 'All':
        query = query.filter(
            Deal.title.ilike(f"%{search_query}%") | 
            Deal.place_name.ilike(f"%{search_query}%") |
            Deal.description.ilike(f"%{search_query}%")
        )

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
    
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from supabase import create_client
import pandas as pd
import os

app = FastAPI(title="Vijayawada AI Platform Backend")

# CORS సెటప్ (ఫ్రంట్ ఎండ్ కనెక్ట్ అవ్వడానికి)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ఎన్విరాన్మెంట్ వేరియబుల్స్ నుండి కీస్ తీసుకోవడం
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
supabase = create_client(SUPABASE_URL, SUPABASE_KEY) if (SUPABASE_URL and SUPABASE_KEY) else None

class ChatRequest(BaseModel):
    message: str
    language: str = "Telugu"  # Telugu, English, Hindi
    mode: str = "local_info"  # local_info, code_assistant, data_analysis
    session_id: str = "default-session"

@app.get("/")
def home():
    return {"status": "Vijayawada AI Platform Backend is running successfully!"}

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    if not client:
        raise HTTPException(status_code=500, OpenAI="OpenAI API key is not configured.")
        
    context = ""
    
    # 1. విజయవాడ లోకల్ సమాచారం కోసం వెక్టర్ సెర్చ్ (Supabase ఉంటే)
    if req.mode == "local_info" and supabase:
        try:
            emb_response = client.embeddings.create(
                input=req.message,
                model="text-embedding-3-small"
            )
            query_vector = emb_response.data[0].embedding
            
            # Supabase RPC కాల్
            matches = supabase.rpc("match_vijayawada_info", {
                "query_embedding": query_vector,
                "match_threshold": 0.5,
                "match_count": 5
            }).execute()
            
            if matches.data:
                context = "\n".join([item.get('details', '') for item in matches.data])
        except Exception as e:
            print(f"Vector search warning: {e}")

    # 2. మోడ్ ప్రకారం ప్రాంప్ట్స్ సెట్ చేయడం
    system_prompts = {
        "local_info": f"""నీవు విజయవాడ (Vijayawada) ఆల్-ఇన్-వన్ లోకల్ గైడ్ AI. 
        యూజర్ అడిగే ప్రశ్నలకు (షాప్స్, ఫుడ్, బట్టలు, రోజువారీ కూలీ పనులు, సర్వీసులు మొదలైనవి) {req.language} భాషలో ఖచ్చితమైన సమాచారం ఇవ్వు.
        స్థానిక సమాచారం (Context): {context}""",
        
        "code_assistant": f"You are an expert Coding Assistant. Provide clear explanations and clean code snippets in {req.language}.",
        
        "data_analysis": f"You are an expert Data Analyst. Explain data insights clearly and simply in {req.language}."
    }

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompts.get(req.mode, system_prompts["local_info"])},
                {"role": "user", "content": req.message}
            ]
        )
        ai_reply = response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # 3. Supabase లో చాట్ హిస్టరీ సేవ్ చేయడం (అందుబాటులో ఉంటే)
    if supabase:
        try:
            supabase.table("chat_messages").insert([
                {"session_id": req.session_id, "role": "user", "content": req.message, "mode": req.mode},
                {"session_id": req.session_id, "role": "assistant", "content": ai_reply, "mode": req.mode}
            ]).execute()
        except Exception as e:
            print(f"Chat save warning: {e}")

    return {"reply": ai_reply}

# Data Analysis కోసం CSV/Excel ఫైల్ అప్‌లోడ్ API
@app.post("/analyze-data")
async def analyze_data(file: UploadFile = File(...), question: str = "Summarize this data"):
    try:
        df = pd.read_csv(file.file)
        summary = df.describe().to_string()
        
        if not client:
            return {"analysis": f"Dataset Summary:\n{summary}"}
            
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Analyze this dataset summary and give useful business insights."},
                {"role": "user", "content": f"Data Summary:\n{summary}\n\nUser Question: {question}"}
            ]
        )
        return {"analysis": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing file: {str(e)}")
        
