import random
import math

states = ["Low Demand", "Medium Demand", "High Demand"]
actions = ["Buy Energy", "Use Battery", "Sell Energy"]

episodes = int(input("Enter Number of Episodes: "))
max_kl = float(input("Enter Maximum KL Limit (Example 0.01): "))

policy = []

for i in range(len(states)):
    policy.append([0.33, 0.34, 0.33])

total_reward = 0

print("\nSmart Grid Energy Management using TRPO")
print("---------------------------------------")

for episode in range(episodes):

    state = random.randint(0, 2)

    old_policy = policy[state].copy()

    action = random.choices(
        range(3),
        weights=old_policy
    )[0]

    if state == 0:
        if action == 1:
            reward = 10
        elif action == 0:
            reward = 5
        else:
            reward = -5

    elif state == 1:
        if action == 1:
            reward = 8
        elif action == 0:
            reward = 5
        else:
            reward = 2

    else:
        if action == 0:
            reward = 10
        elif action == 2:
            reward = 8
        else:
            reward = -5

    total_reward += reward

    advantage = reward

    new_policy = old_policy.copy()

    new_policy[action] += 0.05 * advantage

    if new_policy[action] < 0.01:
        new_policy[action] = 0.01

    total = sum(new_policy)

    for j in range(3):
        new_policy[j] = new_policy[j] / total

    kl = 0

    for j in range(3):
        if new_policy[j] > 0:
            kl += old_policy[j] * math.log(
                old_policy[j] / new_policy[j]
            )

    if kl <= max_kl:
        policy[state] = new_policy

    print("\nEpisode:", episode + 1)
    print("State:", states[state])
    print("Action:", actions[action])
    print("Reward:", reward)
    print("KL Divergence:", round(kl, 4))

print("\n---------------------------------------")
print("Training Completed")
print("---------------------------------------")

print("Total Reward:", total_reward)

print("\nFinal Policy")

for i in range(3):

    print("\nState:", states[i])

    for j in range(3):
        print(
            actions[j],
            "Probability:",
            round(policy[i][j], 3)
        )
