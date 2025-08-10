def currency_converter():
    # Hardcoded exchange rates relative to USD
    rates = {
        "USD": 1.0,
        "EUR": 0.91,
        "INR": 83.0,
        "GBP": 0.78,
        "JPY": 138.5,
        "AUD": 1.49
    }

    print("Available currencies:", ", ".join(rates.keys()))
    from_curr = input("Convert from (currency code): ").upper()
    to_curr = input("Convert to (currency code): ").upper()

    if from_curr not in rates or to_curr not in rates:
        print("Invalid currency code(s).")
        return

    try:
        amount = float(input(f"Amount in {from_curr}: "))
    except ValueError:
        print("Invalid amount entered.")
        return

    # Convert amount to USD first, then to target currency
    amount_in_usd = amount / rates[from_curr]
    converted_amount = amount_in_usd * rates[to_curr]

    print(f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}")

if __name__ == "__main__":
    currency_converter()
