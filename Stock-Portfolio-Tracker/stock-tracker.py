stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 310
}

def stock_tracker():
    print("=" * 40)
    print("     STOCK PORTFOLIO TRACKER")
    print("=" * 40)
    print("\nAvailable stocks:", ", ".join(stock_prices.keys()))

    portfolio = {}
    total = 0

    while True:
        stock = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found. Try again.")
            continue

        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            if qty <= 0:
                print("❌ Quantity must be positive.")
                continue
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty

    if not portfolio:
        print("\nNo stocks added.")
        return

    print("\n" + "=" * 40)
    print("        YOUR PORTFOLIO")
    print("=" * 40)
    print(f"{'Stock':<10} {'Qty':<8} {'Price':<10} {'Value'}")
    print("-" * 40)

    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total += value
        print(f"{stock:<10} {qty:<8} ${stock_prices[stock]:<10} ${value}")

    print("-" * 40)
    print(f"{'TOTAL':<28} ${total}")

    save = input("\nSave portfolio to file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.csv", "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                f.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
            f.write(f"TOTAL,,,{total}\n")
        print("✅ Portfolio saved to portfolio.csv")

stock_tracker()