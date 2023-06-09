# 영역 카운팅(=도착=~까지)은 "인덱스 끝" 기준 / 따라서 index = '0' ~ 'd' (distance = d)

def checkIsAvailable(_position, _arr, _time, _times) -> bool:
    patrol_index = _arr[_position] -1       # 순찰병 번호 = 인덱스 + 1
    work_time, play_time = _times[patrol_index][0], _times[patrol_index][1]
    if 0 <_time%(work_time + play_time)<=work_time : return False
    else : return True

def makeSorted(_val1, _val2) -> (int, int):
    if _val1 < _val2 : return _val1, _val2
    else : return _val2, _val1

def makeInfoArr(_scope, _arr) -> list:
    for patrol_index in range(len(_scope)):
        start_range, finish_range = makeSorted(_scope[patrol_index][0], _scope[patrol_index][1])
        for i in range(start_range,finish_range+1): # start_scope <= x <= finish scope
            _arr[i] = patrol_index + 1              # 순찰병 번호 = 인덱스 + 1
    return _arr

def solution(distance, scope, times):
    arr = makeInfoArr(scope, [0]*distance)
    for move_index in range(distance):      # time = move_index (화랑이가 1m/s로 고정되어 있기 때문)
        if not arr[move_index] : continue
        if not checkIsAvailable(move_index, arr, move_index, times) :
            return move_index
    return distance
