def main():

    score = float(input("Enter score: "))

    rating = rate_score(score)

    print(rating)

    import random

    rating_random = rate_score(random.randint(1, 100))
    print(rating_random)


def rate_score(score):
    if score > 100 or score < 0:
        return "Invalid Choice"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()