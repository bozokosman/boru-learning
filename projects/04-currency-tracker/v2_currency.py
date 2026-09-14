# Currency-Tracker v2
import random
import json
import os

rates = {
    "TL": 1.0,
    "USD": 48.50,
    "EUR": 56.57,
    "GBP": 65.82,
    "JPY": 0.33,
    "CHF": 60.20,
    "BTC": 2100000,
    "ETH": 120000,
    "BNB": 20000,
    "SOL": 5000,
    "XRP": 20,
    "XAU": 213400,
    "XAG": 3200,
    "XPT": 89240
}
symbols = set(rates.keys())
history=[]
portfolio = {}

def show_rates(rates):
    for key, value in rates.items():
        print(f"{key}: {value}")

def convert(rates, source, target, amount):
    if source not in rates or target not in rates:
        return None
    else:
        goal = (amount * rates[source]) / rates[target]
        return (source, target, amount, goal)

def add_history(history, record):
    history.append(record)
    return history

def show_history(history):
    output = "--- History ---\n"
    if not history:
        return "You have no previous transactions."
    else:
        for i in history:
            output += f"{i[2]} {i[0]} → {i[3]} {i[1]}\n"
        return output

def add_to_portfolio(portfolio, symbol, amount):
    if symbol not in rates:
        return "error"
    elif symbol in portfolio:
        portfolio[symbol] += amount
    else:
        portfolio[symbol] = amount
        
    return portfolio

def show_portfolio(portfolio, rates):
    if not portfolio:
        return "You have no assets in your portfolio."
    else:
        output = "--- Portfolio ---\n"
        total = 0
        for symbol, amount in portfolio.items():
            value = amount * rates[symbol]
            total += value
            output += f"{symbol}: {amount} → {value} TL\n"
        output += f"-------------------\nTotal Value: {total} TL"
        return output

def update_rates(rates):
    for key in rates:
        if key == "TL":
            continue
        rates[key] *= (1 + random.uniform(-0.03, 0.03))

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as jdata:
            loaded_data = json.load(jdata)
            return loaded_data["rates"], loaded_data["portfolio"], loaded_data["history"]            
    else:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump({"rates": rates, "portfolio": portfolio, "history": history}, f, indent=4, ensure_ascii=False)
            return rates, portfolio, history

def save_data(rates, portfolio, history):
    with open("data.json", "w", encoding="utf-8") as jdata:
        json.dump({"rates": rates, "portfolio": portfolio, "history": history}, jdata, indent=4, ensure_ascii=False)

def main():
    global rates, portfolio, history
    rates, portfolio, history = load_data()
    print("Welcome.")
    while True:
        print("""
1- Show Rates
2- Convert
3- Show Portfolio
4- Add Asset to Portfolio
5- Show Conversion History
6- Update Rates (Simulation)
7- Exit
""")
        
        choose = input("Please make your selection: ")
        if choose == "1":
            show_rates(rates)
        elif choose == "2":
            source = input("At which exchange rate: ").upper()
            target = input("To which exchange rate: ").upper()
            amount = float(input("how much: "))
            result = convert(rates, source, target, amount)
            if result is None:
                print("Error: Invalid unit")
            else:
                add_history(history, result)
                print(result)
        elif choose == "3":
            print(show_portfolio(portfolio, rates))
        elif choose == "4":
            symbol = input("Which exchange rate would you like to add: ").upper()
            money = float(input("How much would you like to add: "))
            added = add_to_portfolio(portfolio, symbol, money)
            if added == "error":
                print("Invalid currency! Please try again.")
            else:
                print("The transaction was completed successfully.")
        elif choose == "5":
            histor = show_history(history)
            print(histor)
        elif choose == "6":
            update_rates(rates)
            print("All exchange rates have been updated.")
        elif choose == "7":
            save_data(rates, portfolio, history)
            print("Good Bye!")
            break
        else:
            print("You entered the wrong transaction. Please try again.")

if __name__ == "__main__":
    main()