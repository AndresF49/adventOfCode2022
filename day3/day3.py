def main():
	total = 0
	line = [l.strip() for l in open("input3.txt")]
	for word in line:
		dict = {}
		letterUsed = ''

		for i in range(65, 91):
			dict.update({chr(i): False})
			dict.update({(chr(i + 32)): False})

		firstPart = word[:int(len(word) / 2)]
		secondPart = word[int(len(word) / 2):]

		for let in firstPart:
			dict[let] = True

		for let in secondPart:
			if dict[let]:
				# letter was used already and is shared
				letterUsed = let
				break

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
