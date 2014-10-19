import getpass
import json
import datetime
j = json.loads(open('card.json').read())
day = open( datetime.date.today().strftime("%B%d%Y") + '.txt','a')
while True:
	card = getpass.getpass('Swipe Card: ')
	extra = getpass.getpass('')
	card = card[6:15]
	card = filter(str.isdigit, card)
	if card not in j:
		print 'Invalid Read'
	else:
		print j[card]
		day.write(j[card] + '\n')
