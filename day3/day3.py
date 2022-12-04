def findCommonletter(sack1,sack2,sack3):
	dict = {}

	for i in range(65, 91):
			dict.update({chr(i): [0,0,0]})
			dict.update({(chr(i + 32)): [0,0,0]})

	for let in sack1:
		dict[let][0] += 1
	for let in sack2:
		dict[let][1] += 1
	for let in sack3:
		dict[let][2] += 1

	for key,val in dict.items():
		if val[0] and val[1] and val[2]:
			return key


def main():
	total = 0
	line = [l.strip() for l in open("input3.txt")]

	for index in range(0,len(line),3):
	# for word in line:
		
		dict = {}
		letterUsed = ''

		for i in range(65, 91):
			dict.update({chr(i): 0})
			dict.update({(chr(i + 32)): 0})

		sack1 = line[index]
		sack2 = line[index+1]
		sack3 = line[index+2]
		
		# for k in range(3):
		# 	# firstPart = line[index + k][:int(len(line[index + k]) / 2)]
		# 	# secondPart = line[index + k][int(len(line[index + k]) / 2):]
			
	
		# 	for let in firstPart:
		# 		dict[let] += 1
	
		# 	for let in secondPart:
		# 		if dict[let] == 3:
		# 			# letter was identifier and is shared
		# 			letterUsed = let
		# 			break

		letterUsed = findCommonletter(sack1,sack2,sack3)

		if ord(letterUsed) >= 97 and ord(letterUsed) <= 122:
			total += (ord(letterUsed) - 96)
			# lowercase 97-122 (1-26)

		if ord(letterUsed) >= 65 and ord(letterUsed) <= 90:
			total += (ord(letterUsed) - 38)
			# uppercase 65-90 (27-52)

	print(total)
	return 0


if __name__ == "__main__":
	main()
