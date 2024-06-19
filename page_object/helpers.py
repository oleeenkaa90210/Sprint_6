import random
from datetime import datetime, timedelta


def generate_order_info():

    names = ['Иван', 'Петр', 'Сергей', 'Алексей', 'Михаил']
    surnames = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнов']
    addresses = ['ул. Ленина, д. 1', 'ул. Пушкина, д. 5', 'ул. Гоголя, д. 10', 'ул. Чехова, д. 15', 'ул. Толстого, д. 20']
    metro_stations = ['Бульвар Рокоссовского', 'Черкизовская', 'Преображенская площадь', 'Сокольники', 'Комсомольская']

    user_info = {
        'name': random.choice(names),
        'surname': random.choice(surnames),
        'metro': random.choice(metro_stations),
        'phone': random.randint(10000000000, 99999999999),
        'address': random.choice(addresses)
    }

    random_date = datetime.now() + timedelta(days=random.randint(1, 7))
    user_info['date'] = random_date.strftime('%d.%m.%Y')

    return user_info
