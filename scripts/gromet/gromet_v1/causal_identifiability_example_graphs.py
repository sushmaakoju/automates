"""
def test_conditional_identifiability():
    g = igraph.Graph(edges=[[0, 1], [1, 2], [0, 1], [1, 0]], directed=True)
    g.vs["name"] = ["X", "Z", "Y"]
    g.es["description"] = ["O", "O", "U", "U"]
    y = ["Y"]
    x = ["X"]
    z = ["Z"]
    results = identifiability(y, x, g, z)
    assert results == "\\frac{P(Y|X,Z)}{\\sum_{Y}P(Y|X,Z)}"
"""

# model 1: Simple_SIR
edges = [[0, 6], [0, 8],
         [1, 6], [1, 7], [1, 9],
         [2, 6], [2, 10],
         [3, 6],
         [4, 7],
         [5, 6], [5, 7],
         [6, 8], [6, 9],
         [7, 9], [7, 10]]
names = ['s', 'i', 'r', 'beta', 'gamma', 'dt', 'inf', 'rec', 's2', 'i2', 'r2']

# model 2: CHIME_SIR (v01)
edges = [[0, 5], [0, 6],
         [1, 5], [1, 6], [1, 7],
         [2, 7],
         [3, 5], [3, 6],
         [4, 6], [4, 7],
         [5, 9], [5, 10],
         [6, 9], [6, 11],
         [7, 9], [7, 12],
         [8, 9],
         [9, 10], [9, 11], [9, 12]]
names = ['s', 'i', 'r', 'beta', 'gamma', 's_n', 'i_n', 'r_n', 'n', 'scale', 's1', 'i2', 'r2']
