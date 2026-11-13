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
            <h1 class="text-xl font-bold text-blue-600"> Vijayawada Smart Needs</h1>
            <nav class="space-x-3 text-sm font-medium">
                <a href="#" class="hover:text-blue-600">Home</a>
                <a href="#categories" class="hover:text-blue-600">Categories</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section with Clear Search Bar -->
    <section class="bg-blue-700 text-white py-10 px-4 text-center">
        <h2 class="text-2xl md:text-3xl font-bold mb-2">విజయవాడలో మీకు కావాల్సిన ప్రతిదీ ఒకేచోట!</h2>
        <p class="text-blue-100 mb-6 text-sm">Shopping • Food • Daily Markets • Jobs • Services across 64 Wards</p>
        
        <!-- Search & Filter Box -->
        <div class="max-w-2xl mx-auto bg-white p-4 rounded-xl shadow-xl flex flex-col md:flex-row gap-3">
            <input type="text" id="searchInput" placeholder="Search PVP Mall, Benz Circle, Vegetables..." class="flex-1 px-4 py-3 text-slate-800 rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500">
            <select id="wardSelect" class="px-4 py-3 text-slate-800 rounded-lg border border-slate-300 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500">
                <option value="All Wards">All 64 Wards</option>
                <option value="Benz Circle / Labbipet">Benz Circle / Labbipet</option>
                <option value="Governorpet / MG Road">Governorpet / MG Road</option>
                <option value="Patamata / Eluru Road">Patamata / Eluru Road</option>
                <option value="One Town / Besant Road">One Town / Besant Road</option>
                <option value="Suryaraopeta">Suryaraopeta</option>
            </select>
            <button onclick="handleSearch()" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-semibold shadow transition">Search</button>
        </div>
    </section>

    <!-- Categories Section -->
    <section id="categories" class="max-w-6xl mx-auto px-4 py-8">
        <h3 class="text-xl font-bold mb-5 text-slate-800">Explore Categories</h3>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
            
            <div onclick="selectCategory('Shopping')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">🛍️</div>
                <h4 class="font-semibold text-sm text-slate-700">Shopping</h4>
            </div>

            <div onclick="selectCategory('Restaurants')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">🍽️</div>
                <h4 class="font-semibold text-sm text-slate-700">Restaurants</h4>
            </div>

            <div onclick="selectCategory('Vegetables & Markets')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">🥬</div>
                <h4 class="font-semibold text-sm text-slate-700">Vegetables</h4>
            </div>

            <div onclick="selectCategory('Daily Wage Jobs')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md cursor-pointer border border-slate-200 transition text-center">
                <div class="text-3xl mb-2">💼</div>
                <h4 class="font-semibold text-sm text-slate-700">Jobs</h4>
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
    <section class="max-w-6xl mx-auto px-4 py-4 mb-12">
        <div id="resultsContainer" class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <h3 id="resultTitle" class="text-lg font-bold text-blue-600 mb-3">Welcome to Vijayawada Smart Needs</h3>
            <p id="resultContent" class="text-slate-600 text-sm leading-relaxed">
                దయచేసి పైన ఉన్న కేటగిరీలను క్లిక్ చేయండి లేదా మీకు కావలసిన షాప్/మార్కెట్ పేరును సెర్చ్ చేయండి. విజయవాడలోని అన్ని ప్రముఖ మాల్స్, రెస్టారెంట్లు, కూరగాయల మార్కెట్లు మరియు డైలీ వేజ్ ఉద్యోగాల సమాచారం ఇక్కడ లభిస్తుంది.
            </p>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-800 text-slate-400 text-center py-6 text-sm">
        <p>&copy; 2026 Vijayawada Smart Needs. Empowering Vijayawada Citizens.</p>
    </footer>

    <!-- Interactive JavaScript -->
    <script>
        const database = {
            "Shopping": "🛍️ **Vijayawada Shopping Hubs:**\n• **PVP Mall (MG Road):** Open 10 AM - 10 PM. Top brands, clothing, and multiplex cinemas with festive discounts up to 50%.\n• **Trendz & Kalamandir (Patamata):** Best ethnic wear and traditional silk sarees.\n• **Besant Road & Eluru Road:** Wholesale textile markets and footwear stores.",
            "Restaurants": "🍽️ **Top Dining & Food Spots:**\n• **SS Biryani (Benz Circle):** Famous for Hyderabadi Dum Biryani.\n• **Ruchi Restaurant (Governorpet):** Traditional Andhra meals and tiffins.\n• **Sweet Magic (Labbipet):** Sweets, snacks, and family restaurant.",
            "Vegetables & Markets": "🥬 **Fresh Vegetable Markets & Daily Prices:**\n• **Rythu Bazaar (Suryaraopeta & Patamata):** Direct farm-to-table fresh vegetables at government-regulated prices.\n• **Gollapudi Wholesale Market:** Bulk vegetable and fruit trading hub for Vijayawada.",
            "Daily Wage Jobs": "💼 **Available Jobs & Local Work:**\n• **Construction & Helpers:** Daily openings around Benz Circle and Eluru Road (Contact local contractors).\n• **Delivery Executives:** Zepto, Blinkit, and Swiggy hiring active delivery partners in all wards.\n• **Store Assistants:** Retail shops in MG Road looking for immediate helpers.",
            "Daily Needs": "🛒 **Daily Essentials & Wards Supply:**\n• Milk delivery, groceries, and household water supplies active across all 64 municipal divisions in Vijayawada.",
            "Electronics": "📱 **Mobile & Electronics Showrooms:**\n• **Murali Mobiles (Eluru Road):** Best prices on smartphones and accessories.\n• **Reliance Digital (MG Road):** Home appliances, laptops, and exchange offers."
        };

        function selectCategory(categoryName) {
            const title = document.getElementById('resultTitle');
            const content = document.getElementById('resultContent');
            const ward = document.getElementById('wardSelect').value;

            title.innerText = `Category: ${categoryName} (Area: ${ward})`;
            content.innerHTML = (database[categoryName] || "సమాచారం అందుబాటులో ఉంది.").replace(/\n/g, '<br>');
        }

        function handleSearch() {
            const query = document.getElementById('searchInput').value.trim();
            const ward = document.getElementById('wardSelect').value;
            const title = document.getElementById('resultTitle');
            const content = document.getElementById('resultContent');

            if(!query) {
                alert("దయచేసి సెర్చ్ బార్‌లో ఏదైనా టైప్ చేయండి (ఉదా: PVP Mall)");
                return;
            }

            title.innerText = `Search Results for "${query}" in ${ward}`;
            content.innerHTML = `🔍 **Search Match Found:** విజయవాడలోని <strong>${ward}</strong> ప్రాంతంలో <strong>${query}</strong> కి సంబంధించిన స్టోర్స్, కాంటాక్ట్ నంబర్లు మరియు ప్రత్యక్ష ఆఫర్లు అందుబాటులో ఉన్నాయి. త్వరలో మరిన్ని పూర్తి వివరాలు జోడించబడతాయి.`;
        }
    </script>
</body>
</html>
