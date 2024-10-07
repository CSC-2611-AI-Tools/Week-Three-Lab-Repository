import random


def generate_group_size_birthdays(group_size=100):
    """
    method for generating a list of birthdays for group sizes
    :param group_size:
    :return: list of birthdays
    """

    birthday_list = []

    for i in range(group_size):
        birthday_list.append((random.randint(1, 365)))

    return birthday_list


def compute_probability(user_group_size=23, number_of_simulation=1000):
    """
    method for computing the probability of 2 people sharing the same birthday
    :param user_group_size:
    :param number_of_simulation:
    :return: the probability value
    """

    duplicate_count = 0
    for i in range(0, number_of_simulation):
        birthday_list_sample = generate_group_size_birthdays(user_group_size)
        if len(birthday_list_sample) != len(set(birthday_list_sample)):
            duplicate_count = duplicate_count + 1
    probability_calculation = duplicate_count / number_of_simulation
    print("The probability of a group size of", user_group_size, "having a common birthday is",
          round(probability_calculation, 2))
    return probability_calculation


def smallest_group_size(number_of_simulation=1000):
    """
    method to compute the smallest group size that has a probability of greater than 50%
    of two people sharing the same birthday
    :return the probability value:
    """
    experimental_group_size = 1
    experimental_probability = 0
    while experimental_probability < 0.5:
        experimental_probability = compute_probability(len(generate_group_size_birthdays(experimental_group_size)),
                                                       number_of_simulation)
        experimental_group_size = experimental_group_size + 1
    return experimental_group_size


print(compute_probability())
print(compute_probability(50, 5000))
print(smallest_group_size())
