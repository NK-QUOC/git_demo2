
import math
import os
import random
import re
import sys
import timeit
import datetime

def climbingLeaderboard(ranked, player):
    scores = set(ranked)
    scores = list(scores)
    scores.sort(reverse = True)
    
    rank_history = []
    index = 0
    rank = len(scores)-1
    while index < len(player):
        while rank >= 0:
            if rank >= len(scores):
                rank -=1
            if player[index] == scores[rank]:
                rank_history.append(rank)
                rank = rank
                break
            elif player[index] < scores[rank]:
                rank_history.append(rank+1)
                rank = rank+1
                break
            elif player[index] > scores[rank]:
                if rank == 0:
                    rank_history.append(0)
                    break
                else:
                    rank-=1
        index += 1    

    rank_history = list(map(lambda x : x+1 ,rank_history))
    
    return rank_history

def climbingLeaderboard_1(ranked, player):
 
	scores = set(ranked)
	scores = list(scores)
	scores.sort(reverse = True)
	ranks_player = list(range(1,len(scores)+1))			
	
	table_rank = [[x,y] for x,y in zip(ranks_player,scores)]	
	table_rank.sort(reverse=True)

	# print(table_rank)
	rank_history = []
	for score_player in player : 
		rank_temp = None
		for rank, score in table_rank:
			if score_player == score :
				rank_history.append(rank)
				rank_temp = None
				break 
			elif score_player < score : 
				rank_history.append(rank+1)
				rank_temp = None
				break
			elif score_player > score :
				rank_temp = rank 
		if rank_temp != None:
			rank_history.append(1)

	return rank_history


if __name__ == "__main__":
    
	with open('input.txt') as f:
		datalist = f.readlines()
	
	ranked_count = int(datalist[0].rstrip("\n"))
	# print(ranked_count)
	ranked = list(map(int, datalist[1].rstrip().split()))
	# print(ranked)
	player_count = int(datalist[2].strip())
	player = list(map(int, datalist[3].rstrip().split()))
	# ranked = [100,100,50,40,40,20,10]
	# player = [5,25,50,120]

	result = climbingLeaderboard(ranked,player)
	print(result)
	execution_time = timeit.timeit(lambda : climbingLeaderboard(ranked,player), number=1000)
	print("Execution time:", execution_time)
