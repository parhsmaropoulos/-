# lista =[[1,4], [7, 10], [3, 5]]
i = 0
lista = []
while i < 10000:
    print('Type start and end of range separated with space')
    mrange = [int(x) for x in input().split()]
    lista.append(mrange)
    if input('Want another range? \n press Y for more \n press N to calculate') == 'Y':
        i += 1
    else:
        break
print(lista)
def sumintervals(lista):
 sum = 0
 lowerbounds = []
 upperbounds = []
 for i in lista:
    # print(i)
    lowerbound1 = []
    upperbound1 = []
    lowerbound = i[0]
    upperbound = i[1]
    lowerbounds.append(lowerbound)
    upperbounds.append(upperbound)
    for j in range(len(lowerbounds)):
        # print(j)
        if j != lista.index(i):
          if lowerbound < lowerbounds[j] and upperbound <= lowerbounds[j]:
              upperbound = upperbound
              lowerbound = lowerbound
              # print('1st')
          elif lowerbound >= upperbounds[j]:
              upperbound = upperbound
              lowerbound = lowerbound
              # print('2nd')
          elif lowerbound < lowerbounds[j] and  lowerbounds[j] <= upperbound <= upperbounds[j]:
              upperbound = lowerbounds[j]
              lowerbound = lowerbound
              # print('3rd')
          elif lowerbound < lowerbounds[j] and upperbound > upperbounds[j]:
              lowerbound1.append(lowerbounds[j])
              upperbound1.append(upperbounds[j])
              # print('4th')
          # elif lowerbounds[j] <= lowerbound <= upperbounds[j] and lowerbounds[j] <= upperbound <= upperbounds[j]:
          #     lowerbound = lowerbound
          #     upperbound = upperbound
          #     print('5th')
          #     continue
          elif lowerbounds[j] <= lowerbound <= upperbounds[j] and upperbound > upperbounds[j]:
              lowerbound = upperbounds[j]
              # print('6th')
          else:
              lowerbound = upperbound
    if 0 != len(lowerbound1):
        sum = sum + (lowerbound1[0] - lowerbound) + (upperbound - upperbound1[0])
    else:
        sum = sum + upperbound - lowerbound
 return sum


print('Sum is:', sumintervals(lista))
