import random

states = [
    "Straight",
    "Left Turn",
    "Right Turn",
    "Sharp Turn"
]

actions = [
    "Accelerate",
    "Brake",
    "Turn Left",
    "Turn Right",
    "Straight"
]

episodes = int(input("Enter Number of Episodes: "))
track_length = int(input("Enter Track Length: "))

learning_rate = 0.1
gamma = 0.9

actor = {}

critic = {}

for state in states:
    actor[state] = [0.2, 0.2, 0.2, 0.2, 0.2]
    critic[state] = 0

total_race_reward = 0

print("\nA2C Autonomous Racing Training\n")

for episode in range(episodes):

    position = 0
    speed = 0
    episode_reward = 0

    print("Episode:", episode + 1)

    for step in range(track_length):

        state = random.choice(states)

        probabilities = actor[state]

        action_index = random.choices(
            range(len(actions)),
            weights=probabilities
        )[0]

        action = actions[action_index]

        if state == "Straight":

            if action == "Accelerate":
                reward = 10
                speed += 2

            elif action == "Straight":
                reward = 6
                speed += 1

            else:
                reward = -2

        elif state == "Left Turn":

            if action == "Turn Left":
                reward = 10
                speed += 1

            elif action == "Brake":
                reward = 5
                speed -= 1

            else:
                reward = -5

        elif state == "Right Turn":

            if action == "Turn Right":
                reward = 10
                speed += 1

            elif action == "Brake":
                reward = 5
                speed -= 1

            else:
                reward = -5

        else:

            if action == "Brake":
                reward = 8
                speed -= 1

            else:
                reward = -6

        if speed < 0:
            speed = 0

        position += speed

        if position > track_length:
            position = track_length

        episode_reward += reward

        next_value = critic[state]

        target = reward + gamma * next_value

        advantage = target - critic[state]

        critic[state] += learning_rate * advantage

        if advantage > 0:

            actor[state][action_index] += learning_rate * advantage

        else:

            actor[state][action_index] += learning_rate * advantage

        for i in range(len(actor[state])):

            if actor[state][i] < 0.01:
                actor[state][i] = 0.01

        total = sum(actor[state])

        for i in range(len(actor[state])):
            actor[state][i] /= total

        if position >= track_length:
            break

    total_race_reward += episode_reward

    print("Position:", position)
    print("Reward:", episode_reward)
    print()

print("--------------------------------")
print("A2C Training Completed")
print("--------------------------------")

average_reward = total_race_reward / episodes

print("Total Reward:", total_race_reward)
print("Average Reward:", round(average_reward, 2))

print("\nLearned Racing Policy")

for state in states:

    best_action = actor[state].index(
        max(actor[state])
    )

    print(state, "->", actions[best_action])
