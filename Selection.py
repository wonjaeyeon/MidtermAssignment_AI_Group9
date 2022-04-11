# <Selection 단계>
import Cities
import random
import Preset
# 사용할 부모 쌍 인덱스를 리턴
# offspring의 p1Index, p2Index에 할당하는 건 해당 함수 외부에서 처리

# 옵션에 따라 '품질 비례 룰렛휠' 또는 '순위 기반 선택'으로 가능하다
def parentSelection(parent, bestCost, worstCost, option=1):
    sumOfFitness = 0
    result = []  # 자식에 할당될 부모의 인덱스를 저장할 배열
    # [p1, p2, p1, p2, p1, p2 ...] 이런 방식

    # 해당 함수에서 사용될 적합도(fitness)값을 산출

    # 품질 비례 룰렛 휠에 사용되는 적합도
    if option == 1:
        for i in range(Cities.NUM_OF_PARENTS):
            parent[i].fitness = Preset.getFitness_1(bestCost, worstCost, parent[i].cost, 4, 1)
            sumOfFitness += parent[i].fitness

    # 순위 기반 선택으로 변형된 적합도
    # 이 부분은 잠시 보류. 내가 잘못 이해하는 것일수도 있다

    # 자식수*2 만큼의 부모를 선출
    for i in range(Cities.NUM_OF_OFFSPINGS * 2):
        # 부모 1번의 인덱스
        point = random.random(0, sumOfFitness)
        sum = 0

        # 모든 부모에 대해 fitness 값을 더해가며 바늘의 위치는 찾음
        for j in range(Cities.NUM_OF_PARENTS):
            sum = sum + parent[i].fitness
            if point < sum:
                result.append(j)
    return result

# 순위 기반 선택; 보류
