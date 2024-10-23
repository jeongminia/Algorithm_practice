def solution(name, yearning, photo):
    answer = []
    photo_cnt = 0
    name_dict = {name[i]: yearning[i] for i in range(len(name))}
  #  print(name_dict)
    
    while True:
        photo_lst = photo[photo_cnt]
     #   print(photo_lst)
        
        photo_value = 0
        for j in photo_lst:
            if j not in name:
                pass
            else:
      #          print(j, name_dict[j])
                photo_value += name_dict[j]
        
        answer.append(photo_value)
    #    print(photo_value)
        
        photo_cnt += 1
        if photo_cnt >= len(photo):
            break
        
    return answer