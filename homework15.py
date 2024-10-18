import json
import requests

url = 'https://dummyjson.com/products?limit=200'
response = requests.get(url)
response_json = response.json()
brands: list[dict] = response_json['products']

total_price_prem_brands = 0

for brand in brands:
    if brand.get('brand') == 'TechGear':
        print(f"id of TechGear brand products: {id(brand['sku'])}")
    if brand.get('id') == 135:
        image_url = brand['images'][0]
        image_response = requests.get(image_url)
        with open('phone.png', mode='wb') as pic_file:
            pic_file.write(image_response.content)
    if 'premium' in brand['description']:
        if brand['price'] > 800:
            total_price_prem_brands += brand['price']
print(f"price for premium brands: {total_price_prem_brands}")

pass
