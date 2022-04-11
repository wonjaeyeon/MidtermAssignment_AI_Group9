# 25구획, 구역 내 평균 노드 40개 기준 예시 입니다
# 노드가 몇 개가 되든, 부모의 수는 20개로 고정된다. 노드가 10개라고 해도 부모 20개는 충분히 만든다
NUM_OF_PARENTS = 20
NUM_OF_OFFSPRINGS = 5
# 해당 값은 전역입니다. 제발 인자로 넘기지 마세요

class City:
    def __init__(self, xPos, yPos, index):
        self.xPos = xPos  # 해당 지점의 x좌표
        self.yPos = yPos  # 해당 지점의 y좌표
        self.index = index  # 해당 지점의 번호 인덱스


class CityInRange:
    nodesInRange = []  # int형 인덱스 방식으로 해당 범위 내 city 데이터를 저장하는 list
    count = 0  # 범위 내 city 수
    vIndex1, vIndex2 = 0  # GA로 산출된 해당 경로의 양 끝 지점 인덱스
    bestCost, worstCost = 0  # 범위 내 parent들의 fitness를 구하는 데 사용되는 cost 값
    resultCost = 0  # GA로 산출된 해당 경로의 비용 (되돌아오는 비용은 제외한다)

class GAparent:
    nodesInPath = []  # int형 인덱스 방식으로 path 데이터 순서를 저장하는 list
    cost = 0  # 해당 경로의 cost (복귀 비용 제외)
    fitness = 0  # selection 단계에서 구함

# 단순히 nodes에 append하는 건 굳이 함수를 써야 할까
# parents[45].nodes.append(581)

class GAoffsping:
    nodesInPath = []  # int형 인덱스 방식으로 path 데이터 순서를 저장하는 list
    cost = 0  # 해당 경로의 cost (복귀 비용 제외)
    # fitness 값을 쓰이지 않습니다
    p1Index, p2Indes = 0  # 자신을 구성하는 두 부모의 인덱스
    # 이 인덱스는 parents[] 해집합에서의 인덱스입니다

# crossover에 간선 재조합에서 사용
class Neighbor:
    neighborNode = -1
    for i in range(4):  # 이웃한 노드의 목록
        count = 0  # 유효한 이웃의 수



