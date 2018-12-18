import time

print('-'*65)
print('Life Decision Bot:')
print()
answer = input('Are you having a good morning? ')
if answer == 'Yes':
	print('Well...')
	time.sleep(1)
	print('It is gonna get a LOT worse...' )
	time.sleep(1)
else:
	print('Sorry to hear that, chap')
	print('Go see a movie later.' )
	print('-'*65)
