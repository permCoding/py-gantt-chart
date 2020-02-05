
f = open('input.txt', 'r')
lines = f.read().split('\n')
f.close()

bar = '█' # символ для рисования столбиков
spa = ' ' # символ для рисование пустоты
tab = []  # таблица загруженности
objs = []  # список объектов
tetris = [] # список загруженности


min_left = max_right = 0
for line in lines:
	if line != '':
		id, left, right = map(int, line.split())
		objs.append((id,left,right))
	else:
		break
objs = objs[::-1] # разворачиваем, так как на графике снизу-вверх


# определяем границы
min_left = objs[0][1]
max_right = objs[0][2]
for obj in objs:
	if obj[1] < min_left:
		min_left = obj[1]
	if obj[2] > max_right:
		max_right = obj[2]
tab = [0]*max_right

# формируем исходную диаграмму ганта
gant = "объекты\n"
for obj in objs:
	line = '%4d' % obj[0]
	for pos in range(max_right):
		if obj[1] <= pos+1 <= obj[2]:
			tab[pos] += 1
			line += bar
		else:
			line += spa
	gant += line + '\n'
gant += spa*3 + ''.join([str(i) for i in range(10)]) + '\n'


# формируем диаграмму с пиками нагруженности
gant += '\n\n\n'
for row in range(len(objs)):
	tetris.append([spa for col in range(max_right)])
for col in range(max_right):
	for row in range(len(tetris)):
		if row <= tab[col]-1:
			tetris[row][col] = bar
		else:
			break
gant += 'загруженность\n'
tetris = tetris[::-1]
for row in range(len(tetris)):
	gant += '%4d' % (row+1) + ''.join(tetris[row]) + '\n'
gant += spa*3 + ''.join([str(i) for i in range(10)]) + '\n'


f = open('output.txt', 'w', encoding='utf-8')
f.write(gant)
f.close()


#
