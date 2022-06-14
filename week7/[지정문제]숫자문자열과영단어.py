def solution(s):
    answer = ''
    number = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 
              'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    word = ''
    for letter in s:
        
        if letter.isdigit():
            answer += letter
        else:
            word += letter
            if word in list(number.keys()):
                answer += number[word]
                word = ''
    return int(answer)