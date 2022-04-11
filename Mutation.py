import random
import Cities
# <Mutation 단계> 1개 + 1개(보류)

# (1) 전형적 변이

def simpleMutation(offsprings, cityCounts):
    # 인접한 두 노드의 값 변환
    for current in range(0, Cities.NUM_OF_OFFSPRINGS):
        pointIndex = random.randint(0, cityCounts - 1)
        # 쉬운 연산자 있는 거 아는데, 너무 끔찍하게 길다
        tmpVal = offsprings[current].nodesInPath[pointIndex]
        offsprings[current].nodesInPath[pointIndex] = offsprings[current].nodesInPath[pointIndex + 1]
        offsprings[current].nodesInPath[pointIndex + 1] = offsprings[current].nodesInPath[pointIndex]


# (2) 지역 최적화; 보류
# localOptimization

# <Inversion 단계> 2개

# (1) parents (집합) 내 최악해와 대치
# 각 parent가 상위 단계에서 경로 크기 순서로 정렬된 상태라 가정한다
# 또한 각 offspring은 본인의 cost 값을 구해왔다고 가정한다
def inverseWithWorst(offsprings, parents):
    # 변동된 순위 정보를 기록하는 int형 리스트
    # -1은 기존의 부모 데이터가 사용됨을, 그 이상의 정수 값은 새로운 자식 데이터의 인덱스를 의미
    rankList = [-1 for i in range(Cities.NUM_OF_PARENTS)]

    for current in range(Cities.NUM_OF_OFFSPRING):
        parentIndex = 0

        # 만약 자식의 cost가 부모 집합 내 최악보다 나쁘면 판단하지 않는다
        if offsprings[current].cost >= parents[Cities.NUM_OF_PARENTS]:
            continue
        for rankIndex in range(Cities.NUM_OF_PARENTS):
            # 제일 위에서부터 비교한다

            # 해당 위치가 부모라면
            if rankList[rankIndex] == -1:
                if offsprings[current].cost < parents[parentIndex]:
                    rankList[rankIndex] = current
                else:
                    parentIndex = parentIndex + 1

            # 해당 위치가 다른 자식이라면
            else:
                if offsprings[current].cost < offsprings[rankList[rankIndex]].cost:
                    rankList = rankShift(rankList, rankIndex + 1, rankList[rankIndex]).copy()
                    rankList[rankIndex] = current


# 이렇게 산출된 rankList에 따라 실제 parents 집합의 값을 바꾼다


# 재귀 방식의 랭킹 시프팅(밀어내기) 함수
# rankToShift는 대상이 이동해야(내려가야)할 위치의 인덱스 값
# offspringToShift는 밀려나는 자식의 offsprings 내 인덱스 값
def rankShift(rankList, rankToShift, offspringToShift):
    tmp = rankList.copy()

    # 밀려나는 위치가 out of index라면 그냥 리턴
    if rankToShift >= Cities.NUM_OF_PARENTS:
        return tmp

    # 다음 값도 자식이라면, 우선 그 자식을 옮긴 뒤 대체
    if tmp[rankToShift] != -1:
        tmp = rankShift(tmp, rankToShift + 1, tmp[rankToShift]).copy()
    else:
        pass

    # 다음 빈 자리가 생겼다고 상정, 값을 대체한다
    tmp[rankToShift] = offspringToShift
    return tmp


# rankList의 정보를 parents 집합에 반영하는 함수

# (2) 각 offspring이 자신의 부모보다 우월한 경우 그 부모와 대치
# 각 parent가 상위 단계에서 경로 크기 순서로 정렬된 상태라 가정한다
# 또한 각 offspring은 본인의 cost 값을 구해왔다고 가정한다
def invserseWithParents(offsprings,current, parent):
    # 변동된 순위 정보를 기록하는 int형 리스트
    # -1은 기존의 부모 데이터가 사용됨을, 그 이상의 정수 값은 새로운 자식 데이터의 인덱스를 의미
    rankList = [-1 for i in range(Cities.NUM_OF_PARENTS)]

    p1 = offsprings[current].p1Index
    p2 = offsprings[current].p2Index

    # 부모 대체 가능 여부
    canInvertP1 = False;
    canInvertP2 = False;

    if offsprings[current].cost < parent[p1].cost:
        canInvertP1 = True
    if offsprings[current].cost < parent[p2].cost:
        canInvertP2 = True

        # 아예 저열한 offspring
        # 한 부모 보다만 우월한 offspring
        # 두 부모 둘다보다 우월한 offspring

        # 원칙1: 최대한 많은 offspring을 살려서 간다
        # 원칙2: 두 부모 둘 다 대치할 수 있는 경우, 저열해를 대치하는 것이 우선이다
        #// 여기는
        #나중에..,

# 이렇게 산출된 rankList에 따라 실제 parents 집합의 값을 바꾼다