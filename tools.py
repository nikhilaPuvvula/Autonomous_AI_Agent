# agents/tools.py
from langchain.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchResults


@tool
def get_weather_data(city: str) -> str:
    """Fetch current weather for a given city."""
    try:
        # Step 1: Get latitude & longitude from Open-Meteo geocoding
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_res = requests.get(geo_url).json()
        results = geo_res.get("results")
        if not results:
            return f"City '{city}' not found."
        lat, lon = results[0]["latitude"], results[0]["longitude"]

        # Step 2: Get current weather
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url)
        data = response.json()
        weather = data.get("current_weather", {})
        return f"Weather in {city}: {weather.get('temperature')}°C, Windspeed: {weather.get('windspeed')} km/h"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"


@tool
def convert_currency(amount_currency: str) -> str:
    """Convert currencies. Example: '10 USD to INR'"""
    try:
        parts = amount_currency.upper().split()
        amount, from_curr, _, to_curr = parts
        url = f"https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}&amount={amount}"
        response = requests.get(url)
        result = response.json()
        return f"{amount} {from_curr} = {result['result']} {to_curr}"
    except Exception as e:
        return f"Error in conversion: {str(e)}"


@tool
def calculate(expression: str) -> str:
    """Evaluate a math expression."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Invalid expression: {str(e)}"


@tool
def run_python_code(code: str) -> str:
    """Execute small Python code safely."""
    try:
        local_vars = {}
        exec(code, {}, local_vars)
        return str(local_vars)
    except Exception as e:
        return f"Error executing code: {str(e)}"


@tool
def web_search(query: str) -> str:
    """Search the web using DuckDuckGo."""
    try:
        search = DuckDuckGoSearchResults()
        result = search.run(query)
        return result
    except Exception as e:
        return f"Error performing search: {str(e)}"
