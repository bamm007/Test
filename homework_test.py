import copy

def countK(moneyInfoList, totalMoney, totalK) :
	copy_totalM = totalMoney
	copy_totalK = totalK
	number = 0
	k = 0

	if totalK == 1 :
		for i in range (1, moneyInfoList[0][1]+1) :
			if copy_totalM == moneyInfoList[0][0]*i :
				number += 1
		return number

	count = []
	for i in range (0, totalK) :
		count.append(0)

	while True :
		# count[1]배열부터 +1씩 늘려가며 가지고 있는 수를 넘었을 경우 다음 count배열의 값을 +1시키고 그 전 배열은 0으로 초기화
		for i in range (1, totalK) :
			if count[i] > moneyInfoList[i][1] :
				if i == totalK-1 :
					return number
				count[i+1] += 1
				k = 1
				continue
			elif k == 1 :
				for j in range(1, i) :
					count[j] = 0
				k = 0
			else :
				break

		copy_totalM = totalMoney
		for i in range (1, totalK) :
			copy_totalM = copy_totalM - moneyInfoList[i][0]*count[i]
		
		if copy_totalM < 0 :
			count[1] += 1
			continue

		for i in range (0, moneyInfoList[0][1]+1) :	
			if copy_totalM == moneyInfoList[0][0] * i :
				number += 1
				break
			elif copy_totalM < moneyInfoList[0][0] * i :
				break

		count[1] += 1


totalMoney = int(input("지폐의 금액 : "))
totalK = int(input("가지수 : "))

moneyInfoList = []
str_moneySize = []
str_moneyCount = []
a=5
for i in range(0, totalK) :
	moneyInfo = input("금액, 개수 : ")
	moneyInfo = [int(i) for i in moneyInfo.split()]
	moneyInfoList.append(moneyInfo)

# 작은수부터 큰 순서대로 정렬(2차원배열)
moneyInfoList.sort()

print(countK(moneyInfoList, totalMoney, totalK))

c = input()



	

