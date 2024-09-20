name = str(input())
fixSalary = float(input())
saleMouth = float(input())

bonusSale = saleMouth * 0.15
fixSalary += bonusSale
print('TOTAL = R$ ''{:.2f}'.format(fixSalary))