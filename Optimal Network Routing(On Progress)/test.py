# Optimal Network Routing
import sys
class Graph():

	def __init__(self, graph):
		self.graph = graph

	def findMinEffort(self, efforts, mepSet):

		min = sys.maxsize
		min_index = 0

		for v in range(len(self.graph[0])):
			if efforts[v] < min and mepSet[v] == False: 
				min = efforts[v] 
				min_index = v 

		return min_index 


	def getEffort(self):
		N = len(self.graph)
		M = len(self.graph[0])
		efforts = [sys.maxsize]*M
		efforts[0] = 0
		mepSet = [False]*M
		v = self.graph[0][0]

		for row in range(N):

			# u = self.findMinEffort(v, efforts, mepSet)
			mepSet[u] = True
			min = sys.maxsize
			for col in range(M):
				print("Paths =>",v,"->",u)
				if(mepSet[col] == False and abs(self.graph[u][col] - v) < min):
					efforts[col] = self.graph[u][col] - v
					v = self.graph[u][col]
		return sum(map(abs,efforts))

def getMinEffort(C):
	g = Graph(C)
	return g.getEffort()

if __name__ == "__main__":
	grid = [[5,1,3,2],[7,4,1,8],[6,7,5,9]]
	# grid = [[12, 6, 5, 3],[6, 13, 3, 15],[8, 2, 6, 9]] 
	print(getMinEffort(grid))
