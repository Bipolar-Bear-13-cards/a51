from Cipher_a5 import Cipher_a5
import re

def user_input_ciphertext(): #ввод зашифрованного текста
	ciphertext = str(input('Введите зашифрованный текст в двоичном виде: '))
	if (re.match("^([01])+", ciphertext)):
		return ciphertext
	else:
		while(not re.match("^([01])+", ciphertext)):
			if (re.match("^([01])+", ciphertext)):
				return ciphertext
			ciphertext = str(input('Введите зашифрованный текст в двоичном виде: '))
	return ciphertext


StrCi=Cipher_a5()
StrCi.set_key()
ciphertext = str(user_input_ciphertext())
print(StrCi.decrypt(ciphertext))
input("для продолжения нажмите Enter")
