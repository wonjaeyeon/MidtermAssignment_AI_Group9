import Cities
import random
# <Crossover 단계> 4개

# 만약에 클래스 형이 call by ref 안되면 그때가서 다시 수정하기

# (1) 사이클 교차
# offspring 가져와서 멤버 접근으로 직접 수정...이 되!?
# cityCount는 splittedMap.count값을 받아옴
def cycleCrossover(offsprings, parents, cityCount):

    # offsprings에 넘겨줄 배열 초기화, 값은 -1
    # 이거 에러나면 그냥 각각 append해주자. 그렇게 오래 안 걸려

    result = [[-1 for i in range(cityCount)] for j in range(Cities.NUM_OF_OFFSPRINGS)]

    searchP1 = True  # T이면 P1에 대해, F이면 P2에 대해 값을 받는다
    insertIndex = 0  # 할당 작업이 진행되는 노드(도시) 위치
    unReceived = 0  # 값이 할당되지 않은 offspirngs 내 원소 중 가장 좌측 인덱스

    # 너무 길어서 축약
    for current in range(Cities.NUM_OF_OFFSPRINGS):
        p1 = offsprings[current].p1Index
    p2 = offsprings[current].p2Index

    # offspings의 모든 노드 인자가 채워지면 break
    while True:
        # p1은 넣고, p2는 배제
        if (searchP1):
            while True:
                # P1에서 동일 위치에 대해 값 할당
                result[current][insertIndex] = parents[p1].nodesInPath[insertIndex]
                offsprings[current].nodesInPath[insertIndex] = parents[p1].nodesInPath[insertIndex]

                # 이때 parent[p2].배열[insertIndex] 값은 채택되지 못하므로 S1에서 채택
                # 작업을 진행할 새로운 index 잡기
                insertIndex = parents[p1].nodesInPath.index(parents[p2].nodesInPath[insertIndex])

                # 이미 값이 할당된 부분이라면 종료
                if (result[current][insertIndex] != -1):
                    break
                if (offsprings[current].nodesInPath[insertIndex] != -1):
                    break

        # p2는 넣고, p1은 배제
        else:
            while True:
                result[current][insertIndex] = parents[p2].nodesInPath[insertIndex]
                offsprings[current].nodesInPath[insertIndex] = parents[p2].nodesInPath[insertIndex]
                insertIndex = parents[p2].nodesInPath.index(parents[p1].nodesInPath[insertIndex])
                if (result[current][insertIndex] != -1):
                    break
                if (offsprings[current].nodesInPath[insertIndex] != -1):
                    break

        # 사이클 교차를 진행할 다음 위치 잡기; offsprings 내 할당되지 않은 최좌측
        while result[current][unReceived] != -1:
            while offsprings[current].nodesInPath[unReceived] != -1:
                unReceived = unReceived + 1

        # 해당 할당되지 않은 위치가 다음 작업 지점
        insertIndex = unReceived
        # 플래그 반전
        searchP1 = not(searchP1)

        # 해당 offspring의 모든 값이 할당된 상태라면 종료
        if insertIndex > cityCount:
            break
    return result


# (2) 순서 교차
def orderCrossover(offsprings, parents, cityCount):
    cut_index1, cut_index2 = 0  # 자름선. 만약 cut_index=3이면 3과 4 사이를 자른다는 의미
    p2_insertIndex = 0  # p2의 작업 위치를 정하는 인덱스
    insertVal = 0  # p2에서 대체하려는 값

    # current 번째 offspring에 대해서 작업
    for current in range(0, Cities.NUM_OF_OFFSPRINGS):

        # 부모 자체에 접근하기 위한 인덱스 값
        p1 = offsprings[current].p1Index
        p2 = offsprings[current].p2Index

        # 랜덤한 정수 값을 리턴 (반드시 cut_index1 < cut_index2)
        cut_index1 = random.randint(0, cityCount - 1)  # 0에서 N-2 사이에 리턴된다
        cut_index2 = random.randint(cut_index1 + 1, cityCount)

        # 자름선 사이의 값을 그대로 적용 (cut_index1 + 1 ~ cut_index2)
        for insertIndex in range(cut_index1 + 1, cut_index2 + 1):
            offsprings[current].nodesInPath[insertIndex] = parents[p1].nodesInPath[insertIndex]

        # offsping은 0 인덱스부터, p2는 cut_index2 + 1부터 적용
        p2_insertIndex = cut_index2 + 1

        # 추가한 코드 p2_repaceIndex에 대해 추가 -> 따로 값이 없어서
        p2_replaceIndex = cut_index1 + 1

        for insertIndex in range(0, cityCount):
            # 자름선 내 값에 대해서는 작업하지 않는다
            if insertIndex == cut_index1 + 1:
                insertIndex = cut_index2 + 1

            insertVal = parents[p2].nodesIsPath[p2_insertIndex]

            # p2에서 차용하려는 값이 이미 자름선 내에서 적용된 값이라면, 다음 p2를 탐색
            while not isValid(offsprings[current].nodesInPath, insertVal, cut_index1, cut_index2):
                p2_insertIndex = p2_replaceIndex + 1
                # 만약 인덱스 값을 초과했다면 처음으로 돌림
                if p2_insertIndex >= cityCount:
                    p2_insertIndex = 0
                insertVal = parents[p2].nodesIsPath[p2_insertIndex]

            # p2에서 값 적용
            offsprings[current].nodesInPath[insertIndex] = insertVal


# return

# isValid 함수; 인덱스가 이미 사용된 부분이면 false 리턴
# o = offspring[current].nodesInPath, pVal = parent[p2].nodesInPath[p2_insertIndex], cut_index1, cut_index2
def isValid(o, pVal, cut_index1, cut_index2):
    for i in range(cut_index1 + 1, cut_index2 + 1):
        if o[i] == pVal:
            return False  # 이미 사용된 값입니다
    # 중복이 없다면 통과
    return True


# (3) PMX
def PMX(offsprings, parents, cityCount):
    # 자름선. 만약 cut_index=3이면 3과 4 사이를 자른다는 의미
    cut_index1, cut_index2 = 0

    p2_replaceIndex  = 0 # 값을 대체할 p2내 위치
    insertVal = 0 # p2에서 대체하려는 값

    # current 번째 offspring에 대해서 작업
    for current in range(0, Cities.NUM_OF_OFFSPRINGS):

        # 부모 자체에 접근하기 위한 인덱스 값
        p1 = offsprings[current].p1Index
        p2 = offsprings[current].p2Index

        # 랜덤한 정수 값을 리턴 (반드시 cut_index1 < cut_index2)
        cut_index1 = random.randint(0, cityCount - 1)  # 0에서 N-2 사이에 리턴된다
        cut_index2 = random.randint(cut_index1 + 1, cityCount)

        # 자름선 사이의 값을 그대로 적용 (cut_index1 +1 ~ cut_index2)
        for insertIndex in range(cut_index1 + 1, cut_index2 + 1):
            offsprings[current].nodesInPath[insertIndex] = parents[p1].nodesInPath[insertIndex]

        # 값 중복 시 자름 선 내 p2 값에 접근하기 위한 인덱스 변수
        p2_replaceIndex = cut_index1 + 1

        for insertIndex in range(0, cityCount):
            # 자름선 내 값에 대해서는 작업하지 않는다
            if insertIndex == cut_index1 + 1:
                insertIndex = cut_index2 + 1

            # 일단은 offspring과 p2의 위치를 맞춰 넣는다
            insertVal = parents[p2].nodesInPath[insertIndex]

            # p2에서 차용하려는 값이 이미 자름선 내에서 적용된 값이라면, 자름선 내 p2 원소로 대체
            while not isValid(offsprings[current].nodesInPath, insertVal, cut_index1, cut_index2):
                insertVal = parents[p2].nodesInPath[p2_replaceIndex]
                p2_replaceIndex = p2_replaceIndex + 1

            # 어디서 왔든, 중복되지 않는 값이 들어간다
            offsprings[current].nodesInPath[insertIndex] = insertVal


# return

# 해당 방식의 isValid 함수는 (2)번의 것과 동일하다


# (4) 간선 재조합
def assemblyCrossover(offsprings, parents, cityCounts):
    table = []

    neighborIndex = 0
    insertVal = 0  # neighbor만들 때 한번
    tmpCountl, insertCount = 0
    reference = 0  # 접근하는 이웃 테이블 상 인덱스

    for i in range(0, cityCounts):
        table.append(Cities.Neighbor())

    # current 만큼 이웃 테이블을 제작, 사용한다
    for current in range(0, Cities.NUM_OF_OFFSPRING):

        p1 = offsprings[current].p1Index
        p2 = offsprings[current].p2Index

        # p1의 이웃 정보를 적용
        for i in range(0, cityCounts):
            # parent는 자신의 앞/뒤 인덱스의 값을 저장한다
            # 현재 위치의 다음 인덱스 값이 초과할 경우 앞으로 돌리기
            if i + 1 >= cityCounts:
                insertVal = parents[p1].nodesInPath[0]
            else:
                insertVal = parents[p1].nodesInPath[i + 1]

            table[i].neighborNode[table[i].count] = insertVal
            table[i].count = table[i].count + 1

            if i - 1 < 0:
                insertVal = parents[p1].nodesInPath[cityCounts - 1]
            else:
                insertVal = parents[p1].nodesInPath[i - 1]
            table[i].neighborNode[table[i].count] = insertVal
            table[i].count = table[i].count + 1

        # p2의 이웃 정보를 적용. p1의 것과 중복되지 않도록 검사
        for i in range(0, cityCounts):
            if i + 1 >= cityCounts:
                insertVal = parents[p2].nodesInPath[0]
            else:
                insertVal = parents[p2].nodesInPath[i + 1]

            # 새로 들어가는 이웃의 정보가 중복되지 않는 경우에만 값 투입
            if table[i].neighbor[0] != insertVal and table[i].neighbor[1] != insertVal:
                table[i].neighborNode[table[i].count] = insertVal
                table[i].count = table[i].count + 1

            if i - 1 < 0:
                insertVal = parents[p2].nodesInPath[cityCounts - 1]
            else:
                insertVal = parents[p2].nodesInPath[i - 1]

            # 새로 들어가는 이웃의 정보가 중복되지 않는 경우에만 값 투입
            if table[i].neighbor[0] != insertVal and table[i].neighbor[1] != insertVal:
                table[i].neighborNode[table[i].count] = insertVal
                table[i].count = table[i].count + 1
        # 단일 offspring에 대한 neighbor table 제작 끝

        for insertIndex in range(0, cityCounts):

            insertVal = -1
            insertCount = -1
            tmpCount = -1

            # 지닌 이웃 수 만큼 판단
            for neighborIndex in range(0, table[reference].count):
                t = table[reference].neighborNode[neighborIndex]
                tmpCount = table[t].count

                # refer한 원소가 더 많은 이웃 수를 지니고 있다면
                if insertCount < tmpCount:
                    insertCount = tmpCount
                    insertVal = t

            # 한 이웃 테이블의 정보가 확정되면
            offsprings[current].nodesInPath[insertIndex] = insertVal
            # 반영된 이웃이 중복 고려되지 않도록 count값 파괴
            table[reference].count = -2
    # 이웃 테이블을 토대로 하나의 자식 완성

# return
