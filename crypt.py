from Cipher_a5 import Cipher_a5

def user_input_plaintext(): #ввод открытого текста
	try:
		someIn = str(input('Введите открытый текст: '))
	except:
		someIn = str(input('Похоже, ваш открытый текст не подходит. Попробуйте снова: '))
	return someIn


StrCi=Cipher_a5()
StrCi.set_key()
plaintext = str(user_input_plaintext())
print(plaintext)
print("зашифрованный текст в двоичном виде: " + StrCi.encrypt(plaintext))
input("для продолжения нажмите Enter")
