### Using the AGD Algorithm
Before using the AGD algorithm, ensure that all the polygon's vertices are transformed so that the longest edge aligns with the X-axis and all vertices are positioned within the first quadrant of the XY-coordinate system. For reference, see Example 1 in the Appendix of the paper (https://arxiv.org/pdf/2412.00899).

To use the AGD algorithm, create the `nodes_list` (vertices of the search area) following these rules:

1. The first node should be the vertex on the longest edge with the minimum X-coordinate.  
2. The nodes should be listed in counterclockwise order around the polygon.
