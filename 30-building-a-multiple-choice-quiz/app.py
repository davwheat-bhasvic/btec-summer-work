from Question import Question

questions = [
    Question("What colour are apples?\n(a) red\n(b) blue\n(c) yellow", "a"),
    Question("What colour are strawberries?\n(a) red\n(b) blue\n(c) yellow", "a"),
    Question(
        "What is the best mobile network?\n(a) VOXI\n(b) Smarty\n(c) giffgaff", "c"
    ),
]


def run_test(questions):
    score = 0

    for question in questions:
        print("\n--------------------------\n" + question.prompt)
        ans = input("\nAnswer: ")

        if ans.lower().rstrip() == question.answer.lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect.")

    return score


result = run_test(questions)

print(f"\nYou scored {result}/{len(questions)}.")
