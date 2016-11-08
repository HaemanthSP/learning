6.006 Introduction to Algorithms Recitation 13 October 28, 2011
Review on Graphs Handshaking Lemma
In a party, people shook hands with each other. The sum of the number of times each person shook
hands must be even. This can be proven by proving the handshaking lemma: if G = (V, E) is an
undirected graph, then   degree(v) = 2|E|. v∈V
Proof. The degree of a vertex in an undirected graph is the number of edges incident on it. For example, in Figure 1, The degree of node 1 is 2 and the degree of node 2 is 3. Consider a particular, but arbitrarily chosen edge ek = (vi, vj ) ∈ E; it contributes a count of 1 each to deg(vi) and deg(vj) and hence a count of 2 to the total degree. Hence, |E| edges contribute 2|E| to the total degree. Each vertex represents a person and an edge (ui , uj ) represents ui and uj shook hands. The sum of hand-shakes is the sum of the vertex-degrees which is even.
Path
Apathoflengthkfromavertexutoavertexu′ inagraphG=(V,E)isasequence⟨v0,v1,v2,...,vk⟩ of vertices such that u = v0, u′ = vk, and (vi−1,vi) ∈ E for i = 1,2,...,k. There is always a 0-length path from u to u. If there is a path p from u to u′, we say that u′ is reachable from u via
p. If there is no path from u to u′, the distance from u to u′ is infinity.
Graph Representation
In addition to the representations shown during the lecture: adjacency lists, object-oriented vari- ations and implicit representations, there is another way to represent a graph, called adjacency matrix.
Adjacency Matrix
For a graph G = (V, E), we assume that the vertices are numbered 1, 2, . . . |V | in some arbitrary order. Then the adjacency matrix representation of G consists of a |V | × |V | matrix A = (aij ) such that
 1, if(i,j)∈E, aij = 0, otherwise .
This matrix can be stored as an array of arrays, and it requires Θ(V 2) memory, independent of the number of the edges in the graph. Figure 1 shows the adjacency matrix of an undirected graph. Observe the symmetry along the main diagonal of the matrix. In some applications, it pays to store only the entries on and above the diagonal of the adjacency matrix, thereby cutting the memory needed to store the graph almost in half.
 1
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
     12345
  1 2 3 4 5
         01001 10111 01010 01101 11010
      12
54
3
            Figure 1: Adjacency matrix representation of an undirected graph.
Representation Tradeoffs
Space:
• Adjacency lists uses one node per edge, and two machine words per node. So space is
Θ(Ew) bits (w = word size).
• Adjacency matrix uses V 2 entries, but each entry can be just one bit. So space can be Θ(V 2)
bits. Time:
• Add an edge: both data structures are O(1).
• Find if there is an edge from u to v: matrix is O(1), and adjacency list must be scanned.
• Visitallneighborsofv(verycommon):matrixisΘ(V),andadjacencylistisO(neighbors). This means BFS will take O(V 2) time if we use adjacency matrix representation.
• Remove an edge: similar to find and add.
The adjacency list representation provides a compact way to represent sparse graphs – those for which |E| is much less than |V 2| – it is usually the method of choice. We may prefer an adjacency matrix representation, however, when the graph is dense – |E| is close to |V 2| – or when we need to be able to tell quickly if there is an edge connecting two given vertices.
Breadth First Search
Breadth first search (BFS) uses a queue to perform the search. A queue is a FIFO (first-in first- out) data structure. When we visit a node and add all the neighbors into the queue, then pop the next thing off of the queue, we will get the neighbors of the first node as the first elements in the queue. This comes about naturally from the FIFO property of the queue and ends up being an extremely useful property. Even thougth the implementation shown in the lecture does not use a queue explicitly, it still maintains the FIFO order of visiting the nodes.
The following is the Python implementation of a queue-based BFS.
2
1 2 3 4 5 6 7 8 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
def
def
__init__(self):
self.adj = {}
add_edge(self, u, v): if self.adj[u] is None:
    self.adj[u] = []
self.adj[u].append(v)
6.006 Introduction to Algorithms
from collections import deque
class BFSResult:
def __init__(self):
        self.level = {}
        self.parent = {}
class Graph:
Recitation 13
October 28, 2011
 def bfs(g, s):
’’’Queue-based implementation of BFS.
Args:
    g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
       neighbors.
    s: source.
’’’
r= BFSResult() r.parent = {s: None} r.level = {s: 0}
queue = deque()
queue.append(s)
while queue:
u = queue.popleft() for n in g.adj[u]:
return r
if n not in level: r.parent[n] = u
    r.level[n] = r.level[u] + 1
    queue.append(n)
3
MIT OpenCourseWare
http://ocw.mit.edu
6.006 Introduction to Algorithms Fall 2011
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
Review on Graphs Handshaking Lemma
In a party, people shook hands with each other. The sum of the number of times each person shook
hands must be even. This can be proven by proving the handshaking lemma: if G = (V, E) is an
undirected graph, then   degree(v) = 2|E|. v∈V
Proof. The degree of a vertex in an undirected graph is the number of edges incident on it. For example, in Figure 1, The degree of node 1 is 2 and the degree of node 2 is 3. Consider a particular, but arbitrarily chosen edge ek = (vi, vj ) ∈ E; it contributes a count of 1 each to deg(vi) and deg(vj) and hence a count of 2 to the total degree. Hence, |E| edges contribute 2|E| to the total degree. Each vertex represents a person and an edge (ui , uj ) represents ui and uj shook hands. The sum of hand-shakes is the sum of the vertex-degrees which is even.
Path
Apathoflengthkfromavertexutoavertexu′ inagraphG=(V,E)isasequence⟨v0,v1,v2,...,vk⟩ of vertices such that u = v0, u′ = vk, and (vi−1,vi) ∈ E for i = 1,2,...,k. There is always a 0-length path from u to u. If there is a path p from u to u′, we say that u′ is reachable from u via
p. If there is no path from u to u′, the distance from u to u′ is infinity.
Graph Representation
In addition to the representations shown during the lecture: adjacency lists, object-oriented vari- ations and implicit representations, there is another way to represent a graph, called adjacency matrix.
Adjacency Matrix
For a graph G = (V, E), we assume that the vertices are numbered 1, 2, . . . |V | in some arbitrary order. Then the adjacency matrix representation of G consists of a |V | × |V | matrix A = (aij ) such that
 1, if(i,j)∈E, aij = 0, otherwise .
This matrix can be stored as an array of arrays, and it requires Θ(V 2) memory, independent of the number of the edges in the graph. Figure 1 shows the adjacency matrix of an undirected graph. Observe the symmetry along the main diagonal of the matrix. In some applications, it pays to store only the entries on and above the diagonal of the adjacency matrix, thereby cutting the memory needed to store the graph almost in half.
 1
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
     12345
  1 2 3 4 5
         01001 10111 01010 01101 11010
      12
54
3
            Figure 1: Adjacency matrix representation of an undirected graph.
Representation Tradeoffs
Space:
• Adjacency lists uses one node per edge, and two machine words per node. So space is
Θ(Ew) bits (w = word size).
• Adjacency matrix uses V 2 entries, but each entry can be just one bit. So space can be Θ(V 2)
bits. Time:
• Add an edge: both data structures are O(1).
• Find if there is an edge from u to v: matrix is O(1), and adjacency list must be scanned.
• Visitallneighborsofv(verycommon):matrixisΘ(V),andadjacencylistisO(neighbors). This means BFS will take O(V 2) time if we use adjacency matrix representation.
• Remove an edge: similar to find and add.
The adjacency list representation provides a compact way to represent sparse graphs – those for which |E| is much less than |V 2| – it is usually the method of choice. We may prefer an adjacency matrix representation, however, when the graph is dense – |E| is close to |V 2| – or when we need to be able to tell quickly if there is an edge connecting two given vertices.
Breadth First Search
Breadth first search (BFS) uses a queue to perform the search. A queue is a FIFO (first-in first- out) data structure. When we visit a node and add all the neighbors into the queue, then pop the next thing off of the queue, we will get the neighbors of the first node as the first elements in the queue. This comes about naturally from the FIFO property of the queue and ends up being an extremely useful property. Even thougth the implementation shown in the lecture does not use a queue explicitly, it still maintains the FIFO order of visiting the nodes.
The following is the Python implementation of a queue-based BFS.
2
1 2 3 4 5 6 7 8 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
def
def
__init__(self):
self.adj = {}
add_edge(self, u, v): if self.adj[u] is None:
    self.adj[u] = []
self.adj[u].append(v)
6.006 Introduction to Algorithms
from collections import deque
class BFSResult:
def __init__(self):
        self.level = {}
        self.parent = {}
class Graph:
Recitation 13
October 28, 2011
 def bfs(g, s):
’’’Queue-based implementation of BFS.
Args:
    g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
       neighbors.
    s: source.
’’’
r= BFSResult() r.parent = {s: None} r.level = {s: 0}
queue = deque()
queue.append(s)
while queue:
u = queue.popleft() for n in g.adj[u]:
return r
if n not in level: r.parent[n] = u
    r.level[n] = r.level[u] + 1
    queue.append(n)
3
MIT OpenCourseWare
http://ocw.mit.edu
6.006 Introduction to Algorithms Fall 2011
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
Review on Graphs Handshaking Lemma
In a party, people shook hands with each other. The sum of the number of times each person shook
hands must be even. This can be proven by proving the handshaking lemma: if G = (V, E) is an
undirected graph, then   degree(v) = 2|E|. v∈V
Proof. The degree of a vertex in an undirected graph is the number of edges incident on it. For example, in Figure 1, The degree of node 1 is 2 and the degree of node 2 is 3. Consider a particular, but arbitrarily chosen edge ek = (vi, vj ) ∈ E; it contributes a count of 1 each to deg(vi) and deg(vj) and hence a count of 2 to the total degree. Hence, |E| edges contribute 2|E| to the total degree. Each vertex represents a person and an edge (ui , uj ) represents ui and uj shook hands. The sum of hand-shakes is the sum of the vertex-degrees which is even.
Path
Apathoflengthkfromavertexutoavertexu′ inagraphG=(V,E)isasequence⟨v0,v1,v2,...,vk⟩ of vertices such that u = v0, u′ = vk, and (vi−1,vi) ∈ E for i = 1,2,...,k. There is always a 0-length path from u to u. If there is a path p from u to u′, we say that u′ is reachable from u via
p. If there is no path from u to u′, the distance from u to u′ is infinity.
Graph Representation
In addition to the representations shown during the lecture: adjacency lists, object-oriented vari- ations and implicit representations, there is another way to represent a graph, called adjacency matrix.
Adjacency Matrix
For a graph G = (V, E), we assume that the vertices are numbered 1, 2, . . . |V | in some arbitrary order. Then the adjacency matrix representation of G consists of a |V | × |V | matrix A = (aij ) such that
 1, if(i,j)∈E, aij = 0, otherwise .
This matrix can be stored as an array of arrays, and it requires Θ(V 2) memory, independent of the number of the edges in the graph. Figure 1 shows the adjacency matrix of an undirected graph. Observe the symmetry along the main diagonal of the matrix. In some applications, it pays to store only the entries on and above the diagonal of the adjacency matrix, thereby cutting the memory needed to store the graph almost in half.
 1
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
     12345
  1 2 3 4 5
         01001 10111 01010 01101 11010
      12
54
3
            Figure 1: Adjacency matrix representation of an undirected graph.
Representation Tradeoffs
Space:
• Adjacency lists uses one node per edge, and two machine words per node. So space is
Θ(Ew) bits (w = word size).
• Adjacency matrix uses V 2 entries, but each entry can be just one bit. So space can be Θ(V 2)
bits. Time:
• Add an edge: both data structures are O(1).
• Find if there is an edge from u to v: matrix is O(1), and adjacency list must be scanned.
• Visitallneighborsofv(verycommon):matrixisΘ(V),andadjacencylistisO(neighbors). This means BFS will take O(V 2) time if we use adjacency matrix representation.
• Remove an edge: similar to find and add.
The adjacency list representation provides a compact way to represent sparse graphs – those for which |E| is much less than |V 2| – it is usually the method of choice. We may prefer an adjacency matrix representation, however, when the graph is dense – |E| is close to |V 2| – or when we need to be able to tell quickly if there is an edge connecting two given vertices.
Breadth First Search
Breadth first search (BFS) uses a queue to perform the search. A queue is a FIFO (first-in first- out) data structure. When we visit a node and add all the neighbors into the queue, then pop the next thing off of the queue, we will get the neighbors of the first node as the first elements in the queue. This comes about naturally from the FIFO property of the queue and ends up being an extremely useful property. Even thougth the implementation shown in the lecture does not use a queue explicitly, it still maintains the FIFO order of visiting the nodes.
The following is the Python implementation of a queue-based BFS.
2
1 2 3 4 5 6 7 8 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
def
def
__init__(self):
self.adj = {}
add_edge(self, u, v): if self.adj[u] is None:
    self.adj[u] = []
self.adj[u].append(v)
6.006 Introduction to Algorithms
from collections import deque
class BFSResult:
def __init__(self):
        self.level = {}
        self.parent = {}
class Graph:
Recitation 13
October 28, 2011
 def bfs(g, s):
’’’Queue-based implementation of BFS.
Args:
    g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
       neighbors.
    s: source.
’’’
r= BFSResult() r.parent = {s: None} r.level = {s: 0}
queue = deque()
queue.append(s)
while queue:
u = queue.popleft() for n in g.adj[u]:
return r
if n not in level: r.parent[n] = u
    r.level[n] = r.level[u] + 1
    queue.append(n)
3
MIT OpenCourseWare
http://ocw.mit.edu
6.006 Introduction to Algorithms Fall 2011
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
Review on Graphs Handshaking Lemma
In a party, people shook hands with each other. The sum of the number of times each person shook
hands must be even. This can be proven by proving the handshaking lemma: if G = (V, E) is an
undirected graph, then   degree(v) = 2|E|. v∈V
Proof. The degree of a vertex in an undirected graph is the number of edges incident on it. For example, in Figure 1, The degree of node 1 is 2 and the degree of node 2 is 3. Consider a particular, but arbitrarily chosen edge ek = (vi, vj ) ∈ E; it contributes a count of 1 each to deg(vi) and deg(vj) and hence a count of 2 to the total degree. Hence, |E| edges contribute 2|E| to the total degree. Each vertex represents a person and an edge (ui , uj ) represents ui and uj shook hands. The sum of hand-shakes is the sum of the vertex-degrees which is even.
Path
Apathoflengthkfromavertexutoavertexu′ inagraphG=(V,E)isasequence⟨v0,v1,v2,...,vk⟩ of vertices such that u = v0, u′ = vk, and (vi−1,vi) ∈ E for i = 1,2,...,k. There is always a 0-length path from u to u. If there is a path p from u to u′, we say that u′ is reachable from u via
p. If there is no path from u to u′, the distance from u to u′ is infinity.
Graph Representation
In addition to the representations shown during the lecture: adjacency lists, object-oriented vari- ations and implicit representations, there is another way to represent a graph, called adjacency matrix.
Adjacency Matrix
For a graph G = (V, E), we assume that the vertices are numbered 1, 2, . . . |V | in some arbitrary order. Then the adjacency matrix representation of G consists of a |V | × |V | matrix A = (aij ) such that
 1, if(i,j)∈E, aij = 0, otherwise .
This matrix can be stored as an array of arrays, and it requires Θ(V 2) memory, independent of the number of the edges in the graph. Figure 1 shows the adjacency matrix of an undirected graph. Observe the symmetry along the main diagonal of the matrix. In some applications, it pays to store only the entries on and above the diagonal of the adjacency matrix, thereby cutting the memory needed to store the graph almost in half.
 1
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
     12345
  1 2 3 4 5
         01001 10111 01010 01101 11010
      12
54
3
            Figure 1: Adjacency matrix representation of an undirected graph.
Representation Tradeoffs
Space:
• Adjacency lists uses one node per edge, and two machine words per node. So space is
Θ(Ew) bits (w = word size).
• Adjacency matrix uses V 2 entries, but each entry can be just one bit. So space can be Θ(V 2)
bits. Time:
• Add an edge: both data structures are O(1).
• Find if there is an edge from u to v: matrix is O(1), and adjacency list must be scanned.
• Visitallneighborsofv(verycommon):matrixisΘ(V),andadjacencylistisO(neighbors). This means BFS will take O(V 2) time if we use adjacency matrix representation.
• Remove an edge: similar to find and add.
The adjacency list representation provides a compact way to represent sparse graphs – those for which |E| is much less than |V 2| – it is usually the method of choice. We may prefer an adjacency matrix representation, however, when the graph is dense – |E| is close to |V 2| – or when we need to be able to tell quickly if there is an edge connecting two given vertices.
Breadth First Search
Breadth first search (BFS) uses a queue to perform the search. A queue is a FIFO (first-in first- out) data structure. When we visit a node and add all the neighbors into the queue, then pop the next thing off of the queue, we will get the neighbors of the first node as the first elements in the queue. This comes about naturally from the FIFO property of the queue and ends up being an extremely useful property. Even thougth the implementation shown in the lecture does not use a queue explicitly, it still maintains the FIFO order of visiting the nodes.
The following is the Python implementation of a queue-based BFS.
2
1 2 3 4 5 6 7 8 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
def
def
__init__(self):
self.adj = {}
add_edge(self, u, v): if self.adj[u] is None:
    self.adj[u] = []
self.adj[u].append(v)
6.006 Introduction to Algorithms
from collections import deque
class BFSResult:
def __init__(self):
        self.level = {}
        self.parent = {}
class Graph:
Recitation 13
October 28, 2011
 def bfs(g, s):
’’’Queue-based implementation of BFS.
Args:
    g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
       neighbors.
    s: source.
’’’
r= BFSResult() r.parent = {s: None} r.level = {s: 0}
queue = deque()
queue.append(s)
while queue:
u = queue.popleft() for n in g.adj[u]:
return r
if n not in level: r.parent[n] = u
    r.level[n] = r.level[u] + 1
    queue.append(n)
3
MIT OpenCourseWare
http://ocw.mit.edu
6.006 Introduction to Algorithms Fall 2011
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
Review on Graphs Handshaking Lemma
In a party, people shook hands with each other. The sum of the number of times each person shook
hands must be even. This can be proven by proving the handshaking lemma: if G = (V, E) is an
undirected graph, then   degree(v) = 2|E|. v∈V
Proof. The degree of a vertex in an undirected graph is the number of edges incident on it. For example, in Figure 1, The degree of node 1 is 2 and the degree of node 2 is 3. Consider a particular, but arbitrarily chosen edge ek = (vi, vj ) ∈ E; it contributes a count of 1 each to deg(vi) and deg(vj) and hence a count of 2 to the total degree. Hence, |E| edges contribute 2|E| to the total degree. Each vertex represents a person and an edge (ui , uj ) represents ui and uj shook hands. The sum of hand-shakes is the sum of the vertex-degrees which is even.
Path
Apathoflengthkfromavertexutoavertexu′ inagraphG=(V,E)isasequence⟨v0,v1,v2,...,vk⟩ of vertices such that u = v0, u′ = vk, and (vi−1,vi) ∈ E for i = 1,2,...,k. There is always a 0-length path from u to u. If there is a path p from u to u′, we say that u′ is reachable from u via
p. If there is no path from u to u′, the distance from u to u′ is infinity.
Graph Representation
In addition to the representations shown during the lecture: adjacency lists, object-oriented vari- ations and implicit representations, there is another way to represent a graph, called adjacency matrix.
Adjacency Matrix
For a graph G = (V, E), we assume that the vertices are numbered 1, 2, . . . |V | in some arbitrary order. Then the adjacency matrix representation of G consists of a |V | × |V | matrix A = (aij ) such that
 1, if(i,j)∈E, aij = 0, otherwise .
This matrix can be stored as an array of arrays, and it requires Θ(V 2) memory, independent of the number of the edges in the graph. Figure 1 shows the adjacency matrix of an undirected graph. Observe the symmetry along the main diagonal of the matrix. In some applications, it pays to store only the entries on and above the diagonal of the adjacency matrix, thereby cutting the memory needed to store the graph almost in half.
 1
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
     12345
  1 2 3 4 5
         01001 10111 01010 01101 11010
      12
54
3
            Figure 1: Adjacency matrix representation of an undirected graph.
Representation Tradeoffs
Space:
• Adjacency lists uses one node per edge, and two machine words per node. So space is
Θ(Ew) bits (w = word size).
• Adjacency matrix uses V 2 entries, but each entry can be just one bit. So space can be Θ(V 2)
bits. Time:
• Add an edge: both data structures are O(1).
• Find if there is an edge from u to v: matrix is O(1), and adjacency list must be scanned.
• Visitallneighborsofv(verycommon):matrixisΘ(V),andadjacencylistisO(neighbors). This means BFS will take O(V 2) time if we use adjacency matrix representation.
• Remove an edge: similar to find and add.
The adjacency list representation provides a compact way to represent sparse graphs – those for which |E| is much less than |V 2| – it is usually the method of choice. We may prefer an adjacency matrix representation, however, when the graph is dense – |E| is close to |V 2| – or when we need to be able to tell quickly if there is an edge connecting two given vertices.
Breadth First Search
Breadth first search (BFS) uses a queue to perform the search. A queue is a FIFO (first-in first- out) data structure. When we visit a node and add all the neighbors into the queue, then pop the next thing off of the queue, we will get the neighbors of the first node as the first elements in the queue. This comes about naturally from the FIFO property of the queue and ends up being an extremely useful property. Even thougth the implementation shown in the lecture does not use a queue explicitly, it still maintains the FIFO order of visiting the nodes.
The following is the Python implementation of a queue-based BFS.
2
1 2 3 4 5 6 7 8 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
def
def
__init__(self):
self.adj = {}
add_edge(self, u, v): if self.adj[u] is None:
    self.adj[u] = []
self.adj[u].append(v)
6.006 Introduction to Algorithms
from collections import deque
class BFSResult:
def __init__(self):
        self.level = {}
        self.parent = {}
class Graph:
Recitation 13
October 28, 2011
 def bfs(g, s):
’’’Queue-based implementation of BFS.
Args:
    g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
       neighbors.
    s: source.
’’’
r= BFSResult() r.parent = {s: None} r.level = {s: 0}
queue = deque()
queue.append(s)
while queue:
u = queue.popleft() for n in g.adj[u]:
return r
if n not in level: r.parent[n] = u
    r.level[n] = r.level[u] + 1
    queue.append(n)
3
MIT OpenCourseWare
http://ocw.mit.edu
6.006 Introduction to Algorithms Fall 2011
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
Review on Graphs Handshaking Lemma
In a party, people shook hands with each other. The sum of the number of times each person shook
hands must be even. This can be proven by proving the handshaking lemma: if G = (V, E) is an
undirected graph, then   degree(v) = 2|E|. v∈V
Proof. The degree of a vertex in an undirected graph is the number of edges incident on it. For example, in Figure 1, The degree of node 1 is 2 and the degree of node 2 is 3. Consider a particular, but arbitrarily chosen edge ek = (vi, vj ) ∈ E; it contributes a count of 1 each to deg(vi) and deg(vj) and hence a count of 2 to the total degree. Hence, |E| edges contribute 2|E| to the total degree. Each vertex represents a person and an edge (ui , uj ) represents ui and uj shook hands. The sum of hand-shakes is the sum of the vertex-degrees which is even.
Path
Apathoflengthkfromavertexutoavertexu′ inagraphG=(V,E)isasequence⟨v0,v1,v2,...,vk⟩ of vertices such that u = v0, u′ = vk, and (vi−1,vi) ∈ E for i = 1,2,...,k. There is always a 0-length path from u to u. If there is a path p from u to u′, we say that u′ is reachable from u via
p. If there is no path from u to u′, the distance from u to u′ is infinity.
Graph Representation
In addition to the representations shown during the lecture: adjacency lists, object-oriented vari- ations and implicit representations, there is another way to represent a graph, called adjacency matrix.
Adjacency Matrix
For a graph G = (V, E), we assume that the vertices are numbered 1, 2, . . . |V | in some arbitrary order. Then the adjacency matrix representation of G consists of a |V | × |V | matrix A = (aij ) such that
 1, if(i,j)∈E, aij = 0, otherwise .
This matrix can be stored as an array of arrays, and it requires Θ(V 2) memory, independent of the number of the edges in the graph. Figure 1 shows the adjacency matrix of an undirected graph. Observe the symmetry along the main diagonal of the matrix. In some applications, it pays to store only the entries on and above the diagonal of the adjacency matrix, thereby cutting the memory needed to store the graph almost in half.
 1
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
     12345
  1 2 3 4 5
         01001 10111 01010 01101 11010
      12
54
3
            Figure 1: Adjacency matrix representation of an undirected graph.
Representation Tradeoffs
Space:
• Adjacency lists uses one node per edge, and two machine words per node. So space is
Θ(Ew) bits (w = word size).
• Adjacency matrix uses V 2 entries, but each entry can be just one bit. So space can be Θ(V 2)
bits. Time:
• Add an edge: both data structures are O(1).
• Find if there is an edge from u to v: matrix is O(1), and adjacency list must be scanned.
• Visitallneighborsofv(verycommon):matrixisΘ(V),andadjacencylistisO(neighbors). This means BFS will take O(V 2) time if we use adjacency matrix representation.
• Remove an edge: similar to find and add.
The adjacency list representation provides a compact way to represent sparse graphs – those for which |E| is much less than |V 2| – it is usually the method of choice. We may prefer an adjacency matrix representation, however, when the graph is dense – |E| is close to |V 2| – or when we need to be able to tell quickly if there is an edge connecting two given vertices.
Breadth First Search
Breadth first search (BFS) uses a queue to perform the search. A queue is a FIFO (first-in first- out) data structure. When we visit a node and add all the neighbors into the queue, then pop the next thing off of the queue, we will get the neighbors of the first node as the first elements in the queue. This comes about naturally from the FIFO property of the queue and ends up being an extremely useful property. Even thougth the implementation shown in the lecture does not use a queue explicitly, it still maintains the FIFO order of visiting the nodes.
The following is the Python implementation of a queue-based BFS.
2
1 2 3 4 5 6 7 8 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
def
def
__init__(self):
self.adj = {}
add_edge(self, u, v): if self.adj[u] is None:
    self.adj[u] = []
self.adj[u].append(v)
6.006 Introduction to Algorithms
from collections import deque
class BFSResult:
def __init__(self):
        self.level = {}
        self.parent = {}
class Graph:
Recitation 13
October 28, 2011
 def bfs(g, s):
’’’Queue-based implementation of BFS.
Args:
    g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
       neighbors.
    s: source.
’’’
r= BFSResult() r.parent = {s: None} r.level = {s: 0}
queue = deque()
queue.append(s)
while queue:
u = queue.popleft() for n in g.adj[u]:
return r
if n not in level: r.parent[n] = u
    r.level[n] = r.level[u] + 1
    queue.append(n)
3
MIT OpenCourseWare
http://ocw.mit.edu
6.006 Introduction to Algorithms Fall 2011
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.
ntroduction to Algorithms Recitation 13 October 28, 2011
Review on Graphs Handshaking Lemma
In a party, people shook hands with each other. The sum of the number of times each person shook
hands must be even. This can be proven by proving the handshaking lemma: if G = (V, E) is an
undirected graph, then   degree(v) = 2|E|. v∈V
Proof. The degree of a vertex in an undirected graph is the number of edges incident on it. For example, in Figure 1, The degree of node 1 is 2 and the degree of node 2 is 3. Consider a particular, but arbitrarily chosen edge ek = (vi, vj ) ∈ E; it contributes a count of 1 each to deg(vi) and deg(vj) and hence a count of 2 to the total degree. Hence, |E| edges contribute 2|E| to the total degree. Each vertex represents a person and an edge (ui , uj ) represents ui and uj shook hands. The sum of hand-shakes is the sum of the vertex-degrees which is even.
Path
Apathoflengthkfromavertexutoavertexu′ inagraphG=(V,E)isasequence⟨v0,v1,v2,...,vk⟩ of vertices such that u = v0, u′ = vk, and (vi−1,vi) ∈ E for i = 1,2,...,k. There is always a 0-length path from u to u. If there is a path p from u to u′, we say that u′ is reachable from u via
p. If there is no path from u to u′, the distance from u to u′ is infinity.
Graph Representation
In addition to the representations shown during the lecture: adjacency lists, object-oriented vari- ations and implicit representations, there is another way to represent a graph, called adjacency matrix.
Adjacency Matrix
For a graph G = (V, E), we assume that the vertices are numbered 1, 2, . . . |V | in some arbitrary order. Then the adjacency matrix representation of G consists of a |V | × |V | matrix A = (aij ) such that
 1, if(i,j)∈E, aij = 0, otherwise .
This matrix can be stored as an array of arrays, and it requires Θ(V 2) memory, independent of the number of the edges in the graph. Figure 1 shows the adjacency matrix of an undirected graph. Observe the symmetry along the main diagonal of the matrix. In some applications, it pays to store only the entries on and above the diagonal of the adjacency matrix, thereby cutting the memory needed to store the graph almost in half.
 1
6.006 Introduction to Algorithms Recitation 13 October 28, 2011
     12345
  1 2 3 4 5
         01001 10111 01010 01101 11010
      12
54
3
            Figure 1: Adjacency matrix representation of an undirected graph.
Representation Tradeoffs
Space:
• Adjacency lists uses one node per edge, and two machine words per node. So space is
Θ(Ew) bits (w = word size).
• Adjacency matrix uses V 2 entries, but each entry can be just one bit. So space can be Θ(V 2)
bits. Time:
• Add an edge: both data structures are O(1).
• Find if there is an edge from u to v: matrix is O(1), and adjacency list must be scanned.
• Visitallneighborsofv(verycommon):matrixisΘ(V),andadjacencylistisO(neighbors). This means BFS will take O(V 2) time if we use adjacency matrix representation.
• Remove an edge: similar to find and add.
The adjacency list representation provides a compact way to represent sparse graphs – those for which |E| is much less than |V 2| – it is usually the method of choice. We may prefer an adjacency matrix representation, however, when the graph is dense – |E| is close to |V 2| – or when we need to be able to tell quickly if there is an edge connecting two given vertices.
Breadth First Search
Breadth first search (BFS) uses a queue to perform the search. A queue is a FIFO (first-in first- out) data structure. When we visit a node and add all the neighbors into the queue, then pop the next thing off of the queue, we will get the neighbors of the first node as the first elements in the queue. This comes about naturally from the FIFO property of the queue and ends up being an extremely useful property. Even thougth the implementation shown in the lecture does not use a queue explicitly, it still maintains the FIFO order of visiting the nodes.
The following is the Python implementation of a queue-based BFS.
2
1 2 3 4 5 6 7 8 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
def
def
__init__(self):
self.adj = {}
add_edge(self, u, v): if self.adj[u] is None:
    self.adj[u] = []
self.adj[u].append(v)
6.006 Introduction to Algorithms
from collections import deque
class BFSResult:
def __init__(self):
        self.level = {}
        self.parent = {}
class Graph:
Recitation 13
October 28, 2011
 def bfs(g, s):
’’’Queue-based implementation of BFS.
Args:
    g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
       neighbors.
    s: source.
’’’
r= BFSResult() r.parent = {s: None} r.level = {s: 0}
queue = deque()
queue.append(s)
while queue:
u = queue.popleft() for n in g.adj[u]:
return r
if n not in level: r.parent[n] = u
    r.level[n] = r.level[u] + 1
    queue.append(n)
3
MIT OpenCourseWare
http://ocw.mit.edu
6.006 Introduction to Algorithms Fall 2011
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

