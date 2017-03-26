def main():
    score = float(input("Enter score: "))
    print(scoreGrade(score))


def scoreGrade(score):
    if score < 0 or score > 100:
        return"Invalid score"
    elif 50 <= score < 90:
        return"Passable"
    elif score >= 90:
        return"Excellent"
    else:
        return"Bad"

main()
