import os

def main():
	alphaDict = {}
	for i in range(97,123):
		alphaDict[chr(i)] = False

	line = [l.strip() for l in open(os.getcwd() + "/input6.txt")]
	line = line[0]

	# counter = 0
	# for i in range(len(line)):
	# 	if alphaDict[line[i]]:
	# 		continue
	# 	if alphaDict[line[i]] == False:
	# 		# this is a new character found
	# 		counter += 1
	# 		alphaDict[line[i]] = True
	# 		if counter == 4:
	# 			print(i+1)
	# 			return 0

	for i in range(3,len(line)):
		if line[i-3] != line[i-2] and line[i-3] != line[i-1] and line[i-3] != line[i] and line[i-2] != line[i-1] and line[i-2] != line[i] and line[i-1] != line[i]:
			print(i+1)
			return 1
		
	return 0


if __name__ == "__main__":
	main()
