def calculate_min_steps(n, s, x):
    # Sort the array of positions
    x.sort()
    
    # Case 1: Starting position is less than the smallest position
    if s <= x[0]:
        return x[-1] - s
    
    # Case 2: Starting position is greater than the largest position
    elif s >= x[-1]:
        return s - x[0]
    
    # Case 3: Starting position is between the smallest and largest positions
    else:
        # Calculate steps for both directions and take the minimum
        left_to_right = (s - x[0]) + (x[-1] - x[0])
        right_to_left = (x[-1] - s) + (x[-1] - x[0])
        return min(left_to_right, right_to_left)

def main():
    t = int(input())  # Number of test cases
    results = []
    
    for _ in range(t):
        n, s = map(int, input().split())  # Number of positions and starting position
        x = list(map(int, input().split()))  # Positions to visit
        results.append(calculate_min_steps(n, s, x))
    
    # Output results for all test cases
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
