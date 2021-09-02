lines = []
with open('3.txt', 'r', encoding = 'utf-8') as f:
	for line in f:
		lines.append(line.strip())
print(lines)
print(line)

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(time, name)
	
