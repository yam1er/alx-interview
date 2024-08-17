def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        # Start a new row with `1`s
        row = [1] * (i + 1)
        
        # Compute the values for the current row based on the previous rowfor j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle
