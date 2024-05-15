def objective(x, target_value):
    return (x**2) - target_value

def hillclimbing(target_value):
    current_solution = 0.0
    epsilon = 0.1
    while True:
        current_objective = objective(current_solution, target_value)

        if abs(current_objective) < epsilon:
            break
        if current_objective < 0:
            current_solution += 0.001
        elif current_objective > 0:
            current_solution -= 0.001
    return current_solution

target_value = int(input("Enter a Value:"))
solution = hillclimbing(target_value)
print(f"Root of {target_value} is: {solution:.5f}")
#In the worst case, the Hill Climbing algorithm may get stuck in a local maximum, and it may need to explore all possible neighbors at each step.
#If the search space has n possible states, and each state has m possible neighbors,
#then the time complexity of the Hill Climbing algorithm can be expressed as O(n * m)