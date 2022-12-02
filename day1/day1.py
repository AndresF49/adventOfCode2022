'''
Each number is the # of calories each elf is carrying

Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

'''
import os
# print(os.getcwd())

def main():
	max = -999999999999999
	topThree = [max,max,max,max]

	with open((os.getcwd() + "/day1/input1.txt"), 'r') as file:
		localSum = 0
		for line in file:
			# print(line, end = " ")
			if line == '\n':
				# print("newline found")
				for i in range(2):
					if topThree[i] < localSum:
						if i == 0:
							topThree[i+2] = topThree[i+1]
							topThree[i+1] = topThree[i]
							topThree[i] = localSum
							break
						elif i == 1:
							topThree[i+2] = topThree[i+1]
							topThree[i] = localSum
							break
						else:
							topThree[i] = localSum
							break
				
				# if max < localSum:
				# 	max = localSum
				localSum = 0
			elif line != "":
				localSum += int(line)
			

	print(f"Top three calories are: {topThree[0]} {topThree[1]} {topThree[2]}", end="\n")
	print(f"Sum is: {topThree[0]+topThree[1]+topThree[2]}")
	return 0

if __name__ == "__main__":
	main()