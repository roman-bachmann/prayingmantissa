import pandas as pd
import numpy as np
from graph_tool.all import *

DATA = './'
reader = pd.read_csv(DATA + 'citations_processed.csv', engine='c', chunksize=500000)

graph = Graph()
count = 0
props = np.empty(0, dtype=np.int32)

for chunk in reader:
    print(count)
    count += 1
    
    '''
    chunk.dropna(inplace=True)
    chunk['patent_id'] = chunk['patent_id'].astype(str)
    chunk['citation_id'] = chunk['citation_id'].astype(str)

    chunk = chunk[chunk.patent_id.str.match(r'([D]\d+$)|(^\d+$)')]
    chunk = chunk[chunk.citation_id.str.match(r'([D]\d+$)|(^\d+$)')]

    chunk.columns.str.strip()

    chunk['patent_id'] = np.array(list(map(lambda i: int(i, 16), chunk.patent_id)), dtype=np.int32)
    chunk['citation_id'] = np.array(list(map(lambda i: int(i, 16), chunk.citation_id)), dtype=np.int32)
    '''

    chunk_props = graph.add_edge_list(chunk.values, hashed=True)
    chunk_props_arr = chunk_props.get_array()
    props = PropertyArray(np.concatenate([props, chunk_props_arr[len(chunk_props_arr)-2:]]), graph)
    
print(props)
graph.vertex_properties['id'] = graph.new_vertex_property('int', props)

print("Generated graph")

graph.save("citations_graph.xml.gz")

print("Saved as citations_graph.xml.gz")

print(graph.vp.id['4'])

print(graph.get_vertices())