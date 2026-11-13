<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vijayawada Smart Needs - Digital City Directory</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-100 text-slate-800 font-sans">

    <!-- Top Live Daily Rates Bar -->
    <div class="bg-slate-900 text-white text-xs py-2 px-4 overflow-x-auto whitespace-nowrap">
        <div class="max-w-7xl mx-auto flex justify-between items-center gap-6">
            <span class="font-bold text-amber-400">DAILY UPDATES (VIJAYAWADA):</span>
            <span>Gold (22K): Rs. 7,150/gm</span>
            <span>Petrol: Rs. 109.45/L</span>
            <span>Diesel: Rs. 97.30/L</span>
            <span>Tomato: Rs. 28/Kg</span>
            <span>Onion: Rs. 35/Kg</span>
            <span>Rice (25Kg): Rs. 1,350</span>
        </div>
    </div>

    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
            <div>
                <h1 class="text-xl md:text-2xl font-bold text-blue-700">Vijayawada Smart Needs</h1>
                <p class="text-[11px] text-slate-500">Complete Digital City Directory - All 64 Wards</p>
            </div>
            <div class="flex items-center gap-3">
                <a href="#categories" class="hidden md:inline text-sm font-medium hover:text-blue-600">Categories</a>
                <button onclick="openAddModal()" class="bg-green-600 hover:bg-green-700 text-white text-xs md:text-sm font-semibold px-3 py-2 rounded-lg shadow transition">
                    + Add Business
                </button>
            </div>
        </div>
    </header>

    <!-- Hero Search & Multi-Filter Section -->
    <section class="bg-gradient-to-r from-blue-800 to-blue-600 text-white py-10 px-4">
        <div class="max-w-5xl mx-auto text-center">
            <h2 class="text-2xl md:text-4xl font-bold mb-2">విజయవాడ నగరంలోని ప్రతి అవసరం, ప్రతి షాప్ ఒకేచోట!</h2>
            <p class="text-blue-100 text-xs md:text-sm mb-6">Search Clothes, Biryani, Malls, Daily Wages, Hospitals, Rentals, Plumbers & Daily Prices</p>

            <!-- Search & Filters Box -->
            <div class="bg-white p-4 rounded-2xl shadow-xl grid grid-cols-1 md:grid-cols-12 gap-3 text-slate-800">
                <div class="md:col-span-5">
                    <input type="text" id="searchInput" onkeyup="filterListings()" placeholder="Search Biryani, Sarees, Blood Bank, Plumber, Jobs..." class="w-full px-4 py-3 rounded-xl border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-blue-600">
                </div>
                <div class="md:col-span-3">
                    <select id="areaFilter" onchange="filterListings()" class="w-full px-3 py-3 rounded-xl border border-slate-300 text-sm bg-white focus:outline-none focus:ring-2 focus:ring-blue-600">
                        <option value="ALL">All Vijayawada (64 Wards)</option>
                        <option value="MG Road">MG Road / PVP Area</option>
                        <option value="Benz Circle">Benz Circle / Labbipet</option>
                        <option value="Governorpet">Governorpet / Besant Road</option>
                        <option value="Patamata">Patamata / Auto Nagar</option>
                        <option value="Eluru Road">Eluru Road / Gundala</option>
                        <option value="One Town">One Town / Kaleswara Rao Market</option>
                        <option value="Suryaraopeta">Suryaraopeta / Moghalrajpuram</option>
                    </select>
                </div>
                <div class="md:col-span-2">
                    <select id="budgetFilter" onchange="filterListings()" class="w-full px-3 py-3 rounded-xl border border-slate-300 text-sm bg-white focus:outline-none focus:ring-2 focus:ring-blue-600">
                        <option value="ALL">Any Budget</option>
                        <option value="Low">Low Budget</option>
                        <option value="Medium">Medium Budget</option>
                        <option value="High">High / Premium</option>
                    </select>
                </div>
                <div class="md:col-span-2">
                    <button onclick="filterListings()" class="w-full h-full bg-blue-700 hover:bg-blue-800 text-white font-bold py-3 rounded-xl text-sm transition shadow">
                        Search Now
                    </button>
                </div>
            </div>

            <!-- Quick Question Chips -->
            <div class="mt-4 flex flex-wrap justify-center gap-2 text-xs">
                <span class="text-blue-200 py-1">Quick Ask:</span>
                <button onclick="quickSearch('Biryani')" class="bg-blue-900/60 hover:bg-blue-900 px-3 py-1 rounded-full border border-blue-400/30">Best Biryani?</button>
                <button onclick="quickSearch('Clothes')" class="bg-blue-900/60 hover:bg-blue-900 px-3 py-1 rounded-full border border-blue-400/30">Low Price Clothes?</button>
                <button onclick="quickSearch('Jobs')" class="bg-blue-900/60 hover:bg-blue-900 px-3 py-1 rounded-full border border-blue-400/30">Daily Wage Jobs?</button>
                <button onclick="quickSearch('Hospital')" class="bg-blue-900/60 hover:bg-blue-900 px-3 py-1 rounded-full border border-blue-400/30">Hospital & Blood Bank?</button>
                <button onclick="quickSearch('Plumber')" class="bg-blue-900/60 hover:bg-blue-900 px-3 py-1 rounded-full border border-blue-400/30">Electrician / Plumber?</button>
            </div>
        </div>
    </section>

    <!-- Categories Section -->
    <section id="categories" class="max-w-7xl mx-auto px-4 py-8">
        <div class="flex justify-between items-center mb-4">
            <h3 class="text-lg md:text-xl font-bold text-slate-800">Browse City Categories</h3>
            <button onclick="selectCategory('ALL')" class="text-xs font-semibold text-blue-600 hover:underline">Show All Listings</button>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
            <div onclick="selectCategory('Shopping')" class="cat-card bg-white p-3 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 text-center transition">
                <div class="text-2xl mb-1">🛍️</div>
                <p class="text-xs font-bold text-slate-700">Shopping & Malls</p>
            </div>
            <div onclick="selectCategory('Restaurants')" class="cat-card bg-white p-3 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 text-center transition">
                <div class="text-2xl mb-1">🍽️</div>
                <p class="text-xs font-bold text-slate-700">Restaurants & Biryani</p>
            </div>
            <div onclick="selectCategory('Vegetables')" class="cat-card bg-white p-3 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 text-center transition">
                <div class="text-2xl mb-1">🥬</div>
                <p class="text-xs font-bold text-slate-700">Veg & Fruit Rates</p>
            </div>
            <div onclick="selectCategory('Grocery')" class="cat-card bg-white p-3 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 text-center transition">
                <div class="text-2xl mb-1">🛒</div>
                <p class="text-xs font-bold text-slate-700">Grocery & Offers</p>
            </div>
            <div onclick="selectCategory('Jobs')" class="cat-card bg-white p-3 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 text-center transition">
                <div class="text-2xl mb-1">💼</div>
                <p class="text-xs font-bold text-slate-700">Jobs & Daily Wages</p>
            </div>
            <div onclick="selectCategory('Services')" class="cat-card bg-white p-3 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 text-center transition">
                <div class="text-2xl mb-1">🔧</div>
                <p class="text-xs font-bold text-slate-700">Local Services</p>
            </div>
            <div onclick="selectCategory('Medical')" class="cat-card bg-white p-3 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 text-center transition">
                <div class="text-2xl mb-1">🏥</div>
                <p class="text-xs font-bold text-slate-700">Medical & Blood Bank</p>
            </div>
            <div onclick="selectCategory('Rentals')" class="cat-card bg-white p-3 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 text-center transition">
                <div class="text-2xl mb-1">🏠</div>
                <p class="text-xs font-bold text-slate-700">House Rentals</p>
            </div>
        </div>
    </section>

    <!-- Main Directory Listings Grid -->
    <section class="max-w-7xl mx-auto px-4 pb-16">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-4 gap-2">
            <h3 id="resultsHeading" class="text-lg font-bold text-slate-800">Showing All Vijayawada Listings</h3>
            <span id="resultCount" class="text-xs bg-blue-100 text-blue-800 font-semibold px-3 py-1 rounded-full">0 Results</span>
        </div>

        <div id="directoryGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            <!-- Dynamic Business Cards Render Here -->
        </div>
    </section>

    <!-- Add New Business Modal -->
    <div id="addModal" class="fixed inset-0 bg-black/60 hidden items-center justify-center z-50 p-4">
        <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-lg font-bold text-slate-800">Add Your Business / Service</h3>
                <button onclick="closeAddModal()" class="text-slate-400 hover:text-slate-700 font-bold text-xl">&times;</button>
            </div>
            <form onsubmit="submitNewBusiness(event)" class="space-y-3 text-sm">
                <div>
                    <label class="block font-semibold mb-1">Shop / Service / Job Name</label>
                    <input type="text" id="newTitle" required placeholder="e.g., Sri Sai Electricals" class="w-full border border-slate-300 rounded-lg px-3 py-2">
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block font-semibold mb-1">Category</label>
                        <select id="newCategory" class="w-full border border-slate-300 rounded-lg px-3 py-2">
                            <option value="Shopping">Shopping</option>
                            <option value="Restaurants">Restaurants</option>
                            <option value="Vegetables">Vegetables & Fruits</option>
                            <option value="Grocery">Grocery</option>
                            <option value="Jobs">Jobs & Daily Wages</option>
                            <option value="Services">Local Services</option>
                            <option value="Medical">Medical & Hospitals</option>
                            <option value="Rentals">House Rentals</option>
                        </select>
                    </div>
                    <div>
                        <label class="block font-semibold mb-1">Budget Level</label>
                        <select id="newBudget" class="w-full border border-slate-300 rounded-lg px-3 py-2">
                            <option value="Low">Low</option>
                            <option value="Medium">Medium</option>
                            <option value="High">High</option>
                        </select>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block font-semibold mb-1">Area / Ward</label>
                        <input type="text" id="newArea" required placeholder="e.g., Benz Circle" class="w-full border border-slate-300 rounded-lg px-3 py-2">
                    </div>
                    <div>
                        <label class="block font-semibold mb-1">Price / Wage / Rent</label>
                        <input type="text" id="newPrice" required placeholder="e.g., Rs. 300 onwards" class="w-full border border-slate-300 rounded-lg px-3 py-2">
                    </div>
                </div>
                <div>
                    <label class="block font-semibold mb-1">WhatsApp Phone Number</label>
                    <input type="tel" id="newPhone" required placeholder="e.g., 919848012345" class="w-full border border-slate-300 rounded-lg px-3 py-2">
                </div>
                <div>
                    <label class="block font-semibold mb-1">Details / Offers</label>
                    <textarea id="newDesc" rows="2" required placeholder="Short details about items, timing or offers..." class="w-full border border-slate-300 rounded-lg px-3 py-2"></textarea>
                </div>
                <button type="submit" class="w-full bg-blue-700 hover:bg-blue-800 text-white font-bold py-2.5 rounded-xl transition">Submit Listing</button>
            </form>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-8 px-4 text-center text-xs">
        <p class="text-white font-bold text-sm mb-1">Vijayawada Smart Needs - Digital City Directory</p>
        <p class="mb-3">Connecting All 64 Wards: Shopping, Food, Daily Markets, Jobs, Hospitals & Rentals.</p>
        <p>&copy; 2026 Bezawada Deals & Smart Needs. All Rights Reserved.</p>
    </footer>

    <!-- Master City Database & Logic -->
    <script>
        let selectedCat = 'ALL';

        const cityDirectory = [
            // Shopping & Malls
            { title: "Besant Road Wholesale & Retail Clothes", category: "Shopping", area: "Governorpet", budget: "Low", price: "Rs. 199 - Rs. 799", phone: "919848011111", desc: "Best place in Vijayawada for low budget clothes, kids wear, kurtis and daily sarees.", keywords: "clothes battalu low price cheap shopping dress" },
            { title: "PVP Square Shopping Mall", category: "Shopping", area: "MG Road", budget: "High", price: "Rs. 999 onwards", phone: "919848022222", desc: "Top shopping mall with Lifestyle, Max, Pantaloons, multiplex cinemas & food court.", keywords: "shopping malls pvp multiplex brands" },
            { title: "Trendset Mall & Big Bazaar", category: "Shopping", area: "Benz Circle", budget: "Medium", price: "Rs. 499 - Rs. 3,500", phone: "919848033333", desc: "Shopping mall with branded fashion stores, gaming zone and family entertainment.", keywords: "shopping malls trendset benz circle" },
            { title: "Kalamandir & KLM Fashion Mall", category: "Shopping", area: "Patamata", budget: "Medium", price: "Rs. 599 - Rs. 15,000", phone: "919848044444", desc: "Wedding pattu sarees, mens ethnic wear and festive discount offers.", keywords: "sarees clothes shopping kalamandir klm" },

            // Restaurants & Hotels
            { title: "SS Hyderabadi Dum Biryani", category: "Restaurants", area: "Benz Circle", budget: "Medium", price: "Rs. 260 (Full)", phone: "919848055555", desc: "Famous for authentic spicy chicken & mutton dum biryani with family pack combos.", keywords: "biryani hotel restaurant food lunch dinner" },
            { title: "Ruchi Andhra Mess & Meals", category: "Restaurants", area: "Governorpet", budget: "Low", price: "Rs. 120 / Full Meals", phone: "919848066666", desc: "Homely unlimited Andhra vegetarian meals, curries, pappu and fresh tiffins.", keywords: "meals food hotel tiffins low budget" },
            { title: "Babai Hotel Original Tiffins", category: "Restaurants", area: "Governorpet", budget: "Low", price: "Rs. 50 - Rs. 90", phone: "919848077777", desc: "Iconic Vijayawada breakfast spot famous for idli with butter and upma pesarattu.", keywords: "tiffin idli dosa breakfast hotel" },
            { title: "DV Manor Multi-Cuisine Restaurant", category: "Restaurants", area: "MG Road", budget: "High", price: "Rs. 600 - Rs. 1,500", phone: "919848088888", desc: "Luxury 4-star dining, buffet lunch, North Indian and Continental dishes.", keywords: "luxury hotel buffet restaurant biryani" },

            // Vegetables & Fruits
            { title: "Suryaraopeta Rythu Bazaar", category: "Vegetables", area: "Suryaraopeta", budget: "Low", price: "Tomato Rs.28/Kg | Onion Rs.35/Kg", phone: "919848099999", desc: "Direct farmers market with government fixed low rates for fresh vegetables & leafy greens.", keywords: "vegetables kooragayalu tomato onion low price rythu bazaar" },
            { title: "Kaleswara Rao Wholesale Fruit & Veg Market", category: "Vegetables", area: "One Town", budget: "Low", price: "Wholesale Bulk Rates", phone: "919848010101", desc: "Biggest wholesale market in Vijayawada for bananas, mangoes, apples and bulk vegetables.", keywords: "fruits vegetables wholesale market one town" },
            { title: "Patamata Rythu Bazaar", category: "Vegetables", area: "Patamata", budget: "Low", price: "Potato Rs.32/Kg | Chilli Rs.45/Kg", phone: "919848012121", desc: "Morning 6 AM to 8 PM fresh vegetables at lowest rates for Patamata & Auto Nagar residents.", keywords: "vegetables market patamata low price" },

            // Grocery & Supermarkets
            { title: "D-Mart Supermarket Offers", category: "Grocery", area: "Patamata", budget: "Low", price: "Min 10% to 50% Off on MRP", phone: "919848013131", desc: "Lowest prices on Sona Masoori rice (Rs.1350/25kg), cooking oils, pulses & household items.", keywords: "supermarket offers grocery dmart rice oil" },
            { title: "Ratnadeep & Vijetha Supermarket", category: "Grocery", area: "Benz Circle", budget: "Medium", price: "Buy 1 Get 1 Weekend Offers", phone: "919848014141", desc: "Fresh groceries, bakery items, dairy products and home delivery across nearby wards.", keywords: "supermarket offers vijetha ratnadeep grocery" },

            // Jobs & Daily Wages
            { title: "Auto Nagar & Benz Circle Daily Wage Labour Adda", category: "Jobs", area: "Patamata", budget: "Low", price: "Rs. 650 - Rs. 850 / Day", phone: "919848015151", desc: "Daily construction helpers, loading/unloading workers, painters & civil work openings.", keywords: "daily wages coolie pani jobs construction" },
            { title: "Swiggy, Zomato & Zepto Delivery Partners", category: "Jobs", area: "MG Road", budget: "Medium", price: "Rs. 800 - Rs. 1,200 / Day", phone: "919848016161", desc: "Immediate joining with bike or cycle. Weekly payouts + fuel incentives across all 64 wards.", keywords: "jobs delivery boy part time daily income" },
            { title: "Showroom Sales & Office Helpers", category: "Jobs", area: "Eluru Road", budget: "Medium", price: "Rs. 12,000 - Rs. 16,000 / Month", phone: "919848017171", desc: "10th/Inter pass candidates needed for textile & electronics showrooms in Eluru Road.", keywords: "jobs showroom sales office work" },

            // Local Services (Electrician, Plumber, Carpenter)
            { title: "24/7 Vijayawada Electrician & Plumber Service", category: "Services", area: "Benz Circle", budget: "Low", price: "Rs. 200 Visiting Charge", phone: "919848018181", desc: "Fast home repair for wiring, fan/motor repair, tap leakage, pipe fitting & water tank cleaning.", keywords: "electrician plumber repair service home" },
            { title: "Sri Durga Wood Works & Carpenter", category: "Services", area: "Eluru Road", budget: "Medium", price: "Rs. 350 onwards", phone: "919848019191", desc: "Door locks, cupboard repairs, modular kitchen fitting and furniture polishing.", keywords: "carpenter wood work furniture repair" },
            { title: "CoolTech AC & Refrigerator Service", category: "Services", area: "Suryaraopeta", budget: "Medium", price: "Rs. 399 AC Jet Service", phone: "919848020202", desc: "AC gas filling, installation, washing machine and fridge doorstep repair.", keywords: "ac repair electronics service fridge" },

            // Medical, Hospitals & Blood Bank
            { title: "Government General Hospital (GGH) & Blood Bank", category: "Medical", area: "Eluru Road", budget: "Low", price: "Free Treatment / 24x7 Blood Bank", phone: "918662578000", desc: "24/7 emergency trauma care, free medicines, diagnostics and government blood bank.", keywords: "hospital blood bank emergency free medical" },
            { title: "Red Cross Blood Bank & Diagnostics", category: "Medical", area: "Governorpet", budget: "Low", price: "24/7 All Blood Groups Available", phone: "918662571234", desc: "Indian Red Cross Society blood bank, platelets availability and affordable lab tests.", keywords: "blood bank medical test lab" },
            { title: "Aayush & Andhra Multi-Specialty Hospitals", category: "Medical", area: "Suryaraopeta", budget: "High", price: "OP Consultation: Rs. 400 - 500", phone: "918662435555", desc: "24/7 emergency ICU, cardiology, orthopedic and Aarogyasri / insurance accepted.", keywords: "hospital medical emergency doctor" },
            { title: "MedPlus & Apollo 24/7 Pharmacy", category: "Medical", area: "Benz Circle", budget: "Low", price: "Up to 20% Discount on Medicines", phone: "919848021212", desc: "All generic and branded medicines available round the clock with home delivery.", keywords: "medical shop pharmacy medicines" },

            // House Rentals
            { title: "1BHK & 2BHK Family Portions for Rent", category: "Rentals", area: "Patamata", budget: "Medium", price: "Rs. 6,500 - Rs. 11,000 / Month", phone: "919848023232", desc: "24 hours water supply, bike parking, walkable distance to bus stop and schools.", keywords: "house rent 1bhk 2bhk portion" },
            { title: "Single Rooms & Working Women/Men Hostels", category: "Rentals", area: "Benz Circle", budget: "Low", price: "Rs. 4,500 / Month (With Food)", phone: "919848024242", desc: "WiFi, homely food, washing machine and safe accommodation near coaching centers.", keywords: "room rent hostel pg low budget" }
        ];

        function renderListings(list) {
            const grid = document.getElementById('directoryGrid');
            const countBadge = document.getElementById('resultCount');
            countBadge.innerText = `${list.length} Results Found`;

            if (list.length === 0) {
                grid.innerHTML = `
                    <div class="col-span-full bg-white p-8 rounded-2xl text-center border border-slate-200">
                        <p class="text-slate-600 font-semibold mb-2">No exact match found for your filter.</p>
                        <button onclick="resetAll()" class="bg-blue-600 text-white text-xs px-4 py-2 rounded-lg">Reset All Filters</button>
                    </div>`;
                return;
            }

            grid.innerHTML = list.map(item => {
                const mapsUrl = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(item.title + ' ' + item.area + ' Vijayawada')}`;
                const waText = encodeURIComponent(`Hello, I found "${item.title}" on Vijayawada Smart Needs. Please share more details.`);
                const waUrl = `https://wa.me/${item.phone}?text=${waText}`;

                let budgetColor = "bg-green-100 text-green-800";
                if(item.budget === "Medium") budgetColor = "bg-amber-100 text-amber-800";
                if(item.budget === "High") budgetColor = "bg-purple-100 text-purple-800";

                return `
                <div class="bg-white rounded-2xl p-5 shadow-sm hover:shadow-md border border-slate-200 flex flex-col justify-between transition">
                    <div>
                        <div class="flex justify-between items-start gap-2 mb-2">
                            <span class="text-[11px] font-bold uppercase tracking-wide text-blue-700 bg-blue-50 px-2.5 py-1 rounded-md">${item.category}</span>
                            <span class="text-[11px] font-semibold px-2.5 py-1 rounded-md ${budgetColor}">${item.budget} Budget</span>
                        </div>
                        <h4 class="text-base font-bold text-slate-900 mb-1">${item.title}</h4>
                        <p class="text-xs font-medium text-slate-500 mb-2">📍 ${item.area}, Vijayawada</p>
                        <p class="text-xs text-slate-600 leading-relaxed mb-4">${item.desc}</p>
                    </div>
                    <div>
                        <div class="bg-slate-50 px-3 py-2 rounded-lg border border-slate-100 mb-3 flex justify-between items-center">
                            <span class="text-xs text-slate-500">Rate / Price:</span>
                            <span class="text-sm font-bold text-green-700">${item.price}</span>
                        </div>
                        <div class="grid grid-cols-2 gap-2">
                            <a href="${mapsUrl}" target="_blank" class="text-center bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-semibold py-2.5 rounded-xl transition">
                                🗺️ Google Maps
                            </a>
                            <a href="${waUrl}" target="_blank" class="text-center bg-green-600 hover:bg-green-700 text-white text-xs font-semibold py-2.5 rounded-xl transition">
                                💬 WhatsApp
                            </a>
                        </div>
                    </div>
                </div>`;
            }).join('');
        }

        function filterListings() {
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            const area = document.getElementById('areaFilter').value;
            const budget = document.getElementById('budgetFilter').value;

            const filtered = cityDirectory.filter(item => {
                const matchCat = (selectedCat === 'ALL') || (item.category === selectedCat);
                const matchArea = (area === 'ALL') || (item.area.toLowerCase().includes(area.toLowerCase()));
                const matchBudget = (budget === 'ALL') || (item.budget === budget);
                const matchQuery = !query || 
                    item.title.toLowerCase().includes(query) || 
                    item.desc.toLowerCase().includes(query) || 
                    item.area.toLowerCase().includes(query) ||
                    item.category.toLowerCase().includes(query) ||
                    (item.keywords && item.keywords.toLowerCase().includes(query));

                return matchCat && matchArea && matchBudget && matchQuery;
            });

            document.getElementById('resultsHeading').innerText = 
                selectedCat === 'ALL' ? 'Vijayawada City Directory Results' : `${selectedCat} in Vijayawada`;
            renderListings(filtered);
        }

        function selectCategory(cat) {
            selectedCat = cat;
            filterListings();
            document.getElementById('directoryGrid').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }

        function quickSearch(term) {
            selectedCat = 'ALL';
            document.getElementById('searchInput').value = term;
            document.getElementById('areaFilter').value = 'ALL';
            document.getElementById('budgetFilter').value = 'ALL';
            filterListings();
        }

        function resetAll() {
            selectedCat = 'ALL';
            document.getElementById('searchInput').value = '';
            document.getElementById('areaFilter').value = 'ALL';
            document.getElementById('budgetFilter').value = 'ALL';
            filterListings();
        }

        // Modal Functions
        function openAddModal() {
            document.getElementById('addModal').classList.remove('hidden');
            document.getElementById('addModal').classList.add('flex');
        }
        function closeAddModal() {
            document.getElementById('addModal').classList.add('hidden');
            document.getElementById('addModal').classList.remove('flex');
        }

        function submitNewBusiness(e) {
            e.preventDefault();
            const newEntry = {
                title: document.getElementById('newTitle').value,
                category: document.getElementById('newCategory').value,
                budget: document.getElementById('newBudget').value,
                area: document.getElementById('newArea').value,
                price: document.getElementById('newPrice').value,
                phone: document.getElementById('newPhone').value.replace(/\D/g, ''),
                desc: document.getElementById('newDesc').value,
                keywords: document.getElementById('newTitle').value.toLowerCase()
            };
            cityDirectory.unshift(newEntry);
            closeAddModal();
            e.target.reset();
            resetAll();
            alert("మీ Business / Service విజయవంతంగా Vijayawada Smart Needs డైరెక్టరీలో యాడ్ చేయబడింది!");
        }

        // Initial Load
        window.onload = () => renderListings(cityDirectory);
    </script>
</body>
</html>
