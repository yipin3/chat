
def read_file(file_name):
	lines = []
	with open(file_name, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def converts(lines):
	new = []
	person = None
	for line in lines:
		if len(line) < 4:
			person = line
			continue
		elif ' ' in line:
			person = line
			continue
		if person:	
			new.append(person + ': ' + line)
	return new

def write_file(file_name, lines):
	with open(file_name, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = converts(lines)
	write_file('output.txt', lines)


main ()



