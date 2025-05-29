### Without using any Python packages like `numpy` or `pandas`, write a function to calculate the covariance matrix for a given dataset. 
def compute_covariance_matrix(data):
    """
    Compute the covariance matrix for a given dataset.
    Input: data - A 2D list where each inner list is a variable (e.g., [[X], [Y]])
    Output: Covariance matrix as a 2D list
    """
    
    # Number of variables
    n_vars = len(data)
    
    # Number of observations (assuming all variables have same length)
    n_obs = len(data[0])
    
    # Calculate means for each variable
    means = []
    for var in data:
        mean = sum(var) / len(var)
        means.append(mean)
    
    # Initialize covariance matrix
    cov_matrix = [[0.0 for _ in range(n_vars)] for _ in range(n_vars)]
    
    # Calculate covariance for each pair of variables
    for i in range(n_vars):
        for j in range(n_vars):
            # Calculate covariance between variable i and variable j
            covariance = 0.0
            for k in range(n_obs):
                covariance += (data[i][k] - means[i]) * (data[j][k] - means[j])
            
            # Divide by n-1 for sample covariance
            cov_matrix[i][j] = covariance / (n_obs - 1)
    
    return cov_matrix


# Example usage and test
if __name__ == "__main__":
    # Test with simple 2x2 dataset
    test_data = [
        [1, 2, 3, 4, 5],  # Variable X
        [2, 4, 6, 8, 10]  # Variable Y
    ]
    
    result = compute_covariance_matrix(test_data)
    
    print("Test Data:")
    print("Variable X:", test_data[0])
    print("Variable Y:", test_data[1])
    print("\nCovariance Matrix:")
    for row in result:
        print([round(val, 4) for val in row])
    
    # Test with another example
    test_data2 = [
        [1, 3, 5],     # Variable A
        [2, 6, 10],    # Variable B  
        [1, 2, 3]      # Variable C
    ]
    
    result2 = compute_covariance_matrix(test_data2)
    
    print("\n" + "="*40)
    print("Test Data 2:")
    for i, var in enumerate(test_data2):
        print(f"Variable {chr(65+i)}:", var)
    print("\nCovariance Matrix:")
    for row in result2:
        print([round(val, 4) for val in row])

