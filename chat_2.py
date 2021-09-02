
def read_file(file_name):
	lines = []
	with open(file_name, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def converts(lines):
	person = None
	remi_word_count = 0
	remi_sticker_count = 0
	wei_word_count = 0
	wei_sticker_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		person = s[1]
		if person == '陳怡頻':
			if s[2] == '貼圖':
				remi_sticker_count += 1
			else:
				for m in s[2:]:
					remi_word_count += len(m)
		elif person == '韋霖':
			if s[2] == '貼圖':
				wei_sticker_count += 1
			else:
				for m in s[2:]:
					wei_word_count += len(m)
	print('remi 說了', remi_word_count, '個字,傳了', remi_sticker_count, '個貼讀')
	print('wei 說了', wei_word_count, '個字,傳了', wei_sticker_count, '個貼讀')


def write_file(file_name, lines):
	with open(file_name, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input1.txt')
	lines = converts(lines)
	# write_file('output1.txt', lines)


main ()



