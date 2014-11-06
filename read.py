import getpass
import json
import datetime
json_data = open('card.json','r+')
j = json.load(json_data)
day = open( datetime.date.today().strftime("%B%d%Y") + '.txt','a')
owner = ''
accepting = True
while accepting:
	card = getpass.getpass('Swipe Card: ')
	extra = getpass.getpass('')
	card = card[6:15]
	card = filter(str.isdigit, card)
	if card not in j:
		answer = raw_input('The UIN '+ card +' is not recognized. Should it be added: ')
		if answer == 'y':
			name = raw_input('Who does '+ card +' belong to: ')
			j[card] = name	
			json_data.seek(0)  # rewind
			json_data.write(json.dumps(j))
			json_data.truncate()
			day.write(j[card] + '\n') 
	else:
		print j[card]
		day.write(j[card] + '\n')
	
	if card == owner:
		accepting = False
json_data.close()


