import requests

API_KEY = "e10779228ee035394af6425f8471f722"  # ⬅️ Replace with your actual key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        
        # 🧪 DEBUG PRINTS – Add these lines
        print("Requesting weather for:", city)
        print("Full URL:", response.url)
        print("Status Code:", response.status_code)
        print("Response:", data)

        if response.status_code == 200:
            print(f"\n🌤 Weather in {data['name']}, {data['sys']['country']}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Feels Like: {data['main']['feels_like']}°C")
            print(f"Condition: {data['weather'][0]['description'].title()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s\n")
        else:
            print(f"\n❌ City not found: {city}")
    except Exception as e:
        print("⚠️ Error occurred:", e)

def main():
    print("🌦️ Welcome to Weather CLI App")
    while True:
        city = input("🔍 Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("👋 Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
