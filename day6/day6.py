import os

def main():

	queueOf14 = [] 
	line = [l.strip() for l in open(os.getcwd() + "/input6.txt")]
	line = line[0]

	for i in range(len(line)):
		tempSet = list(set(queueOf14))
		if len(tempSet) == 14:
			print(i)
			return 1

		if i >= 14:
			queueOf14.pop(0)
			queueOf14.append(line[i])
			
		else:
			queueOf14.append(line[i])
		
	return 0


if __name__ == "__main__":
	main()
