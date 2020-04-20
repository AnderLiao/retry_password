default_pw = 'a123456'
i = 3
while True:
	user_pw = input('Password: ')
	if user_pw != default_pw:
		if i == 1:
			print('Sorry, you only can try again after 24 hours')
			break
		else:
			print('You have ' + str(i-1) + ' more chances to try')
			i -= 1
	else:
		print('Successful login!')
		break
