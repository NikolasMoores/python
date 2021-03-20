def main():

    score = float(input("Enter score: "))

    rating = rate_score(score)

    print(rating)


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