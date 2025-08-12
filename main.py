import requests
import random

API_URL = "https://zenquotes.io/api/random"

def get_quotes():
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()
    return response.json()

def get_random_quote(quotes):
    return random.choice(quotes)

def main():
    print("✨ Daily Inspiration ✨\n")
    try:
        quotes = get_quotes()
        quote = get_random_quote(quotes)
        print(f"\"{quote['q']}\" — {quote.get('a', 'Unknown')}")
    except Exception as e:
        print("Error fetching quote:", e)

if __name__ == "__main__":
    main()
