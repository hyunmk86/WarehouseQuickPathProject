import matplotlib.pyplot as plt
import networkx as nx


# phone models and how it is setup in the warehouse
# weight represents distance between the node in ft
setup = [
    ('alcatel', 'desire', {'weight': 4}),
    ('desire', 'durashock', {'weight': 4}),
    ('durashock', 'icon', {'weight': 4}),
    ('icon', 'vm1', {'weight': 13}),
    ('icon', 'realm', {'weight': 4}),
    ('realm', 'vm2', {'weight': 13}),
    ('realm', 'tribute', {'weight': 4}),
    ('tribute', 'sync', {'weight': 13}),
    ('vm1', 'vm2', {'weight': 4}),
    ('vm2', 'sync', {'weight': 4}),
    ('sync', 'speed', {'weight': 4}),
    ('speed', 'max', {'weight': 4}),
    ('max', 'prevail2', {'weight': 4}),
    ('prevail2', 's3', {'weight': 12}),
    ('s3', 'prevailLTE', {'weight': 12}),
    ('prevailLTE', 'aquos', {'weight': 12}),
    ('tribute', 'f3', {'weight': 9}),
    ('f3', 'volt', {'weight': 4}),
    ('volt', 'stylo', {'weight': 4}),
    ('stylo', 'motog', {'weight': 4}),
    ('motog', 'motoe', {'weight': 4}),
    ('motoe', 'lumia', {'weight': 4}),
    ('f3', 'speed', {'weight': 15}),
    ('volt', 'max', {'weight': 15}),
    ('stylo', 'prevail2', {'weight': 15}),
    ('motog', 's3', {'weight': 15}),
    ('motoe', 'prevailLTE', {'weight': 15}),
    ('lumia', 'aquos', {'weight': 15}), ]

G = nx.Graph(setup)
# sample picking
picking = ['desire', 'icon', 'vm2', 'tribute', 'speed','max','volt','s3','motog','lumia']
#
# Method 1
#
def shortestpath(picking):
    # iterate through the list of  picking and calculate distance between each items
    # using Graph(setup). Calculates shortest path and returns result
    # undirected graph, nodes does not repeat
    p = picking
    setup = G
    newsort = [picking[0]]
    k = picking[0]
    lowest = []

    while len(newsort) != len(p):
        filteredlist = {}
        path = nx.single_source_dijkstra_path_length(setup, k, cutoff=None, weight='weight')

        for x in newsort:
            if path.has_key(x):
                del path[x]

        for key in path:
            if key in p:
                filteredlist[key] = path[key]


        if filteredlist != {}:
            lowest = min(filteredlist, key=filteredlist.get)
        newsort.append(lowest)
        k = lowest

    return newsort[0:len(p)]


print shortestpath(picking)

#
# to draw the graph, delete the '#' below
#

# nx.draw(G)
# plt.show() # display
