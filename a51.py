import re
import os







def user_input_choice(): #ввод номера пункта меню
	someIn = str(input('[0]: Выход\n[1]: Зашифровать\n[2]: Расшифровать\nВведите 0, 1, или 2: '))
	if (someIn == '0' or someIn == '1' or someIn == '2'):
		return someIn
	else:
		while(someIn != '0' or someIn != '1' or someIn != '2'):
			if (someIn == '0' or someIn == '1' or someIn == '2'):
				return someIn
			someIn = str(input('[0]: Выход\n[1]: Зашифровать\n[2]: Расшифровать\nPress 0, 1, или 2: '))
	return someIn

if __name__ == '__main__': #главная функция
	first_choice=7
	while first_choice!='0':
		first_choice = user_input_choice()
		if(first_choice == '1'):
			os.system('шифрование.exe')
		elif(first_choice == '2'):
			os.system('дешифрование.exe')
	print('Для закрытия окна нажмите любую клавишу')

