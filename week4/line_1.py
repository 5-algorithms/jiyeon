from collections import Counter

def solution(logs):
    answer = []

    logs_uniq = list(set(logs))
    users = []
    probs = []
    for log in logs_uniq:
        users.append(log.split()[0])
        probs.append(log.split()[1])
    users = list(set(users))

    cnt_prob = Counter(probs)
    for k, v in cnt_prob.items():
        if v >= len(users)/2:
            answer.append(k)
    answer.sort()

    return answer