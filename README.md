
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

----
# 코딩테스트에서 많이 쓰이는 표현

```python
import sys
input = sys.stdin.readline
```

```python
from itertools import permutations, combinations, product, combinations_with_replacement # 완전 탐색
```

```python
from collections import Counter, deque # 해시, 큐
```

```python
import heapq # 우선 순위 큐
```

```python
from bisect import bisect_left, bisect_right # 정렬된 배열에서 특정한 원소
```

```python
from math import prod, factorial # 리스트 원소 내의 곱
from math import gcd # 최대공약수 gcd
```

```python
from functools import reduce
```


# 알고리즘 이론
## 01. Stack
> 📦 **Stack** 스택
>
> 
> 가장 최근에 추가한 요소만 제거할 수 있는 선형 자료구조
> 
> - **LIFO 후입 선출 자료구조** : 마지막에 추가한 요소부터 꺼낼 수 있는 자료구조
- `push()` 스택에 요소 추가
- `pop()` 스택에 마지막으로 추가한 요소를 꺼내는 것을 의미
- `peek()` 스택의 마지막에 있는 요소를 제거하지 않고 접근만 함

**스택을 사용해 문자열 뒤집기**

- `a_string[::-1]`
- `‘’.join(reversed(’a string’))`

## 02. Queue
> 📦 **Queue** 큐
>
>
> 뒤에서부터 요소를 추가하고 앞에서부터 요소를 꺼내는 선형 자료 구조
> 
> - **FIFO 선입선출 자료구조 :** 가장 먼저 추가한 요소부터 제거하는 자료구조
>
Queue를 구현할 때는 Stack과 달리 덱을 활용해 구현해야 시간 복잡도가 터지지 않음
- `queue.LifoQueue()` 후입선출(가장 마지막에 추가된 요소 제거)
- `PriorityQueue()`  우선 순위를 부여해 우선순위가 높은 요소 먼저 제거
    - 우선순위는 숫자가 작을수록 높음
- `deque`
        요소를 큐에서 제거하는 것을 의미하며 큐의 앞부분에서 요소 제거
  - list는 삭제, 삽입 모두 가장 뒤쪽 원소 기준
  - `popleft()` 첫번째 원소 삭제
  - `append(x)` 마지막 인덱스에 삽입
  - `pop(x)` 마지막 원소 삭제
  - `appendleft(x)` 첫번째 인덱스 삽입 가능
    
⏪ **스택** 한 쪽이 막힌 상자에 자료를 차곡 차곡 쌓아 위에서부터 꺼냄 

⏩ **큐** 입구와 출구가 따로 있는 통로로 한쪽에서 밀어 넣으면 반대편으로 나오는 것

## 03. Hash
> 🔑 **Hash** 해시
>
> 
> 고유한 키를 사용해 키-값 쌍을 저장하는 선형 자료 구조
> 
> - 키 : 고유해야 하므로 테이블에 중복된 키 저장 불가

`from collections import Counter`

## 04. 완전 탐색 
> 🌐 **완전 탐색**
> 
> 
> 가능한 경우의 수를 모두 나열하면서 원하는 답을 찾는 방법 
>
- 전체를 하나하나 다 따져보기 때문에 Brute-Force라고도 함
- 대신 모든 경우를 전부 따져야 하기 때문에 경우의 수가 매우 많아지는 문제에 대해서는 제한 시간 내에 해결이 힘들 수 있음
- 시간 복잡도
    - 완전탐색을 풀 때는 주로 입력의 개수(N)이 작을 때가 좋음
    - 시간복잡도가 *O*($2^N$) 혹은 *O*($*N!*$)이기 때문에 N의 크기가 증가할수록 복잡도는 폭발적으로 증가

#### 단순 Brute-Force

- 모든 경우를 다 검사하여 원하는 값을 탐색하는 방법

#### 비트마스크(Bitmask)

- 모든 경우의 수를 **이진수로 표현**하여 빠르게 계산을 해 나아가는 방식
	- bin(x)[:2]

#### 백트래킹

- 해결책을 찾아가는 도중에 막히게 되면 다시 돌아가서 다른 경로로 탐색을 하여 결국 모든 가능한 경우의 수를 탐색하여 해결책을 찾아가는 방식

#### 순열

- 서로 다른 n개 중에서 r개를 선택해서 나열하면서 모든 경우의 수를 탐색하는 방식

#### 재귀함수

- 자기 자신을 호출하며 모든 가능한 경우를 체크하면서 최적의 해답하는 방법
  - 최대공약수 구하는 예제
      ```python
      def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a%b) # b와 a를 b로 나눈 나머지를 반환
      ```
  - 최소공배수 구하는 예제
    ```python
    def lcm(a, b):
	    return (a*b) // gcd(a, b)
    ```

## 05. 탐욕법
> 🍏 **Greedy** 탐욕법 알고리즘
>  
> 
> 현재 상황”에서 가장 좋은 것을 고르는 알고리즘

## 06. 깊이/너비 우선탐색 (DFS/BFS)
> 📄 **그래프**
> 
> node랑 해당 node를 연결하는 edge로 이뤄진 자료구조의 일종으로 하나의 정점으로부터 시작해 차례대로 모든 정점들을 한번씩 방문
> 
> - 그래프를 탐색하는 방법에는 DFS, BFS 두가지 방법이 존재


**DFS**

- 탐색 시작 노드를 스택에 삽입하고 방문처리
- 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리
    - 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
- 더 이상 위 과정을 수행할 수 없을 때까지 반복

## 07. Heap
> 🗄️ **Heap 힙**
> 
> 힙은 주로 이진트리(자녀가 최대 두개인) 기반으로 구현
> 
- 최대값 또는 최소값 반환(`top` 또는 `peek`), 요소의 삽입(`push`), 뿌리 노드 삭제(`pop`), 뿌리 노드 교체(`replace`)
- Max Heap
    - 부모 노드의 값이 항상 자식 노드의 값 보다 크거나 같음
    - root 노드는 항상 힙의 최대값
- Min Heap
    - 부모 노드의 값이 항상 자식 노드의 값 보다 작거나 같음
    - 뿌리 노드는 항상 힙의 최솟값
