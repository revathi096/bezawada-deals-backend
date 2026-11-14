
const BD_API = "/api";

let bdSelectedCategory = "";
let bdAllDeals = [];
let bdCategories = [];

const bdArea = document.getElementById("bdArea");
const bdWard = document.getElementById("bdWard");
const bdSearch = document.getElementById("bdSearch");
const bdDeals = document.getElementById("bdDeals");
const bdCategoriesBox = document.getElementById("bdCategories");

const bdWards = Array.from({ length: 86 }, (_, i) => i + 1);

bdWards.forEach(number => {
  const option = document.createElement("option");
  option.value = number;
  option.textContent = `Ward ${number}`;
  bdWard.appendChild(option);
});

async function bdLoadCategories() {
  try {
    const response = await fetch(`${BD_API}/categories`);
    if (!response.ok) throw new Error("Categories unavailable");

    bdCategories = await response.json();

    bdCategoriesBox.innerHTML =
      '<button class="active" data-category="">All Categories</button>';

    bdCategories.forEach(category => {
      const button = document.createElement("button");
      button.dataset.category = category.id;
      button.textContent =
        `${category.icon || "🛍️"} ${category.name}`;

      bdCategoriesBox.appendChild(button);
    });

  } catch (error) {
    bdCategoriesBox.innerHTML =
      "<p>Categories load కాలేదు. Server check చేయండి.</p>";
  }
}

async function bdLoadDeals() {
  bdDeals.innerHTML = "Loading live deals...";

  const params = new URLSearchParams();

  if (bdSelectedCategory) {
    params.set("category", bdSelectedCategory);
  }

  if (bdArea.value) {
    params.set("area", bdArea.value);
  }

  if (bdSearch.value.trim()) {
    params.set("search", bdSearch.value.trim());
  }

  try {
    const response = await fetch(
      `${BD_API}/deals?${params.toString()}`
    );

    if (!response.ok) throw new Error("Deals unavailable");

    bdAllDeals = await response.json();

    // Ward-specific filter: apply only if the API returns ward data.
    const selectedWard = bdWard.value;
    let results = bdAllDeals;

    if (selectedWard) {
      results = results.filter(deal =>
        String(deal.ward_number || "") === selectedWard
      );
    }

    bdRenderDeals(results);

  } catch (error) {
    bdDeals.textContent =
      "Deals load కాలేదు. Backend API connection check చేయండి.";
  }
}

function bdRenderDeals(deals) {
  document.getElementById("bdResultCount").textContent =
    `${deals.length} Deals`;

  const areaName = bdArea.value || "All Areas";
  const categoryName =
    bdCategories.find(c => String(c.id) === String(bdSelectedCategory))?.name
    || "All Categories";

  document.getElementById("bdResultTitle").textContent =
    `${areaName} – ${categoryName}`;

  if (!deals.length) {
    bdDeals.innerHTML =
      "<p>ఈ ప్రాంతంలో ప్రస్తుతం deals అందుబాటులో లేవు.</p>";
    return;
  }

  bdDeals.innerHTML = "";

  deals.forEach(deal => {
    const card = document.createElement("article");
    card.className = "bd-deal-card";

    const image = document.createElement("img");
    image.src = deal.image_url || "https://placehold.co/600x350?text=BezawadaDeals";
    image.alt = deal.title || "Deal image";

    const title = document.createElement("h4");
    title.textContent = deal.title || "Local Deal";

    const description = document.createElement("p");
    description.textContent = deal.description || "";

    const price = document.createElement("p");
    price.className = "bd-price";
    price.textContent = deal.price != null
      ? `₹${deal.price}`
      : (deal.discount || "Offer available");

    const location = document.createElement("p");
    location.textContent =
      `${deal.area || "Vijayawada"}${deal.ward_number ? " • Ward " + deal.ward_number : ""}`;

    card.append(image, title, description, price, location);
    bdDeals.appendChild(card);
  });
}

bdCategoriesBox.addEventListener("click", event => {
  const button = event.target.closest("button[data-category]");
  if (!button) return;

  bdCategoriesBox.querySelectorAll("button")
    .forEach(item => item.classList.remove("active"));

  button.classList.add("active");
  bdSelectedCategory = button.dataset.category;
  bdLoadDeals();
});

bdArea.addEventListener("change", bdLoadDeals);
bdWard.addEventListener("change", bdLoadDeals);

let bdSearchTimer;
bdSearch.addEventListener("input", () => {
  clearTimeout(bdSearchTimer);
  bdSearchTimer = setTimeout(bdLoadDeals, 350);
});

document.getElementById("bdBack").addEventListener("click", () => {
  if (history.length > 1) {
    history.back();
  } else {
    window.location.href = "/";
  }
});

document.getElementById("bdDashboard").addEventListener("click", () => {
  document.getElementById("bdDashboardPanel").hidden = false;
  document.getElementById("bdDashboardPanel")
    .scrollIntoView({ behavior: "smooth" });

  const token = localStorage.getItem("token");

  document.getElementById("bdUserInfo").textContent = token
    ? "మీరు login అయ్యారు. మీ account options ఇక్కడ కనిపిస్తాయి."
    : "Dashboard ఉపయోగించడానికి ముందుగా Login చేయండి.";
});

function bdShowDeals() {
  document.getElementById("bdDashboardPanel").hidden = true;
  document.getElementById("ward-marketplace")
    .scrollIntoView({ behavior: "smooth" });
}

function bdShowSaved() {
  alert("Saved Deals feature కోసం login మరియు favorites API connect చేయాలి.");
}

function bdShowMyPosts() {
  alert("My Posts feature కోసం seller dashboard API connect చేయాలి.");
}

bdLoadCategories().then(bdLoadDeals);

// Refresh displayed deals periodically.
// This fetches the latest data; it does not create market prices automatically.
setInterval(bdLoadDeals, 30000);
