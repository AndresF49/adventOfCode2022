def main():
	stackArr = []
	stackArr.append(['N', 'C', 'R', 'T', 'M', 'Z', 'P'])
	stackArr.append(['D', 'N', 'T', 'S', 'B', 'Z'])
	stackArr.append(['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'])
	stackArr.append(['G', 'R', 'Z'])
	stackArr.append(['Z', 'N', 'R', 'H'])
	stackArr.append(['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'])
	stackArr.append(['W', 'D', 'Z', 'R', 'C', 'G', 'M'])
	stackArr.append(['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'])
	stackArr.append(['S', 'Q', 'P', 'W', 'N'])
	# print(stackArr)
	# return 1

	# for i in range(len(stackArr)):
	# 	print(f"Stack {i + 1}: {stackArr[i]}")
	# return 0

	line = [l.strip() for l in open("input5.txt")]
	for row in range(10, len(line)):
		# print(line[row])
		amountToMove = int(line[row][4:line[row].index(' ', 5)].strip())
		newStr = line[row][9:]
		stackToEmpty = int(newStr[newStr.index(' ') + 1:newStr.index('to ')])
		stackToFill = int(newStr[newStr.index('to ') + 3])

		outer = 0
		while outer < amountToMove:
			# stackArr[stackToFill]
			# stackArr[stackToEmpty]
			stackArr[stackToFill-1].append(stackArr[stackToEmpty-1].pop())
			outer += 1
			# print(stackArr)
			# print(outer)

	ans = ""

	for i in range(len(stackArr)):
		ans += stackArr[i][-1]

	print(ans)
	return 0


if __name__ == "__main__":
	main()
