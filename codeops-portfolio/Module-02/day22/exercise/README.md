# Birr Watch

Birr Watch is a simple ETB currency converter that uses live exchange rates from a public API.

## What It Does

- Loads live ETB exchange rates from a public API
- Displays available currencies in a dropdown
- Converts an amount of Ethiopian Birr (ETB) to a selected currency
- Shows loading, success, and error messages
- Allows currencies to be added to a watchlist
- Prevents duplicate currencies in the watchlist
- Allows currencies to be removed from the watchlist
- Saves the watchlist using localStorage
- Restores the watchlist after refreshing the page

## API Used

Birr Watch uses the ExchangeRate-API public endpoint:

https://open.er-api.com/v6/latest/ETB

The API provides exchange rates with ETB as the base currency.

## How to Run

1. Download or clone the project.
2. Open the project folder in VS Code.
3. Make sure these files are present:

   - index.html
   - style.css
   - app.js
   - README.md

4. Open index.html using Live Server or another local development server.
5. Open the app in your browser.

## Project Structure

```text
exercise/
│
├── index.html
├── style.css
├── app.js
└── README.md