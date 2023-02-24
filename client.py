import requests

# response = requests.post('http://127.0.0.1:5000/announcements',
#                          json={'header': 'Bots_on_python',
#                                'description': 'Cost_50_rubles',
#                                'username': 'Poor_developer'})

# response = requests.get('http://127.0.0.1:5000/announcements/1')

# response = requests.patch('http://127.0.0.1:5000/announcements/1',
#                          json={'header': 'Teaching_python',
#                                'description': 'Cost_80000_rubles',
#                                'username': 'Rich_infoseller'})

response = requests.delete('http://127.0.0.1:5000/announcements/1')

print(response.status_code)
print(response.text)
