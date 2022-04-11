import csv

# <extraction 단계>

City_totalMap = []	# 전체 맵 데이터 저장용	# totalMap[0]은 첫 번째 city의 정보
CityInRange_splittedMap = []

GAparent_parents = []		# 각 구역 내 경로		# parent[0]
GAoffsping_offspings = []	# 새로 추출한 경로 후보

index = 0

f = open('TSP.csv', 'r', encoding='utf-8')
reader = csv.reader(f)
for i in reader:
	City_totalMap.append( {i[0], i[1], index} )
	index = index + 1
# 다 읽어서 1천개의 city 데이터를 지닌 totalMap 리스트 완성
f.close()

# 해당 데이터를 나눠야 함 (5 * 5라 가정)
for index in range(0, 1000):	# 0 ~ 999
	if(City_totalMap[index].xPos >= 0 and City_totalMap[index].xPos < 20):
		if(City_totalMap[index].yPos >= 0 and City_totalMap[index].yPos < 20):
			CityInRange_splittedMap[0].nodesInRange.append(index)
			# splittedMap[0].nodesInRange.count++
		# 그냥 이런 식으로 다 나누기

# 범위별로 나눠진 splittedMap[0 ~ 24]를 이용해 각자 계산
# 각 splittedMap에서 vIndex1, vIndex2, 그 사이에 드는 resultCost를 구하면 된다
# 최종 parents 내 가장 우월한 해는 nodesInRange에 저장

# 여기서 이제 branch and bound
# 그리고 heuristic branch and bound