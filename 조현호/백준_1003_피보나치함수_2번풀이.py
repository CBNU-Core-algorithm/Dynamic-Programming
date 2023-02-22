# https://blog.naver.com/cottonnee/223003254093
# 피보나치 수열의 소스코드를 재귀함수로 작성하면 f(n)에서 n이 커지면 커질수록
# 수행 시간이 기하급수적으로 늘어나는 문제가 발생한다.
# 빅오 표기법으로 시간 복잡도를 표기하면 O(2^n)의 지수 시간이 소요된다.
# 따라서 피보나치 수열을 재귀함수로 만들면 문제를 효율적으로 해결할 수 없다.

import sys
sys.stdin = open('a.txt', 'rt') # 테스트용 코드
input = sys.stdin.readline

# 다이나믹 프로그래밍을 통한 피보나치 함수
def fibonacci(n):
	# 0, 1, 2 .. 일 때의 0과 1개수 리스트
	zero = [1, 0, 1]
	one = [0, 1, 1]
	if n >= 3:
		for i in range(3, n + 1):
			zero.append(zero[i-2] + zero[i-1])
			one.append(one[i-2] + one[i-1])

	return zero[n], one[n]


# 값 입력받고, 동시에 계산하고 출력하기
t = int(input())

for _ in range(t):
	# case 입력받기
	case = int(input())

	# 계산 및 출력
	zero, one = fibonacci(case)
	print(zero, one)
