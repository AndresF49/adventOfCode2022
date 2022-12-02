'''
First col is Opponent move A for Rock, B for Paper, and C for Scissors. The second column is what you play in reseponse, X for Rock, Y for Paper, and Z for Scissors.

Total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

part 2
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
'''

import os

def main():

	totalScore = 0

	with open((os.getcwd() + "/day2/input2.txt"), 'r') as file:
		readline=file.read().splitlines()
		for line in readline:
			opPlay = line[0]
			myPlay = line[2]

			# part 1
			# if opPlay == 'A': # rock
			# 	if myPlay == 'X': # rock & tie
			# 		totalScore += (1 + 3)
			# 	elif myPlay == 'Y': # paper
			# 		# win
			# 		totalScore += (2 + 6)
			# 	else:
			# 		# scissors & loss
			# 		totalScore += (3 + 0)
			# elif opPlay == 'B': # paper:
			# 	if myPlay == 'X': # rock & loss
			# 		totalScore += (1 + 0)
			# 	elif myPlay == 'Y': # paper & tie
			# 		# win
			# 		totalScore += (2 + 3)
			# 	else:
			# 		# scissors & win
			# 		totalScore += (3 + 6)
			# else: # scissors
			# 	if myPlay == 'X': # rock & win
			# 		totalScore += (1 + 6)
			# 	elif myPlay == 'Y': # paper & loss
			# 		# win
			# 		totalScore += (2 + 0)
			# 	else:
			# 		# scissors & tie
			# 		totalScore += (3 + 3)

			# part 2
			if opPlay == 'A': # rock
				if myPlay == 'X': # lose - so we choose scissors
					totalScore += (3 + 0)
				elif myPlay == 'Y': # tie - choose rock
					totalScore += (1 + 3)
				else:
					# win - choose paper
					totalScore += (2 + 6)
			elif opPlay == 'B': # paper:
				if myPlay == 'X': # lose - choose rock
					totalScore += (1 + 0)
				elif myPlay == 'Y': # tie - choose paper
					totalScore += (2 + 3)
				else:
					# win - choose scissors
					totalScore += (3 + 6)
			else: # scissors
				if myPlay == 'X': # lose - chose paper
					totalScore += (2 + 0)
				elif myPlay == 'Y': # draw - choose scissors
					totalScore += (3 + 3)
				else:
					# win - choose rock
					totalScore += (1 + 6)

	print(totalScore)

	return 0

if __name__ == "__main__":
	main()