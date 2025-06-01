'''
columns = ['code', 'date', 'maximum', 'remain']

ext: 해당 컬럼을 기준으로 데이터를 추출
val_ext: 뽑아낼 정보의 기준값을 나타내는 정수
=> ext < val_ext

sort_by: 정보를 정렬할 기준이 되는 문자열

ext값이 val_ext보다 작은 데이터만 추출 -> sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
'''

def solution(data, ext, val_ext, sort_by):
    columns = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    
    answer = []
    for i in range(len(data)):
        check = data[i]
        
        j = columns[ext]
        if check[j] < val_ext:
            answer.append(check)
        
    standard = columns[sort_by]
 #   print(standard)
    
 #   print(sorted(answer, key=lambda x: x[standard]))
    
    
    return sorted(answer, key=lambda x: x[standard])