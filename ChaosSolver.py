import sys
import random
from random import randint

num_args = len(sys.argv)

if num_args < 3 or num_args > 4:
	print("Invalid number of arguments")
	print(">ChaosSolver.py <simulations> <players>")
	print("or")
	print(">ChaosSolver.py <simulations> <lower-player-range> <upper-player-range>")
	exit(1)

num_runs = int(sys.argv[1])
lower_range = int(sys.argv[2])
if num_args == 3:
	upper_range = lower_range + 1
else:
	upper_range = int(sys.argv[3])

print("")

for num_players in range(lower_range, upper_range):
	runList = []
	for i in range(num_runs):

		# Players are stored by int alone, first line
		# makes the player list
		activePlayers = [i for i in range(num_players)]

		# Make an empty array for each player which will
		# later store the players they've captured
		playerCaptures = [[] for i in range(num_players)]

		tag_count = 0
		while len(activePlayers) > 1:

			# Get a random player
			tagged_player = activePlayers[randint(0, len(activePlayers) - 1)]

			# Remove the player from active players
			activePlayers.remove(tagged_player)

			# Randomly select a tagging player
			tagging_player = random.choice(activePlayers)

			# Add the tagged player to the tagging players
			# capture list
			playerCaptures[tagging_player].append(tagged_player)
			
			tag_count += 1
							
			"""
			Optional Debugging Output
			print("")
			print(activePlayers)
			print(tagged_player)
			print(tagging_player)
			print(playerCaptures)
			"""

			# Return all players captured by the tagged player
			activePlayers += playerCaptures[tagged_player]

			# Update the tagged players capture list to empty
			playerCaptures[tagged_player] = [] 

		runList.append(tag_count)

	sum = 0
	for i in runList:
		sum += i	

	print(num_players, sum / num_runs)
