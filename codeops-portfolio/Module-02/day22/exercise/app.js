const API_URL = "https://open.er-api.com/v6/latest/ETB";
const state = {
    rates:{},
    watchlist:[],
    loading:false,
    error:null
};

const status = document.getElementById("status");
const form = document.getElementById("form");
const amountInput = document.getElementById("amount");
const currencySelect = document.getElementById("currency");
const result = document.getElementById("result");
const watchlistElement = document.getElementById("watchlist");

function saveState (){
    localStorage.setItem(
        "birrwatch", 
        JSON.stringify(state.watchlist)
    );
}
function loadState() {
    const saved = localStorage.getItem("birrwatch");
    if (saved) {
        state.watchlist = JSON.parse(saved);
}}

function render() {
    renderCurrencies();
    renderWatchlist();
}

function renderCurrencies() {
    currencySelect.innerHTML = "";
    const currencies = Object.keys(state.rates)
    currencies.forEach(currency => {
        const option = document.createElement("option");
        option.value = currency;
        option.textContent = currency;
        currencySelect.appendChild(option);
    });
}

function renderWatchlist() {
    watchlistElement.innerHTML = "";
    if (state.watchlist.length === 0) {
        const empty = document.createElement("li");
        empty.textContent = "No currencies in your watchlist.";
        empty.className = "empty";
        watchlistElement.appendChild(empty);
        return;}
    state.watchlist.forEach(currency => {
        const li = document.createElement("li");
        li.innerHTML = `
            <span>${currency}</span>
            <button
                class="delete-btn"
                data-currency="${currency}">
                Delete
            </button>
        `;
        watchlistElement.appendChild(li);
    });
}
async function loadRates() {

    state.loading = true;
    state.error = null;

    status.textContent = "Loading exchange rates...";
    status.className = "status loading";

    try {

        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to load exchange rates.");
        }

        const data = await response.json();

        state.rates = data.rates;

        state.loading = false;

        status.textContent = "Rates loaded successfully.";
        status.className = "status success";

        render();

    } catch (error) {

        state.loading = false;
        state.error = error.message;

        status.textContent = "Error: " + error.message;
        status.className = "status error";
    }
}

form.addEventListener("submit", function (event) {

    event.preventDefault();

    const amount = Number(amountInput.value);
    const currency = currencySelect.value;

    if (!amount || amount <= 0) {

        result.textContent = "Please enter a valid amount.";

        return;
    }

    if (!currency) {

        result.textContent = "Please choose a currency.";

        return;
    }

    const rate = state.rates[currency];

    if (!rate) {

        result.textContent = "Exchange rate not available.";

        return;
    }

    const convertedAmount = amount * rate;

    result.textContent =
        `${amount.toFixed(2)} ETB = ${convertedAmount.toFixed(2)} ${currency}`;
});

function addToWatchlist(currency) {
    if (state.watchlist.includes(currency)) {
        return;
    }

    state.watchlist.push(currency);

    saveState();
    renderWatchlist();
}

watchlistElement.addEventListener("click", function (event) {

    if (!event.target.classList.
        contains("delete-btn")) {
        return;
    }

    const currency = event.target.dataset.currency;

    state.watchlist = state.watchlist.filter(
        item => item !== currency
    );

    saveState();
    renderWatchlist();
});

currencySelect.addEventListener("change", function () {

    const currency = currencySelect.value;

    if (currency) {
        addToWatchlist(currency);
    }
});

loadState();
render();
loadRates();
