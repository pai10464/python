def read_answers(n):
    answers = []
    for k in range(n):
        sid, anss = input().split()
        answers.append([sid, anss])
    return answers


def marking(answer, solution):
    score = 0
    for i in range(len(answer)):
        if answer[i] == solution[i]:
            score += 1
    return score


def grading(scores):
    g = [[80, "A"], [70, "B"], [60, "C"], [50, "D"]]
    for a, b in g:
        if scores >= a:
            return b
    return "F"


def scoring(answers, solution):
    scores = []
    for sid, ans in answers:
        score = marking(ans, solution) / len(solution) * 100
        grade = grading(score)
        scores.append([sid, score, grade])
    return scores


def report(scores):
    for sid, sc, grade in scores:
        print(sid, sc, grade)


def sort(scores):
    x = []
    for sid, score, grade in scores:
        x.append([score, sid, grade])
    x.sort(reverse=True)
    for i in range(len(x)):
        scores[i] = [x[i][1], x[i][0], x[i][2]]


solution_real = input()
N = int(input())
ans = read_answers(N)
score = scoring(ans, solution_real)
sort(score)
report(score)
