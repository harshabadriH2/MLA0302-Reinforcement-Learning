import random

intersections = int(input("Enter Number of Intersections: "))

destination = int(input("Enter Destination Intersection (0-" + str(intersections-1) + "): "))

current = int(input("Enter Starting Intersection: "))

print("\nPolicies")
print("1. Safe Driving Policy")
print("2. Fast Driving Policy")

policy = int(input("Choose Policy: "))

reward = 0
steps = 0

while current != destination:

    print("\nCurrent Intersection:", current)

    if policy == 1:

        print("Traffic Rule Followed")

        if current < destination:
            current += 1
        else:
            current -= 1

        reward += 5

    else:

        move = random.randint(1,2)

        current = current + move

        if current > destination:
            current = destination

        if move == 2:
            print("Speeding at Intersection")
            reward -= 2
        else:
            reward += 3

    steps += 1

print("\nDestination Reached")

reward += 10

print("\nTotal Steps =", steps)
print("Total Reward =", reward)

print("\nPolicy Evaluation")

if reward >= 25:
    print("Excellent Policy")

elif reward >= 15:
    print("Good Policy")

else:
    print("Needs Improvement")
