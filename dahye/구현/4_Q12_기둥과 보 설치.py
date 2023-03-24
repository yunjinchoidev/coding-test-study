def check(temp_list):
    for i in range(len(temp_list)):
        x = temp_list[i][0]
        y = temp_list[i][1]
        a = temp_list[i][2]
        if a == 1: #보일 때
            if [x, y-1, 0] in temp_list or [x-1, y, 0] in temp_list or ([x-1, y, 1] in temp_list and [x+1, y, 1] in temp_list):
                return True
                # check조건
                #1. 한쪽 끝이 기둥위에 있음 (왼쪽만확인해도괜찮음)
                #2. 한쪽 끝이 보임
                #3. 양쪽 끝 부분이 다른보와 동시연결
                #하나라도 해당되면 true
        else: #기둥일 때
            if (y == 0 or [x, y-1, 0] in temp_list and [x-1, y, 1] in temp_list) and temp_list.count([x, y, 0]) != 2:
                return True
    return False
                # check조건
                #1. 바닥 위에 있음
                #2. 보의 한쪽 끝 부분 위에 있음
                #3. 다른 기둥 위에 있음
                #하나라도 해당됨 and 4. 원래 기둥이랑 겹치면안됨 true
    

def solution(n, build_frame):
    temp_list = []
    #0 기둥, 1 보
    #0 삭제, 1 설치
    
    for build in build_frame:

        x = build[0]
        y = build[1]
        a = build[2]
        b = build[3]
        temp = [x, y, a]
        if b == 1: # 추가
            temp_list.append(temp)
            if check(temp_list) == False: #조건만족 못하면 삭제
                temp_list.pop()
        elif b==0 and len(temp_list) != 0 : # 삭제
            temp_list.pop()
            if check(temp_list) == False: #조건만족 못하면 다시 추가
                temp_list.append(temp)
    temp_list.sort()
    return temp_list

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5
print(solution(n, build_frame))