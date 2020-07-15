# # Optimal Network Routing
# import sys
# class Graph():

# 	def __init__(self, graph):
# 		self.graph = graph

# 	def getEffort(self):
# 		print("Started...")
# 		v = self.graph[0][0]
# 		effort = 0
# 		dr = [-1, +1, 0, 0]
# 		dc = [0, 0, +1, -1]
# 		N = len(self.graph)
# 		M = len(self.graph[0])
# 		mepSet = [False]*300
# 		r = 0
# 		c = 0
# 		n = 0
# 		while(n < N*M):
# 			if(r >= N and c>= M):
# 				return effort
# 			min = sys.maxsize
# 			for i in range(4):
# 				rr = r + dr[i]
# 				cc = c + dc[i]
# 				if rr >= 0 and rr < N and cc >= 0 and cc < M and (self.graph[rr][cc] - v) < min and mepSet[i] == False:
# 					r = rr
# 					c = cc
# 					min = abs(self.graph[rr][cc] - v)
# 			effort += abs(self.graph[r][c] - v)
# 			v = self.graph[r][c]
# 			mepSet[n] = True
# 			n += 1
# 		return effort

# def getMinEffort(C):
# 	g = Graph(C)
# 	return g.getEffort()

# if __name__ == "__main__":
# 	grid = [[5,1,3,2],[7,4,1,8],[6,7,5,9]]
# 	# grid = [[12, 6, 5, 3],[6, 13, 3, 15],[8, 2, 6, 9]] 
# 	print(getMinEffort(grid))

