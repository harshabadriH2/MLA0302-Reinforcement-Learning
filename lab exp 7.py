gamma = 0.9

n = int(input("Enter Number of States: "))

reward = []

print("\nEnter Reward for Each State")

for i in range(n):
    r = float(input("Reward of State " + str(i) + ": "))
    reward.append(r)

print("\nPolicies")
print("1. Move Right")
print("2. Move Left")

choice = int(input("Choose Policy: "))

value = [0] * n

iterations = int(input("\nEnter Number of Bellman Iterations: "))

for k in range(iterations):

    new_value = value.copy()

    for s in range(n):

        if choice == 1:

            if s == n - 1:
                next_state = s
            else:
                next_state = s + 1

        else:

            if s == 0:
                next_state = s
            else:
                next_state = s - 1

        new_value[s] = reward[s] + gamma * value[next_state]

    value = new_value

print("\nState Value Function")

for i in range(n):
    print("V(State", i, ") =", round(value[i],2))
