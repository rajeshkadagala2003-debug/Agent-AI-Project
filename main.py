from agents.weather_agent import get_weather
from agents.stock_agent import get_stock_price
from agents.joke_agent import get_joke
from agents.calendar_agent import create_event
from agents.notifier_agent import send_whatsapp
 
from utils.context_manager import detect_agent
 
 
def extract_city(query):
 
    words = query.split()
 
    return words[-1]
 
 
def run_agent(query):
 
    agent = detect_agent(query)
 
    if agent == "weather":
 
        city = extract_city(query)
 
        return get_weather(city)
 
    elif agent == "stock":
 
        return get_stock_price(query)
 
    elif agent == "joke":
 
        return get_joke()
 
    elif agent == "calendar":
 
        return create_event(query)
 
    else:
 
        return "Sorry, I couldn't understand your request."
 
 
def send_to_whatsapp(message):
 
    return send_whatsapp(message)