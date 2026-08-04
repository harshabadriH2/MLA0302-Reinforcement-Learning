import random
import math

ads = int(input("Enter Number of Advertisements: "))
rounds = int(input("Enter Number of Rounds: "))

probability = []

print("\nEnter Click Probability (0 to 1) for each Advertisement")

for i in range(ads):
    p = float(input("Advertisement " + str(i + 1) + ": "))
    probability.append(p)

# ------------------------------
# Epsilon Greedy
# ------------------------------

epsilon = float(input("\nEnter Epsilon Value (Example 0.1): "))

reward_eg = 0

count = [0] * ads
value = [0] * ads

for i in range(rounds):

    if random.random() < epsilon:
        ad = random.randint(0, ads - 1)
    else:
        ad = value.index(max(value))

    click = 1 if random.random() < probability[ad] else 0

    reward_eg += click

    count[ad] += 1

    value[ad] = value[ad] + (click - value[ad]) / count[ad]

ctr_eg = reward_eg / rounds

# ------------------------------
# UCB
# ------------------------------

reward_ucb = 0

count = [0] * ads
value = [0] * ads

for i in range(rounds):

    if i < ads:
        ad = i

    else:

        ucb = []

        for j in range(ads):

            bonus = math.sqrt((2 * math.log(i + 1)) / count[j])

            ucb.append(value[j] + bonus)

        ad = ucb.index(max(ucb))

    click = 1 if random.random() < probability[ad] else 0

    reward_ucb += click

    count[ad] += 1

    value[ad] = value[ad] + (click - value[ad]) / count[ad]

ctr_ucb = reward_ucb / rounds

# ------------------------------
# Thompson Sampling
# ------------------------------

reward_ts = 0

success = [1] * ads
failure = [1] * ads

for i in range(rounds):

    sample = []

    for j in range(ads):
        sample.append(random.betavariate(success[j], failure[j]))

    ad = sample.index(max(sample))

    click = 1 if random.random() < probability[ad] else 0

    reward_ts += click

    if click == 1:
        success[ad] += 1
    else:
        failure[ad] += 1

ctr_ts = reward_ts / rounds

# ------------------------------
# Result
# ------------------------------

print("\n--------------------------------")
print("Advertisement Bandit Algorithms")
print("--------------------------------")

print("Epsilon Greedy CTR :", round(ctr_eg,3))
print("UCB CTR            :", round(ctr_ucb,3))
print("Thompson CTR       :", round(ctr_ts,3))

best = max(ctr_eg, ctr_ucb, ctr_ts)

if best == ctr_eg:
    print("\nBest Algorithm : Epsilon Greedy")

elif best == ctr_ucb:
    print("\nBest Algorithm : UCB")

else:
    print("\nBest Algorithm : Thompson Sampling")
