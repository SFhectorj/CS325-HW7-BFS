from collections import deque

def minEffort(puzzle):
    """
    :param puzzle:
    This function will use binary search and  breadth-first search to traverse a 2D matrix.
    The algorithm will reach the destination with minimal effort bu finding the lowest maximum difference of the column/row heights.
    """
    number_of_columns = len(puzzle[0])
    number_of_rows = len(puzzle)

    def reachDestination(maxEffort):
        """
        This is a helper function to check if reaching the bottom right corner is feasible using the given maximum effort.
        """
        # Start with a queue; top left corner (0,0)
        current_queue = deque([(0, 0)])
        # Using a set will automatically remove dupes
        already_visited = set()
        already_visited.add((0, 0))

        # Set the possible movement directions
        # [Up, Down, Left, Right]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # BREADTH-FIRST SEARCH
        while current_queue:
            # popleft() method is used to remove and return the first element (leftmost element) from a deque object.
            current_row = current_queue.popleft()
            current_column = current_queue.popleft()

            # Edgecase: the bottom right corner is reached
            if (current_row, current_column) == (number_of_rows - 1, number_of_columns - 1):
                return True

            # Loop to check all possible directions
            for row, column in directions:
                newRow = current_row + row
                newCol = current_column + column

                # Edgecases for new position:
                # Is within bounds,
                # Not previously visited
                if 0 <= newRow < number_of_rows and 0 <= newCol < number_of_columns and (newRow, newCol) not in already_visited:
                    # Now get the height difference between the current cell and the new cell.
                    height_difference = puzzle[newRow][newCol] - puzzle[current_row][current_column]

                    # When the height difference meets the edgecases, visit new cell.
                    if height_difference <= maxEffort:
                        already_visited.add(newRow, newCol)
                        current_queue.append((newRow, newCol))

        return False

    # BINARY SEARCH
    # Initialize range
    left_side = 0   # min effort
    right_side = 0  # max effort

    # Find the maximum abs difference
    # by looping through all cells
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            # Check the next cell on the right to make sure its in bound
            if j + 1 < number_of_columns:
                right_side = max(right_side, abs(puzzle[i][j] - puzzle[i][j + 1]))

