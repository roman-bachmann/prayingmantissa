## 1 Introduction to patents


## 3 Graph Software

### 3.1 What we tried
Our first library of choice was *networkx*, to store, analyse and display our graphs. While trying to load the 89 Million edges into a graph, we quickly noticed that *networkx* has troubles dealing with such a big graph.

Looking for a graph network library that can handle many more nodes and edges, we discovered *graph-tool*. *graph-tool* stores vertices efficiently just as an index between 0 and N-1, where N is the total number of vertices in the graph. Additional properties of the vertices (like the patent ID to identify them) can be stored alongside in a property variable. *graph-tool*'s algorithms are very fast and efficient, but installing it has proven to be quite the task. In the end we decided to run *graph-tool* inside a docker image.

Even though *graph-tool* is much faster, we are still reaching the limit of what our laptops can handle memory-wise (8GB). Therefore, if needed we will use a computer with more memory (16GB) to run more complex algorithms on the data.


## 5 Planning

### 5.1 Methods we will use on the graph
At this point in time, we have the full graph available that we want to analyse. From this network, we hope to find new insights into the patents data in the following ways:

- Extract most cited patents. This means finding the vertices in the graph that have the highest in-degrees. When we have those patents, we can analyse if and how they are interconnected, as well as who are their inventors / assignees.
- Find the smallest maximum distance between any two patents. How many steps away is any patent from any other one?
- Go back in time: Is there a path from Snapchat's facial filters back in time to the invention of the transistor? We will try to find interesting examples of this type by searching for the shortest path between two nodes of interest.


Methods we are considering:

- Animated graphs that show patent applications and expirations throughout time in a network. *graph-tool* offers functions to build such an animation.





### 5.2 What we still need to figure out:

- bla
- bla


### 5.2 Timeplan







Things to consider:

- What subset of nodes to draw