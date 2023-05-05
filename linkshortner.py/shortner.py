import requests

def shorten_link(full_link, link_name):
    API_KEY = '87ce21c7adf87d5a182c3852c49bf3fb'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    if data['url']['status'] == 7:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        print('Title:', title)
        print('Link:', short_link)
    else:
        print('Error:', data['url']['status'])

# Example usage:
link = input('Enter a link: >>')
name = input('Give your link a name: >>')

shorten_link(link, name)
