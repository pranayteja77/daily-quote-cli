import requests

API_URL = "https://zenquotes.io/api/random"

def get_quote():
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()
    data = response.json()
    if isinstance(data, list) and data:
        return data[0]
    raise ValueError("No quote found in response.")

def main():
    print("✨ Daily Inspiration ✨\n")
    try:
        quote = get_quote()
        print(f"\"{quote['q']}\"")
        print(f"   — {quote.get('a', 'Unknown')}")
        print("-" * 40)
    except Exception as e:
        print("Sorry, couldn't fetch a quote right now.")
        print("Details:", e)

if __name__ == "__main__":
    main()