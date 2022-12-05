import os

def main():
	totalFullyContained = 0
	line = [l.strip() for l in open(os.getcwd() + "/day4/input4.txt")]
	for chore in line:
		chore = chore.split(',')
		# print(chore)
		firstPairLeft = chore[0][0:chore[0].find('-')]
		firstPairRight = chore[0][chore[0].find('-')+1:]
		secPairLeft = chore[1][0:chore[1].find('-')]
		secPairRight = chore[1][chore[1].find('-')+1:]

		# print(f"{firstPairLeft} {firstPairRight} | {secPairLeft} {secPairRight}")

		s1 = set(range(int(firstPairLeft),int(firstPairRight)+1))
		s2 = set(range(int(secPairLeft),int(secPairRight)+1))

		if s1.intersection(s2):
			# print(f"{firstPairLeft} {firstPairRight} | {secPairLeft} {secPairRight}")
			totalFullyContained += 1
# 		else:
# 			print(f"{firstPairLeft} {firstPairRight} | {secPairLeft} {secPairRight}")
		# print(f"{firstPairLeft} {firstPairRight} {secPairLeft} {secPairRight}")

		# if firstPairLeft <= secPairLeft and firstPairRight >= secPairRight:
		# 	totalFullyContained += 1
		# elif secPairLeft <= firstPairLeft and secPairRight >= firstPairRight:
		# 	totalFullyContained += 1
	
	print(totalFullyContained)
	# 841 is too low

		
if __name__ == "__main__":
	main()
