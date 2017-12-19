# Backtracing Innovation
From Snapchat's Facial Recognition to the Inception of Semiconductors

# CAUTION! Github's Jupyter preview chokes on our notebook, please use the following link [Project Notebook](https://nbviewer.jupyter.org/github/qantik/prayingmantissa/blob/master/project/patents.ipynb)

### Abstract
The US Patent & Trademark Office, short USPTO, offers a full-fledged directed graph of US patent
citations since 1975. Many at the time obscure patents paved the way for groundbreaking new
technologies in the future, as for example Google's Page Rank (#6285999) or Stephen Wozniak’s
Microcomputer for use with video display (#4136359). In our project we endeavor to visualize
this massivegraph with more than
89 Million edges in an appealing and concise way in order to render the narration of more
intricate stories possible and offer potential users a slick and interactive interface
for navigating the patents graph. Inspirations on how to beautifully draw a graph network
are taken from [Kirell Benzi](http://www.kirellbenzi.com). Those stories may range from analysing
node connectivities to extract influences of particular inventors to finding the
shortest walks between patents. Through this we hope to gain deeper insight into the
metastructure of inventions throughout the digital revolution and how they shape the future
as we know it today.

### Research questions
 - How to apply common graph algorithms to a massive data set?
 - How to efficiently travers and query a graph of that scale?
 - How to visualize a large and complicated graph?
 - How to handle missing edges in the patent graph?
 - How to eliminate equal patents that were filed under several identifiers?
 - How to draw conclusions about technology soley given patents and their citations?
 
### Datasets
 - [USPTO patents database](http://www.patentsview.org/download)
 - [Google patents](https://www.google.ch/patents)

### Internal milestones up until milestone 2
 - [x] Refresh on graph algorithms.
 - [x] Look for efficient graph processing libraries. Preferably with GPU integration.
 - [x] Sight data and perform preliminary analysis.
 - [x] Find blog skeleton.
 - [x] Discuss narrative of the data story.

### Internal milestones up until milestone 3
 - [x] 1st week of December: Get the blog up and running.
 - [x] 1st week of December: Prepare and compute first data blocks for the website
 - [x] 2nd week of December: Finish data story.
 - [x] 2nd week of December: Have visualization online.
 - [x] Beginning of 3rd week of December: Polish.

### TA Questions
 * What technologies do professional data blogs like FiveThirtyEight use for visualisation?
    - A variety, from custom JS to custom photoshop and illustrator.
 * What is [Kirell Benzi's](http://www.kirellbenzi.com) magic library?
    -  Most advanced stuff can be done with d3.js, other graph visualizations can be done with igraph, graph-tool, gephi, etc. but not all of them scale well.

### Workload distribution
 - Andrea Caforio coded up the website, preparared the data and tools (e.g. graph-tool) and performed preliminary data analysis.
 - Michael Allemann designed and wrote the narrative and explored the data and possible roads to go down.
 - Roman Bachmann explored the data and using those insights created the graph visualisations.
