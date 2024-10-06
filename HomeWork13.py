car_4x2_CVT = {
    'price': 1263400,
    'is rear LED lights with dynamic turn indicators': False,
    'external design elements': [
        'Layers on the roof',
        'Protective cover on the bumper',
        'Additional tinting of rear windows',
        '18" 2-color alloy wheels',
    ],
    'panoramic glass roof': {},

}

car_4x2_CVT_INTENSE = {
    'price': 1470800,
    'is rear LED lights with dynamic turn indicators': True,
    'external design elements': [
        'Layers on the roof',
        'Protective cover on the bumper',
        'Additional tinting of rear windows',
        '18" 2-color alloy wheels',
        'Special paint "black amethyst"',
    ],
    'panoramic glass roof': 29486,
}

price_panoramic_glass_INTENSE = car_4x2_CVT_INTENSE['panoramic glass roof']
print(price_panoramic_glass_INTENSE)

for element in car_4x2_CVT['external design elements']:
    print(element)
