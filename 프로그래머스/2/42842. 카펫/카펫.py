def solution(brown, yellow):
  #  answer = []
    n = brown + yellow
    
    for i in range(1, (n+1)):
        if n % i == 0:
            width = n // i
            height = i
    
          #  print(width, height)
        
            if width >= height and (width - 2) * (height - 2) == yellow:
                return [width, height]
   