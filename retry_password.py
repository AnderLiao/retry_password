default_pw = 'a123456'
i = 3 # remaining balance
while i > 0:
	user_pw = input('Password: ')
	i -= 1
	if user_pw == default_pw:
		print('Successful login!')
		break
	elif i == 0:
		print('Sorry, you only can try again after 24 hours')
	else:
		print('You have ' + str(i) + ' more chances to try')