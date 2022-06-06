import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('BOT_TOKEN')+"5347869449:AAFmdvJD2PzhFhgw6X-iti-fKwndNW-g3uc",')
w.write('\n')
w.write('    "owner": '+os.getenv('OWNER_ID'+"1615607413"))
w.write('\n')
w.write('}')
