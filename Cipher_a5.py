import re
import copy
import sys 
import turtle


class Cipher_a5():

	
	def draw_regs(self):
		self.__demo__(-100,150,19,[0,1,2,5],10)
		self.__demo__(-163,10,22,[0,1],11)
		self.__demo__(-184,-130,23,[0,1,2,15],12)

		self.__strelka__([(-100,162),(-250,162),(-250,42)])
		self.__strelka__([(-163,22),(-230,22)])
		self.__strelka__([(-184,-118),(-250,-118),(-250,2)])
		self.__demoxor__(20,-250,22)
		self.__strelka__([(-270,22),(-300,22),(-300,-220),(314,-220),(314,-250),(295,-250)])

		self.__strelka__([(-90,150),(-90,80),(-60,80)])
		self.__strelka__([(-69,150),(-69,115),(-50,115),(-50,90)])
		self.__demoxor__(10,-50,80)
		self.__strelka__([(-40,80),(-25,80)])
		self.__strelka__([(-42,150),(-42,115),(-15,115),(-15,90)])
		self.__demoxor__(10,-15,80)
		self.__strelka__([(-5,80),(10,80)])
		self.__strelka__([(15,150),(15,115),(20,115),(20,90)])
		self.__demoxor__(10,20,80)
		self.__strelka__([(30,80),(314,80),(314,162),(299,162)])
		self.__strelka__([(120,150),(120,75),(384,75),(384,60)])

		self.__strelka__([(-153,10),(-153,-60),(-138,-60)])
		self.__strelka__([(-132,10),(-132,-25),(-128,-25),(-128,-50)])
		self.__demoxor__(10,-128,-60)
		self.__strelka__([(-118,-60),(314,-60),(314,22),(299,22)])
		self.__strelka__([(78,34),(78,40),(329,40)])

		self.__strelka__([(-174,-130),(-174,-200),(-144,-200)])
		self.__strelka__([(-153,-130),(-153,-165),(-134,-165),(-134,-190)])
		self.__demoxor__(10,-134,-200)
		self.__strelka__([(-124,-200),(-109,-200)])
		self.__strelka__([(-126,-130),(-126,-165),(-99,-165),(-99,-190)])
		self.__demoxor__(10,-99,-200)
		self.__strelka__([(-89,-200),(131,-200)])
		self.__strelka__([(141,-130),(141,-190)])
		self.__demoxor__(10,141,-200)
		self.__strelka__([(151,-200),(314,-200),(314,-118),(299,-118)])
		self.__strelka__([(78,-106),(78,-91),(384,-91),(384,20)])
		turtle.penup()
		turtle.goto(329,20)
		turtle.pendown()
		for i in range(2):
			turtle.fd(110)
			turtle.left(90)
			turtle.fd(40)
			turtle.left(90)
		turtle.penup()
		turtle.goto(347,40)
		turtle.pendown()
		turtle.write("управление",font=("Times New Roman", 12, "normal"))
		turtle.penup()
		turtle.goto(334,25)
		turtle.pendown()
		turtle.write("тактированием",font=("Times New Roman", 12, "normal"))


		

	def __write_reg__(self,x,y,reg):
		self.pen.penup()
		self.pen.goto(x+5, y-4)
		self.pen.pendown()
		self.pen.write(' '.join(list(map(str,list(reversed(reg))))),font=("Times New Roman", 20, "normal") )

	def __strelka__(self,coords):
		turtle.penup()
		turtle.goto(coords[0][0],coords[0][1])
		turtle.pendown()
		for i in range(1,len(coords)):
			turtle.goto(coords[i][0],coords[i][1])
		if coords[-1][0]<coords[-2][0]:
			turtle.goto(coords[-1][0]+10,coords[-1][1]-2)
			turtle.goto(coords[-1][0]+10,coords[-1][1]+2)
			turtle.goto(coords[-1][0],coords[-1][1])
		elif coords[-1][0]>coords[-2][0]:
			turtle.goto(coords[-1][0]-10,coords[-1][1]-2)
			turtle.goto(coords[-1][0]-10,coords[-1][1]+2)
			turtle.goto(coords[-1][0],coords[-1][1])
		elif coords[-1][1]>coords[-2][1]:
			turtle.goto(coords[-1][0]-2,coords[-1][1]-10)
			turtle.goto(coords[-1][0]+2,coords[-1][1]-10)
			turtle.goto(coords[-1][0],coords[-1][1])
		elif coords[-1][1]<coords[-2][1]:
			turtle.goto(coords[-1][0]-2,coords[-1][1]+10)
			turtle.goto(coords[-1][0]+2,coords[-1][1]+10)
			turtle.goto(coords[-1][0],coords[-1][1])

	def __demoxor__(self,r,x,y):
		turtle.color('red')
		turtle.penup()
		turtle.goto(x-r,y)
		turtle.pendown()
		turtle.goto(x+r,y)
		turtle.penup()
		turtle.goto(x,y+r)
		turtle.pendown()
		turtle.goto(x,y-r)
		turtle.pendown()
		turtle.circle(r)
		turtle.color('black')

	def loading_registers(self,key): #заполняет регистры, используя 64-битный ключ в качестве параметра
		self.reg_x=list(map(int,list(key[0:19])))
		self.reg_y=list(map(int,list(key[19:41])))
		self.reg_z=list(map(int,list(key[41:64])))
		
	def set_key(self): #устанавливает ключ и загружает регистры, если он содержит 0 и 1 и если он ровно 64 бита (8 символов) 
		tha_key = '1'
		while (len(tha_key) != 64 or not re.match("^([01])+", tha_key)):
			tha_key = str(input('Введите 8-символьный ключ: '))
			tha_key = ''.join(map(str,self.to_binary(tha_key)))
			print('Двоичная форма введённого ключа, полученная для формирования регистров:')
			print(tha_key)
		self.key_one=tha_key
		self.loading_registers(tha_key)
		

	def __demo__(self,x,y,n,obr,sin):
		turtle.penup()
		turtle.goto(x,y)
		turtle.pendown()
		for i in range(n):
			if i in obr:
				clr='blue'
			elif i==sin:
				clr='orange'
			else:
				clr='white'
			turtle.color('black',clr)
			turtle.begin_fill()
			turtle.goto(x+21*(i+1),y)
			turtle.goto(x+21*(i+1),y+24)
			turtle.goto(x+21*i,y+24)
			turtle.goto(x+21*i,y)
			turtle.end_fill()
			turtle.goto(x+21*(i+1),y)

	def to_binary(self,plain): #преобразует текст в двоичный формат
		s = ""
		i = 0
		for i in plain:
			binary = str(' '.join(format(ord(x), 'b') for x in i))
			j = len(binary)
			while(j < 8):
				binary = "0" + binary
				s = s + binary
				j = j + 1
		binary_values = []
		k = 0
		while(k < len(s)):
			binary_values.insert(k, int(s[k]))
			k = k + 1
		return binary_values


	def get_majority(slef,x,y,z): #выясняет, каких значений среди трёх битов большинство (1 или 0) 
		if(x + y + z > 1):
			return 1
		else:
			return 0

	def get_keystreambit(self,x,y):
		if -80<x<80 and 200<y<230:
			if (self.i < self.lengthbit):
				self.keystream.insert(self.i, self.reg_x[18] ^ self.reg_y[21] ^ self.reg_z[22])
				majority = self.get_majority(self.reg_x[8], self.reg_y[10], self.reg_z[10])
				if self.reg_x[8] == majority: 
					new = self.reg_x[13] ^ self.reg_x[16] ^ self.reg_x[17] ^ self.reg_x[18]
					reg_x_temp_two = copy.deepcopy(self.reg_x)
					j = 1
					while(j < len(self.reg_x)):
						self.reg_x[j] = reg_x_temp_two[j-1]
						j = j + 1
					self.reg_x[0] = new

				if self.reg_y[10] == majority:
					new_one = self.reg_y[20] ^ self.reg_y[21]
					reg_y_temp_two = copy.deepcopy(self.reg_y)
					k = 1
					while(k < len(self.reg_y)):
						self.reg_y[k] = reg_y_temp_two[k-1]
						k = k + 1
					self.reg_y[0] = new_one

				if self.reg_z[10] == majority:
					new_two = self.reg_z[7] ^ self.reg_z[20] ^ self.reg_z[21] ^ self.reg_z[22]
					reg_z_temp_two = copy.deepcopy(self.reg_z)
					m = 1
					while(m < len(self.reg_z)):
						self.reg_z[m] = reg_z_temp_two[m-1]
						m = m + 1
					self.reg_z[0] = new_two

				self.i = self.i + 1
				self.pen.clear()
				self.pen.penup()
				self.pen.goto(295-len(self.keystream)*14,-265)
				self.pen.pendown()
				self.pen.write(''.join(list(map(str,self.keystream))),font=("Times New Roman", 20, "normal"))
				self.__write_reg__(-100,150,self.reg_x)
				self.__write_reg__(-163,10,self.reg_y)
				self.__write_reg__(-184,-130,self.reg_z)
				if (self.i == self.lengthbit):
					self.distruct.clear()
					turtle.penup()
					turtle.goto(-180,200)
					turtle.pendown()
					turtle.write("Для получения результата закройте окно",font=("Times New Roman", 20, "normal"))


	def get_keystream(self,length): #вычисляет ключевой поток путем вычисления соответствующих индексов
		wndow = turtle.Screen()
		wndow.title("Шифр А5/1")
		wndow.setup(900, 550)
		self.pen=turtle.Turtle()
		self.lengthbit=length
		self.pen.hideturtle()
		self.pen.speed(11)
		turtle.hideturtle()
		turtle.speed(11)
		self.draw_regs()
		self.__write_reg__(-100,150,self.reg_x)
		self.__write_reg__(-163,10,self.reg_y)
		self.__write_reg__(-184,-130,self.reg_z)
		self.distruct = turtle.Turtle()
		self.distruct.speed(11)
		self.distruct.hideturtle()
		self.distruct.penup()
		self.distruct.goto(-80,200)
		self.distruct.pendown()
		self.distruct.color('black','green')
		self.distruct.begin_fill()
		for i in range(2):
			self.distruct.fd(160)
			self.distruct.left(90)
			self.distruct.fd(30)
			self.distruct.left(90)
		self.distruct.end_fill()
		self.distruct.penup()
		self.distruct.goto(-57,200)
		self.distruct.pendown()
		self.distruct.color('white')
		self.distruct.write("Смещение",font=("Times New Roman", 20, "normal"))
		self.distruct.color('black')
		self.keystream = []
		self.i = 0
		turtle.listen()
		turtle.onscreenclick(self.get_keystreambit, 1)
		turtle.done()
		return self.keystream


	def convert_binary_to_str(self,binary): #преобразование двоичного кода в строку
		s = ""
		length = len(binary) - 8
		i = 0
		while(i <= length):
			s = s + chr(int(binary[i:i+8], 2))
			i = i + 8
		return str(s)

	def encrypt(self,plain): #принимает открытый текст, преобразует его в двоичный код, получает ключевой поток после получения длины двоичного кода и XORит ключевого потока и двоичный код, а затем преобразует результат в строку
		s = ""
		binary = self.to_binary(plain)
		print ('Двоичная форма введённого текста:')
		print (''.join(list(map(str,binary))))
		keystream = self.get_keystream(len(binary))
		i = 0
		if len(keystream)==len(binary):
			while(i < len(binary)):
				s = s + str(binary[i] ^ keystream[i])
				i = i + 1
			return s
		else:
			print("Вы рано закрыли окно, придётся начать шифрование заново")
		return ''

	def decrypt(self,cipher): #принимает зашифрованный текст, формирует поток ключей исходя из его длины, зашифрованный текст XORится с ключевым потоком и преобразуется в строку
		s = ""
		binary = []
		keystream = self.get_keystream(len(cipher))
		i = 0
		if len(keystream)==len(cipher):
			while(i < len(cipher)):
				binary.insert(i,int(cipher[i]))
				s = s + str(binary[i] ^ keystream[i])
				i = i + 1
			print ('Двоичная форма полученного текста:')
			print (''.join(list(map(str,s))))
			return self.convert_binary_to_str(str(s))
		else:
			print("Вы рано закрыли окно, придётся начать дешифрование заново")
		return ''


		


