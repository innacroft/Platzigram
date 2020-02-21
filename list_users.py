from datetime import date

users = [
    {
        'email': 'ana_m@google.com',
        'first_name': 'Ana',
        'last_name': 'Martinez',
        'country':'Colombia',
        'city':'Bogotá',
        'password': '98654',
        'birthdate': date(1994, 4,2),
        'is_admin': True,
        'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

        
    },
    {
        'email': 'juan_p@google.com',
        'first_name': 'Juan',
        'last_name': 'Perez',
        'country':'México',
        'city':'Monterrey',
        'password': '344555',
        'is_admin': True
    },
    {
        'email': 'camila_l@google.com',
        'first_name': 'Camila ',
        'last_name': 'Lopez',
        'country':'Perú',
        'password': '1234',
        'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

        
    },
    {
        'email': 'luis_t@google.com',
        'first_name': 'Luis ',
        'last_name': 'Torres',
        'password': '45454545',
        'is_admin': True,
        'birthdate': date(2000, 5, 5)
    }
]

from posts.models import User

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)