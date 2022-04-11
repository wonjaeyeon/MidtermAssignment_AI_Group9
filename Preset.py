# <Preset 단계>
# parent 각각의 비용 및 적합도를 구함
import math
import random
import Cities

# 각 구역에 대해 최초 부모 해집단을 생성하는 함수
# nodesList = CityInRange.nodesInRange
def getFirstParents(parents, nodesList):
	for i in range(Cities.NUM_OF_PARENTS):
		# 임의의 노드 배열을 생성, 값만 할당한다
		random.shuffle(nodesList)
		parents[i].nodesInPath = nodesList.copy()
		# 이때 각 parent의 cost도 같이 할당한다
		parents[i].cost = getCost(Cities.nodesInPath)

		# cost를 구한 parent는 즉시 cost 순서에 따라 정렬한다
		# 인덱스 값이 클수록, cost값이 큰 비효율적인 값이다
		for j in range(i):
			if parents[i-j].cost < parents[i-j-1].cost:
				tmpCost = parents[i-j-1].cost
				tmpPath = parents[i-j-1].path
				parents[i-j-1] = parents[i-j].copy()
				parents[i-j-1].cost = parents[i-j].cost
				parents[i-j] = tmpPath.copy()
				parents[i-j].cost = tmpCost
			else:
				# 아니라면 상위에 정렬된 것들과도 비교할 필요가 없으니 종료
				break
	# return
	# best 및 worst 코스트에 대해서는 함수 외부에서 인덱스 참조로 바로 구할 수 있다

# 하나의 parent에 대해 cost를 구하는 함수
# bestCost, worstCost는 이 함수 밖에서 리턴 값으로 판단 및 저장
# parent 내 nodesInPath 리스트만 path로 넘긴다
def getCost(path):
	totalCost = 0
	# 여기 카운트는 멤버 변수값이 아니라 list 자체 제공값
	for i in range(path.nodeInPath.count-1):	# N-1에서 0으로 가는 경로는 제외
		totalCost += distance(path[i], path[i+1])	# 두 경로 사이의 값을 리턴
	return totalCost


# select 단계에서 쓰이는 fitness 값을 구하는 함수
# 품질 비례 룰렛 휠에서 쓰이는 방식이다
# 마찬가지로 sumOfFitness는 이 함수 밖에서 계산한다
def getFitness_1(best, worst, current, k=4):
	return (worst - current) + (worst - best) / (k-1)

# 순위 기반 선택에서 쓰이는 방식이다
# iteration은 함수 외부의 for문에서 받고, min, max는 사용자 지정 값이다
def getFitness_2(min, max, iteration):
	return max + (iteration - 1) * (min - max) / (Cities.NUM_OF_PARENTS - 1)

# import math해야 함
def distance(index1, index2):
	result = (Cities.totalMap[index2].xPos - Cities.totalMap[index1].xPos) ^ 2 + (Cities.totalMap[index2].yPos - Cities.totalMap[index1].yPos) ^ 2
	return math.sqrt(result)
