'''
Question : 
Given a weighted graph G, first find a subgraph H of G such that all vertices of H have the same weight 
and the number of vertices in H is maximized. Then find a minimum spanning tree of H such that the total edge weights 
is minimized. Write a program to solve this problem. You can use C++, Java or Python programming language. The input 
is a weighted graph G described by an adjacent list. Each vertex of G has an integer weight in the range of [1, floor(n/10)], 
where n is the number of vertices in G. Each edge has an integer weight in the range of [1,10n]. 
'''


class Graph:

    def __init__(self,V):
        self.V = V
        self.adj = [ [] for i in range(V) ]
        self.graph = [] 
    

    def DFSUtil( self, temp, v, visited ) :
        visited[v] = True
        temp.append(v)

        for i in self.adj[v] :
            if visited[i] == False :
                temp = self.DFSUtil( temp, i, visited )
        
        return temp


    def addEdge( self, v, u) :
        self.adj[v].append(u)
        self.adj[u].append(v)
        
    
    def vertex_weight(self,gvw):
        gvw_obj={}

        for ele in gvw:
             gvw_obj.setdefault(ele[1],[]).append(ele[0])
        
        return gvw_obj
    

    def vertex_weight_len( self, gvw ) :
        gvw_len=[]

        for k in gvw :
            gvw_len.append( (len(gvw[k]) , k ))
        
        return sorted( gvw_len, reverse = True )
        

    def findEdges( self, v_list, edge_set ) :
        i=0
        j=0
        e_list=[]
        es = edge_set

        while i < ( len(v_list) - 1 ) : 
            v = v_list[i]
            j = i+1
            while j < len(v_list) :

                if ( ( [ v, v_list[j] ] ) in es ) :
                    e_list.append( [ v, v_list[j] ] )

                j=j+1
            i=i+1
        
        return e_list
    

    def addWeightEdge(self, v_list, edge_set, w_graph):
        
        ed_l = self.findEdges( v_list, edge_set )
        for el in ed_l :
            self.graph.append([el[0], el[1], w_graph[(el[0],el[1])] ])
        
        val = self.KruskalMST()
        self.graph=[]
        return val


    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    
    def KruskalMST(self):
 
        result = []
        i = 0  
        e = 0
 
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
 
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        while (e < self.V - 1) and ( i < len( self.graph ) ) :
 
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
 
        minimumCost = 0
        # print( "Edges in the constructed MST" )
        
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        
        print("Minimum Spanning Tree" , minimumCost)
        temp_v=minimumCost
        # print(' temp_v {} '.format( temp_v ))
        return temp_v

    
    def m_connectedComponents( self, ed_l, tup_l ,ed_s, w_graph ) :
        
        visited = []
        cc = []
        mst = []
        
        for i in range(self.V) :
            visited.append(False)
        
        for v in range(self.V) :
            if visited[v] == False :
                temp = []
                t = self.DFSUtil(temp,v,visited)
                x = self.addWeightEdge(t,ed_s,w_graph)
                mst.append( (x,t) )
                cc.append(t)
        
        #returning the maximum value
        return mst
                

if __name__ == "__main__" :

    temp_graph_vertex_weight = [(0,1),(1,2),(2,2),(3,1),(4,2),(5,1),(6,2),(7,2)]

    temp_graph={
        
        0:[[1,3]],
        1:[[2,1],[7,2]],
        2:[[1,1],[7,1],[3,2]],
        3:[[2,2],[4,1]],
        4:[[3,1],[5,1]],
        5:[[4,1],[6,1]],
        6:[[7,2],[5,1]],
        7:[[1,2],[2,1],[6,2]]
    
    }
    weight_edge_graph = {}

    g_size = len( temp_graph )
    g = Graph( g_size )

    edge_set = []
    weight_edge_set = []
    mst=[]

    for k in temp_graph : 
        for ele in temp_graph[k] :
            edge_set.append([k,ele[0]])
            weight_edge_set.append( [ k, ele[0], ele[1] ] )
    
    for k in temp_graph :
        for ele in temp_graph[k] :
            weight_edge_graph[(k, ele[0])] = ele[1]


    print( 'edge_set => {} '.format( edge_set ) )
    # edge_set => [[0, 1], [1, 2], [1, 7], [2, 1], [2, 7], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4], [5, 6], [6, 7], [6, 5], [7, 1], [7, 2], [7, 6]] 

    print( 'weight_edge_set => {} '.format( weight_edge_set ) )
    # weight_edge_set => [[0, 1, 3], [1, 2, 1], [1, 7, 2], [2, 1, 1], [2, 7, 1], [2, 3, 2], [3, 2, 2], [3, 4, 1], [4, 3, 1], [4, 5, 1], [5, 4, 1], [5, 6, 1], [6, 7, 2], [6, 5, 1], [7, 1, 2], [7, 2, 1], [7, 6, 2]]   

    print( 'weight_edge_graph => {} '.format( weight_edge_graph ) ) 
    # weight_edge_graph => {(0, 1): 3, (1, 2): 1, (1, 7): 2, (2, 1): 1, (2, 7): 1, (2, 3): 2, (3, 2): 2, (3, 4): 1, (4, 3): 1, (4, 5): 1, (5, 4): 1, (5, 6): 1, (6, 7): 2, (6, 5): 1, (7, 1): 2, (7, 2): 1, (7, 6): 2} [(5, 2), (3, 1)]


    # print( g.vertex_weight ( temp_graph_vertex_weight ) )

    len_tup = g.vertex_weight_len( g.vertex_weight(  temp_graph_vertex_weight ) )

    gvw_obj = g.vertex_weight(  temp_graph_vertex_weight )

    print( len_tup )

    for ele in len_tup :
        # ele = ( count, weight )
        edge_list = g.findEdges( gvw_obj[ele[1]] , edge_set )
        
        print( 'edge_list => {} '.format( edge_list ) )
        for ed in edge_list :
            g.addEdge( ed[0], ed[1] )
            # print(u,v)

        mst_list = g.m_connectedComponents( edge_list, len_tup ,edge_set, weight_edge_graph )
        
        for v in mst_list :
            if v[0]:
                mst.append(v)

        # len_weight_list.append((k,max_cc_len))
        g.adj = [ [] for i in range(g_size) ]  
        # mst.remove(0)

    print(' mst = >  {}  '.format(mst))

    mst_vtx = (min(mst))[1]
    mst_wgt = (min(mst))[0]

    print('\n\n\n')
    print('\n---------------------------------------------------------------------------\n')

    print('The Graph with vertices {}'.format( g_size ))
    print('Vertices in MST are {} with total weight {}'.format( mst_vtx, mst_wgt) )
    
    print('\n---------------------------------------------------------------------------\n')
    print('\n\n\n')
