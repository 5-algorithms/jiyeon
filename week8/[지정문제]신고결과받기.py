def solution(id_list, report, k):
    reported = {}   # reported = {"신고당한유저":["신고한 유저들"]}    
    cnt = {}    # cnt = {"유저":메일받을횟수}
    # dictionary 초기화
    for id in id_list:
        reported[id] = []
        cnt[id] = 0
    # reported 채우기
    for r in set(report):
        reported[r.split()[1]].append(r.split()[0])
    # cnt 채우기
    for value in reported.values():
        if len(value) >= k:
            for user in value:
                cnt[user] += 1
    return list(cnt.values())
