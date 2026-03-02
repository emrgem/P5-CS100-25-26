import requests
def get_rates(base_currency):
    """Fetch latest rates for given base currency => dict >None """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API returned {response.status_code}")
            return None
    except(requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        print("Cannot reach API (timeout or no internet)")
        return None
    
def convert(amount, base, target):
    data = get_rates(base)
    if not data:
        print("Could not fetch exchange rates.")
        return
    target = target.upper()
    if target not in data["rates"]:
        print(f"Currency '{target}' not found!")
        return
    rate = data["rates"][target]
    result = amount * rate
    
    print(f"{amount:,.2f} {base} -> {result:,.2f} {target}")
    print(f" (1 {base} = {rate:.4f} {target})")
    
    
def main():
    print("===Simple Currency Converter===")
    print("Examples: USD EUR GBP JPY CAD\n")
    
    while True:
        base = input("From currency (or 'quit'):").strip().upper()
        if base == "QUIT":
            print("Bye!")
            break
        if not base:
            continue
        target = input("To currency:").strip().upper()
        if not target:
            continue
        try:
            amount = float(input("Amount:"))
            if amount <= 0:
                print("Enter a positive number\n")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
        
        convert(amount, base, target)
        print("====================")
        
if __name__ == "__main__":
    main()