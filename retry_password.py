default_pw = 'a123456'
i = 3
while True:
	user_pw = input('Password: ')
	if user_pw != default_pw:
		print('You have ' + str(i-1) + ' more chances to try')
		i -= 1
		if i == 0:
			print('Sorry, you only can try again after 24 hours')
			break
	else:
		print('Successful login!')
		break
