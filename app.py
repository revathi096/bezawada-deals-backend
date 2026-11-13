<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vijayawada Smart Needs - విజయవాడ స్మార్ట్ అవసరాలు</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-100 text-slate-800 font-sans">
    
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-3 flex justify-between items-center">
            <h1 class="text-xl font-bold text-blue-600">Vijayawada Smart Needs</h1>
            <nav class="space-x-4 text-sm font-medium">
                <a href="#" class="hover:text-blue-600">Home</a>
                <a href="#categories" class="hover:text-blue-600">Categories</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="bg-blue-700 text-white py-10 px-4 text-center">
        <h2 class="text-2xl md:text-3xl font-bold mb-2">విజయవాడలో మీకు కావాల్సిన ప్రతిదీ ఒకేచోట!</h2>
        <p class="text-blue-100 mb-6 text-sm">Shopping - Food - Daily Markets - Jobs - Services across 64 Wards</p>
        
        <div class="max-w-2xl mx-auto bg-white p-4 rounded-xl shadow-xl flex flex-col md:flex-row gap-3">
            <input type="text" id="searchInput" placeholder="Search Biryani, Tomatoes, Sarees, Jobs..." class="flex-1 px-4 py-3 text-slate-800 rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500">
            <select id="wardSelect" class="px-4 py-3 text-slate-800 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500">
                <option value="All 64 Wards">All 64 Wards</option>
                <option value="Benz Circle / Labbipet">Benz Circle / Labbipet</option>
                <option value="Governorpet / MG Road">Governorpet / MG Road</option>
                <option value="Patamata / Eluru Road">Patamata / Eluru Road</option>
                <option value="One Town / Besant Road">One Town / Besant Road</option>
                <option value="Suryaraopeta">Suryaraopeta</option>
            </select>
            <button onclick="handleSearch()" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-semibold shadow transition">Search</button>
        </div>
    </section>

    <!-- Categories Grid -->
    <section id="categories" class="max-w-6xl mx-auto px-4 py-8">
        <h3 class="text-xl font-bold mb-5 text-slate-800">Explore Categories (Select to View Prices)</h3>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
            
            <div onclick="selectCategory('Shopping')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">🛍️</div>
                <h4 class="font-semibold text-sm text-slate-700">Shopping</h4>
            </div>

            <div onclick="selectCategory('Restaurants')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">🍽️</div>
                <h4 class="font-semibold text-sm text-slate-700">Restaurants</h4>
            </div>

            <div onclick="selectCategory('Vegetables')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">🥬</div>
                <h4 class="font-semibold text-sm text-slate-700">Vegetables</h4>
            </div>

            <div onclick="selectCategory('Jobs')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">💼</div>
                <h4 class="font-semibold text-sm text-slate-700">Daily Jobs</h4>
            </div>

            <div onclick="selectCategory('Daily Needs')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">🛒</div>
                <h4 class="font-semibold text-sm text-slate-700">Daily Needs</h4>
            </div>

            <div onclick="selectCategory('Electronics')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">📱</div>
                <h4 class="font-semibold text-sm text-slate-700">Electronics</h4>
            </div>

        </div>
    </section>

    <!-- Results Display Section -->
    <section class="max-w-6xl mx-auto px-4 py-2 mb-12">
        <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <h3 id="resultTitle" class="text-lg font-bold text-blue-600 mb-4">Today's Featured Prices & Listings</h3>
            <div id="resultGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <!-- Cards will be dynamically inserted here -->
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-800 text-slate-400 text-center py-6 text-sm">
        <p>&copy; 2026 Vijayawada Smart Needs. Empowering Vijayawada Citizens.</p>
    </footer>

    <!-- Interactive Data & JavaScript -->
    <script>
        const catalogData = {
            "Shopping": [
                { name: "Kalamandir Pattu Sarees", location: "Patamata & MG Road", price: "Rs. 2,499 - 15,000", tag: "Festive 30% Off" },
                { name: "PVP Mall Branded Shirts", location: "MG Road", price: "Rs. 1,199 onwards", tag: "Buy 2 Get 1" },
                { name: "Besant Road Cotton Kurtis", location: "Governorpet", price: "Rs. 350 - 850", tag: "Wholesale Rate" }
            ],
            "Restaurants": [
                { name: "SS Special Chicken Dum Biryani", location: "Benz Circle", price: "Rs. 260 (Full)", tag: "Bestseller" },
                { name: "Ruchi Andhra Veg Meals", location: "Governorpet", price: "Rs. 140 / Plate", tag: "Fresh & Hot" },
                { name: "Sweet Magic Punugulu & Tiffins", location: "Labbipet", price: "Rs. 50 - 90", tag: "Evening Special" }
            ],
            "Vegetables": [
                { name: "Fresh Tomatoes", location: "Rythu Bazaar (Suryaraopeta)", price: "Rs. 28 / Kg", tag: "Today's Rate" },
                { name: "Onions", location: "Gollapudi Wholesale", price: "Rs. 35 / Kg", tag: "Fresh Stock" },
                { name: "Potatoes", location: "Patamata Market", price: "Rs. 32 / Kg", tag: "Grade A" },
                { name: "Green Chillies & Coriander", location: "All Ward Rythu Bazaars", price: "Rs. 45 / Kg", tag: "Daily Update" }
            ],
            "Jobs": [
                { name: "Delivery Partner (Swiggy / Zepto)", location: "Benz Circle & Patamata", price: "Rs. 750 - 1,100 / Day", tag: "Immediate Joining" },
                { name: "Retail Store Sales Helper", location: "MG Road & Besant Road", price: "Rs. 12,000 - 15,000 / Month", tag: "Full Time" },
                { name: "Construction & Mason Helpers", location: "Eluru Road", price: "Rs. 650 / Day", tag: "Daily Payment" }
            ],
            "Daily Needs": [
                { name: "Sona Masoori Rice (25 Kg Bag)", location: "All 64 Wards Delivery", price: "Rs. 1,350 / Bag", tag: "Free Delivery" },
                { name: "Farm Fresh Buffalo Milk", location: "Doorstep Delivery", price: "Rs. 72 / Liter", tag: "Morning 6 AM" },
                { name: "20L Mineral Water Can", location: "All Wards", price: "Rs. 25 / Can", tag: "ISI Certified" }
            ],
            "Electronics": [
                { name: "5G Smartphones (Starting Range)", location: "Murali Mobiles, Eluru Road", price: "Rs. 11,999 onwards", tag: "Exchange Bonus" },
                { name: "Smart LED TV (32 Inch)", location: "Reliance Digital, MG Road", price: "Rs. 13,490", tag: "1 Yr Warranty" },
                { name: "Ceiling Fans & Home Appliances", location: "Governorpet Electricals", price: "Rs. 1,450 onwards", tag: "Summer Offer" }
            ]
        };

        function renderCards(items) {
            const grid = document.getElementById('resultGrid');
            grid.innerHTML = items.map(item => `
                <div class="p-4 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:shadow transition flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-start mb-2">
                            <h4 class="font-bold text-slate-800 text-base">${item.name}</h4>
                            <span class="text-xs font-semibold bg-blue-100 text-blue-700 px-2 py-1 rounded-md">${item.tag}</span>
                        </div>
                        <p class="text-xs text-slate-500 mb-3">Location: ${item.location}</p>
                    </div>
                    <div class="pt-3 border-t border-slate-200 flex justify-between items-center">
                        <span class="text-xs text-slate-500 font-medium">Price / Rate:</span>
                        <span class="text-base font-bold text-green-600">${item.price}</span>
                    </div>
                </div>
            `).join('');
        }

        function selectCategory(categoryName) {
            const ward = document.getElementById('wardSelect').value;
            document.getElementById('resultTitle').innerText = `${categoryName} Listings & Prices (${ward})`;
            renderCards(catalogData[categoryName] || []);
        }

        function handleSearch() {
            const query = document.getElementById('searchInput').value.trim().toLowerCase();
            const ward = document.getElementById('wardSelect').value;

            if (!query) {
                alert("దయచేసి ఏదైనా ఐటమ్ పేరు టైప్ చేయండి (ఉదా: Biryani, Tomato, Sarees)");
                return;
            }

            let allItems = [];
            Object.values(catalogData).forEach(list => allItems.push(...list));

            const filtered = allItems.filter(item => 
                item.name.toLowerCase().includes(query) || 
                item.location.toLowerCase().includes(query)
            );

            document.getElementById('resultTitle').innerText = `Search Results for "${query}" in ${ward}`;

            if (filtered.length > 0) {
                renderCards(filtered);
            } else {
                document.getElementById('resultGrid').innerHTML = `
                    <div class="col-span-full p-4 bg-yellow-50 border border-yellow-200 rounded-lg text-sm text-yellow-800">
                        "${query}" కి సంబంధించిన ప్రత్యక్ష ధరలు ప్రస్తుతం లిస్ట్‌లో లేవు. కానీ విజయవాడలోని <strong>${ward}</strong> పరిధిలో అందుబాటులో ఉంది.
                    </div>
                `;
            }
        }

        window.onload = () => selectCategory('Vegetables');
    </script>
</body>
</html>
