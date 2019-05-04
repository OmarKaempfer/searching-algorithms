# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
tu = search.GPSProblem('T', 'U', search.romania)
hl = search.GPSProblem('H', 'L', search.romania)
print("__________________________ Breadth first _________________________\n")
print("A -> B")
print(search.breadth_first_graph_search(ab).path())
print("\nT -> U")
print(search.breadth_first_graph_search(tu).path())
print("\nH -> L")
print(search.breadth_first_graph_search(hl).path())
print("\n\n__________________________ Depth first ___________________________\n")
print("A -> B")
print(search.depth_first_graph_search(ab).path())
print("\nT -> U")
print(search.depth_first_graph_search(tu).path())
print("\nH -> L")
print(search.depth_first_graph_search(hl).path())
print("\n\n________________________ Branch and bound ________________________\n")
print("A -> B")
print(search.bab(ab).path())
print("\nT -> U")
print(search.bab(tu).path())
print("\nH -> L")
print(search.bab(hl).path())
print("\n\n_______________ Branch and bound - subestimation _________________\n")
print("A -> B")
print(search.babh(ab).path())
print("\nT -> U")
print(search.babh(tu).path())
print("\nH -> L")
print(search.babh(hl).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
