



if __name__ == "__main__":

	ranked = [100,100,90,90,80,75,60]
	player = [50,65,77,90,102]

	ranks = [1]
	ranks_player = []
	for i in range(1,len(ranked)):
		t = ranks[-1]
		if ranked[i] == ranked[i-1] :
			ranks.append(t)
		else:
			t +=1 
			ranks.append(t)
	
	merged = [[x,y] for x,y in zip(ranks,ranked)]
	
	for score in player:
		rank_one = 0
		for i in range(len(ranked)-1,-1,-1):
			if merged[i][1] < score:
				rank_one+=1
				continue
			elif merged[i][1] == score:
				ranks_player.append(merged[i][0])
				break
			elif merged[i][1] > score:
				ranks_player.append(merged[i][0]+1)
				break
	print(rank_one)
	if rank_one == len(ranked):
		ranks_player.append(1)

	print(ranks_player)