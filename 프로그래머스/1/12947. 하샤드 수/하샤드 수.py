def solution(x):
  #  num_sum =   answer = True
    return x % sum([int(i) for i in str(x)]) == 0