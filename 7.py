import random
import matplotlib.pyplot as plt

def roll_dice(num_rolls):
    results = [0] * 13 

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        results[roll_sum] += 1

    probabilities = [count / num_rolls for count in results[2:]]

    return probabilities



def plot_probabilities(probabilities):
    sums = list(range(2, 13))
    for sum_value, probability in zip(sums, probabilities):
        print(f"Summ: {sum_value}, Probability: {probability:.4f}")

    plt.bar(sums, probabilities, tick_label=sums)
    plt.xlabel('Summ of dices numbers')
    plt.ylabel('Probability')
    plt.title('Probability of the summ of both dices numbers')
    plt.show()

for accurancy in [100,1000,10000,100000]:
  probabilities = roll_dice(accurancy)
  
  plot_probabilities(probabilities)