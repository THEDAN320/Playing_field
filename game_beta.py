from random import *

#задаем высоту и ширину поля
visota = 8
shirina = 8
shirina2 = shirina
arr = []
#

#заполняем игровое поле
while visota >= 0:
	arr.append([])
	visota -= 1
	
for i in range(0,shirina + 1):
	shirina = shirina2
	while shirina >= 0:
		arr[shirina].append("     ")
		shirina -= 1
		
zapolnenie = len(arr) 
for i in range(0,zapolnenie):
		arr[0][i] = "----"
		arr[-1][i] = "----"
		arr[i][0] = "|"
		arr[i][-1] = "|"
		
arr[0][0] = "|----"
arr[0][-1] = "---|"
arr[-1][0] = "|----"
arr[-1][-1] = "---|"
#
	
#создаем игрока
x_coor =round(len(arr)/2)
y_coor = round(len(arr[0])/2)
arr[x_coor][y_coor] = "  +  "
#

#создаем конечную цель
def start():
	while True:
		x_win = randint(1,len(arr)-2)
		y_win = randint(1,len(arr)-2)
		if x_win == x_coor and y_win == y_coor:
			pass
		else:
			arr[x_win][y_win] = "  @  "
			return x_win, y_win
#
		
# координаты конечной цели
x_win, y_win = map(int,start())
#

#реализуем передвижение
def game(x_coor,y_coor):
	print("Up , down , left or right?")
	enter = input("Вверх , вниз, влево или вправо?  -  ").lower()
	
	if enter == "вверх" or enter == "up":
		
		if arr[x_coor - 1] == arr[0]:
			return x_coor, y_coor
			
		else:
			arr[x_coor][y_coor] = "     "
			x_coor -= 1
			arr[x_coor][y_coor] = "  +  "
			return x_coor, y_coor
		
	elif enter == "вниз" or enter == "down":
		if arr[x_coor + 1] == arr[-1]:
			return x_coor, y_coor
		else:
			arr[x_coor][y_coor] = "     "
			x_coor += 1
			arr[x_coor][y_coor] = "  +  "
			return x_coor, y_coor
		
	elif enter == "влево" or enter == "left":
		for i in range(0,len(arr)):
			if arr[i][y_coor - 1] == arr[i][0]:
				return x_coor, y_coor
			else:
				arr[x_coor][y_coor] = "     "
				y_coor -= 1
				arr[x_coor][y_coor] = "  +  "
				return x_coor, y_coor
	
	elif enter == "вправо" or enter == "right":
		for i in range(0,len(arr)):
			if arr[i][y_coor + 1] == arr[i][-1]:
				return x_coor, y_coor
			else:
				arr[x_coor][y_coor] = "     "
				y_coor += 1
				arr[x_coor][y_coor] = "  +  "
				return x_coor, y_coor
		
	else:
		return x_coor, y_coor
#
		
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# запускаем цикл для игры
while True:
	cikl = 0
	
	# делаем нормальный вывод списка
	while cikl < len(arr):
		arr_str = str(arr[cikl])
		clean_str = ""
		for i in arr_str:
			if i == "[" or i == "]" or i == "," or i =="'":
				pass
			else:
				clean_str += i
		print(clean_str,"\n")
		cikl += 1
	#
	
	x_coor, y_coor = map(int,game(x_coor,y_coor))
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	
	# обьявляем победу
	if x_win == x_coor and y_win == y_coor:
		print("Победа ")
		break
	#
#