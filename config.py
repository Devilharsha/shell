import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('BOT_TOKEN')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('OWNER_ID'+"1615607413"))
w.write('\n')
w.write('}')
