import requests  # Import the requests library to handle HTTP requests

def get_weather(city):
    api_key = "1429dab92711e2f7ab9a28a17399800b"  
    # Construct the API URL with the city name, API key, and units (metric for Celsius)
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Send a GET request to the OpenWeatherMap API
        response = requests.get(base_url)
        # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        # Parse the JSON response
        weather_data = response.json()

        # Extract temperature, humidity, and weather description from the response
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        # Return a dictionary with the weather information
        return {
            "temperature": temp,
            "humidity": humidity,
            "description": description
        }
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        if response.status_code == 404:
            return f"Error: City '{city}' not found. Please check the spelling and try again."
        else:
            return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        # Handle any other request-related errors
        return f"Error: {req_err}"

def main():
    print("Basic Weather App")  # Print a welcome message for the weather app
    city = input("Enter the city name: ")  # Prompt the user to enter a city name
    weather = get_weather(city)  # Get the weather information for the entered city

    # Check if the returned weather information is a dictionary (valid response)
    if isinstance(weather, dict):
        # Print the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Condition: {weather['description']}")
    else:
        # Print the error message
        print(weather)

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
