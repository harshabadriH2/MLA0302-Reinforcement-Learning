import random

episodes = int(input("Enter Number of Simulation Episodes: "))

print("\nPolicies")
print("1. Assign First Available Representative")
print("2. Assign Representative Randomly")

policy = int(input("Choose Policy: "))

total_reward = 0

for episode in range(episodes):

    print("\nEpisode", episode + 1)

    waiting_time = random.randint(1, 5)

    if policy == 1:

        print("Policy: First Available Representative")

        if waiting_time <= 2:
            reward = 10
        elif waiting_time <= 4:
            reward = 5
        else:
            reward = -2

    else:

        print("Policy: Random Representative")

        waiting_time = random.randint(1, 5)

        if waiting_time <= 2:
            reward = 8
        elif waiting_time <= 4:
            reward = 4
        else:
            reward = -3

    print("Waiting Time:", waiting_time)
    print("Reward:", reward)

    total_reward += reward

value_function = total_reward / episodes

print("\n---------------------------")
print("Simulation Completed")
print("---------------------------")
print("Total Reward:", total_reward)
print("Estimated Value Function:", round(value_function, 2))

if value_function >= 8:
    print("Excellent Assignment Policy")
elif value_function >= 5:
    print("Good Assignment Policy")
else:
    print("Needs Improvement")
