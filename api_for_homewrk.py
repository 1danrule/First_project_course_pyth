import requests
import json
from email_util import send_email

url = 'https://script.google.com/macros/s/AKfycby6BJceD647XpPdX2Yf5QewhkCnbt4tcefKyJ7CeO8QE88XSsk6kEePZGW8YNYt6ui6hg/exec'

response = requests.get(url)
response_json = response.json()
animals: list[dict] = response_json['data']

total_price_care = 0
african_animals = 0
most_expensive_animal = None

for animal in animals:
    if animal['is_poison'] is True:
        total_price_care += animal['cost_of_caring']
    if animal['continent'] == 'Африка':
        african_animals += 1
    if most_expensive_animal is None or animal['cost_of_caring'] > most_expensive_animal['cost_of_caring']:
        most_expensive_animal = animal

if most_expensive_animal:
    animal_name = most_expensive_animal['animal_name']
    animal_cost = most_expensive_animal['cost_of_caring']

    mail_body = f"""
    <h1>Інформація про найбільш дорогу в обслуговуванні тварину</h1>
    <p>Назва тварини: {animal_name}</p>
    <p>Витрати за обслуговування: {animal_cost}</p>
    """
    if most_expensive_animal['is_poison'] is True:
        mail_body += "<h3>Увага, ця тварина отруйна!"

    recipients = ['test_hillel_api_mailing@ukr.net']
    mail_subject = 'Інформація про найбільш дорогу в обслуговуванні тварину'

    send_email(recipients, mail_body, mail_subject)
