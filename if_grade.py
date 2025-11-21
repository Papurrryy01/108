def grade_from_score(score: int) -> str:
    if score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    else:
        return "F"


def main():
    try:
        s = input("Enter a score from 1-100: ")
        score = int(s)
    except ValueError:
        print("Please enter a valid integer.")
        return

    if not (1 <= score <= 100):
        print("Score must be between 1 and 100.")
        return

    grade = grade_from_score(score)
    print(f"Grade: {grade}")

    passed = score >= 70
    if passed:
        print("congratulations!")
    else:
        print("Try Again!!!")


if __name__ == "__main__":
    main()
