from collections import defaultdict
import streamlit as st

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
class UndirectedGraph():
    def __init__(self,n):
        self.n=n
        self.graph=defaultdict(list)
        self.output=[]
    
    def addEdge(self,u,v):
        self.output.append("Creating node from {} to {}".format(u,v))
        self.output.append("Creating node from {} to {}".format(v,u))
        self.graph[u].append(v)
        self.graph[v].append(u)

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
            elif parent!=i:
                self.output.append("If adjacent node is visited, checking wether this node is parent or not Node {} != Parent Node {}]".format(i,parent))
                return True

        self.output.append("No cycle detected")
        return False


    


