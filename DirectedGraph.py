from collections import defaultdict
import streamlit as st

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class unweightedDirectedGraph():
    def __init__(self,n):
        self.n=n
        self.graph=defaultdict(list)
        self.output=[]
    
    def addEdge(self,u,v):
        self.output.append("Creating node from {} to {}".format(u,v))
        self.graph[u].append(v)

    def BFS(self,u):
        self.output.append("BFS Start")
        self.output.append("Creating visited array that will contain check wether node is visited or not")
        visited=[False]*self.n
        self.output.append("Creating queue")
        queue=[]
        self.output.append("Enqueue node {} in queue".format(u))
        queue.append(u)
        self.output.append("Marking node {} is visited".format(u))
        visited[u]=True
        while queue:
            self.output.append("Dequeue the queue")
            node=queue.pop(0)
            self.output.append("Node is {}".format(node))
            self.output.append("Looking for all adjacent vertices")
            for i in self.graph[node]:
                self.output.append("Checking the adjacent node {} is visited or not ".format(i))
                if visited[i]==False:
                    self.output.append("Visiting adjacent node")
                    visited[i]=True
                    queue.append(i)
                    self.output.append("Enqueue node in queue -> {}".format(queue))
    
    def _dfs(self,node,visited):
        self.output.append("Marking node {} visited".format(node))
        visited[node]=True
        self.output.append("Looking for all adjacent vertices")
        for i in self.graph[node]:
            self.output.append("Checking the adjacent node {} is visited or not ".format(i))
            if visited[i]==False:
                self.output.append("Starting dfs for {} node ".format(i))
                self._dfs(i,visited)
        
    def DFS(self,u):
        self.output.append("DFS Start")
        self.output.append("Creating visited array that will contain check wether node is visited or not")
        visited=visited=[False]*self.n
        self._dfs(u,visited)

    def cycleCheck(self):
        self.output.append("Cycle check Start")
        self.output.append("Creating visited array that will contain check wether node is visited or not")
        visited=[False]*self.n
        self.output.append("Looping for each and every node in graph")
        for i in range(0,self.n):
            self.output.append("Checking wether node {} is visited or not ".format(i))
            if visited[i]==False:
                self.output.append("Checking for node {} wether it has cycle or not".format(i))
                if self._cycleCheck(i,visited,-1):
                    self.output.append("Cycle Detected")
                    return True
        self.output.append("No cycle detected")
        return False


    def _cycleCheck(self,node,visited,parent):
        self.output.append("Marking current node as visited")
        visited[node]=True
        self.output.append("Looking for all adjacent vertices")
        for i in self.graph[node]:
            self.output.append("Checking the adjacent node {} is visited or not ".format(i))
            if visited[i]==False:
                self.output.append("Checking for node {} wether it has cycle or not".format(i))
                if self._cycleCheck(i,visited,node):
                    
                    return True
            elif visited[i]==True:
                self.output.append("Adjacent node is visited")
                
                return True

        
        return False


    
@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class weightedDirectedGraph():
    def __init__(self,n):
        self.n=n
        self.graph=defaultdict(list)
        self.output=[]
    
    def addEdge(self,u,v,w):
        self.output.append("Creating node from {} to {} having weight {}".format(u,v,w))
        self.graph[u].append([v,w])
    
    def listToMatrix(self):
        self.matrix=[[0 for i in range(self.n)] for j in range(self.n)]
        for u in self.graph:
            for v,w in self.graph[u]:
                self.matrix[u][v]=w
        
    
    def BFS(self,u):
        self.output.append("BFS Start")
        self.output.append("Creating visited array that will contain check wether node is visited or not")
        visited=[False]*self.n
        self.output.append("Creating queue")
        queue=[]
        self.output.append("Enqueue node {} in queue".format(u))
        queue.append(u)
        self.output.append("Marking node {} is visited".format(u))
        visited[u]=True
        while queue:
            self.output.append("Dequeue the queue")
            node=queue.pop(0)
            self.output.append("Node is {}".format(node))
            self.output.append("Looking for all adjacent vertices")
            for i in self.graph[node]:
                self.output.append("Checking the adjacent node {} is visited or not ".format(i[0]))
                if visited[i[0]]==False:
                    self.output.append("Visiting adjacent node")
                    visited[i[0]]=True
                    queue.append(i[0])
                    self.output.append("Enqueue node in queue -> {}".format(queue))
    
    def _dfs(self,node,visited):
        self.output.append("Marking node {} visited".format(node))
        visited[node]=True
        self.output.append("Looking for all adjacent vertices")
        for i in self.graph[node]:
            self.output.append("Checking the adjacent node {} is visited or not ".format(i[0]))
            if visited[i[0]]==False:
                self.output.append("Starting dfs for {} node ".format(i[0]))
                self._dfs(i[0],visited)
        
    def DFS(self,u):
        self.output.append("DFS Start")
        self.output.append("Creating visited array that will contain check wether node is visited or not")
        visited=visited=[False]*self.n
        self._dfs(u,visited)
    
    def cycleCheck(self):
        self.output.append("Cycle check Start")
        self.output.append("Creating visited array that will contain check wether node is visited or not")
        visited=[False]*self.n
        self.output.append("Looping for each and every node in graph")
        for i in range(0,self.n):
            self.output.append("Checking wether node {} is visited or not ".format(i))
            if visited[i]==False:
                self.output.append("Checking for node {} wether it has cycle or not".format(i))
                if self._cycleCheck(i,visited,-1):
                    self.output.append("Cycle Detected")
                    return True
        self.output.append("No cycle detected")
        return False


    def _cycleCheck(self,node,visited,parent):
        self.output.append("Marking current node as visited")
        visited[node]=True
        self.output.append("Looking for all adjacent vertices")
        for i in self.graph[node]:
            self.output.append("Checking the adjacent node {} is visited or not ".format(i[0]))
            if visited[i[0]]==False:
                self.output.append("Checking for node {} wether it has cycle or not".format(i[0]))
                if self._cycleCheck(i[0],visited,node):
                    
                    return True
            elif visited[i[0]]==True:
                self.output.append("Adjacent node is visited")
                
                return True

        
        return False

    def mindist(self,dist,sptset):
        mini=float("inf")
        for i in range(0,self.n):
            if mini>dist[i] and sptset[i]==False:
                mini=dist[i]
                min_index=i
        return min_index
  
    def Dijkstra(self,src):
        self.output.append("Creating a distance array")
        dist=[2*10**31]*self.n 
        dist[src]=0
        self.output.append("Creating visited array that contain wether node is visited or not")
        sptset=[False]*self.n
        for _ in range(self.n):
            self.output.append("Finding node which has min distance fromm source node")
            u=self.mindist(dist,sptset)
            self.output.append("Min distance node is {}".format(u))
            self.output.append("Marking min distance node as True")
            sptset[u]=True
            self.output.append("Traversing adjacent nodes")
            for node,weight in self.graph[u]:
                self.output.append("Checking adjacent node {} is visited or not".format(node))
                if sptset[node]==False:
                    self.output.append("Updating value of distance array")
                    dist[node]=min(dist[node],dist[u]+weight)
            self.output.append("After updating distance array for min distance node {} -> {}".format(u,dist))

        
        for node,distance in enumerate(dist):
            if distance == 2*10**31:
                distance="No Edge"
            self.output.append("Min distance of node {} from source {} is {}".format(node,src,distance))


    def BellmanFord(self, src): 

            self.output.append("Creating a distance array")
            dist = [float("Inf")] * self.n
            dist[src] = 0

            self.output.append("Traverse all edges |{}| - 1 times. A simple shortest path from src to any other vertex can have at-most |{}| - 1 edges ".format(self.n,self.n))
            for _ in range(self.n- 1): 
                self.output.append("Looping adjacency list for updating distance array")
                for u in self.graph:
                    for v,w in self.graph[u]:
                        if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                                dist[v] = dist[u] + w
                self.output.append("Distance array is {}".format(dist))
            
            self.output.append("Checking for negative weight cycle")
            for u in self.graph:
                for v,w in self.graph[u]:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                            self.output.append("Graph contains negative weight cycle")
                            return
                            
            for node,distance in enumerate(dist):
                if distance == float("inf"):
                    distance="No Edge"
                self.output.append("Min distance of node {} from source {} is {}".format(node,src,distance))
    

    def Prims(self):
        self.listToMatrix()
        self.output.append("Creating array of key value for all nodes in graph.Intially all value is infinite")
        key=[2*10**31]*self.n
        self.output.append("Creating array checking wether this node is in Minimum Spanning Tree or not")
        mst=[False]*self.n
        key[0]=0
        self.output.append("Creating parent array that will keep track of node connection")
        parent=[0]*self.n
        parent[0]=-1

        for _ in range(self.n):

            minnum=2*10**31
            self.output.append("Finding minimum key value from key array")
            for k in range(self.n): 
                if key[k]<minnum and mst[k]==False:
                    minnum=key[k]
                    u=k
            self.output.append("Minimum key value for node {} is {} ".format(u,key[u]))
            mst[u]=True
            self.output.append("Marking node as visited")

            self.output.append("Traversing each node to find minimum key value")
            for j in range(self.n):
                self.output.append("Checking wether node {} is connected to min key node {} and included in visited array or not and key value of node {} is less than weight of edge {}-{}".format(j,u,j,u,j))
                if self.matrix[u][j]>0 and mst[j]==False and key[j]>self.matrix[u][j]:
                    self.output.append("Updating key value of node {} and inserting value in parent array ".format(j))
                    key[j]=self.matrix[u][j]
                    parent[j]=u
        
        self.output.append("Minimum Spanning Tree is formed")
        print(parent)
        print(self.matrix)
        for i in range(1, self.n):
            self.output.append("Edge {}-{} Weight {}".format(parent[i], i, self.matrix[i][parent[i]]))

    

    def inDegree(self):
        arr=[0]*self.n
        for i in self.graph:
            for j,w in self.graph[i]:
                arr[j]+=1
        return arr
    
    def topologicalSort(self):
        self.output.append("Storing in degree of all vertices in array")
        arr=self.inDegree()
        self.output.append("Creating a queue")
        queue=[]
        self.output.append("Appending all nodes which have in degree zero")
        for i in range(0,len(arr)):
            if arr[i]==0:
                queue.append(i)
        
        
        while queue:
            self.output.append("Dequeue from queue")
            node=queue.pop(0)
            self.output.append("Node is {}".format(node))
            self.output.append("Traversing all adjacent nodes of {}".format(node))
            for u,w in self.graph[node]:
                self.output.append("Reducing in  degree of node {} by 1 and enqueue in queue".format(u))
                arr[u]-=1
                if arr[u]==0:
                    queue.append(u)
    
        





