#This is file for OOP 
shoppList = ['apple', 'mango','carrot','banana']
print('I have ', len(shoppList) ,'item to purchase')
print('Those items are:',end='')
for item in shoppList:
    print(item, end=' ')

print('\nI also have to buy  rice.')
shoppList.append('rice')
print('My shop list now is ', shoppList)

print('I will sort my list now')
shoppList.sort()
print('sorted shoplist is ', shoppList)
print('The first item that I will buy is ', shoppList[0])

olditem = shoppList[0]
del shoppList[0]

print('I bought the ', olditem)
print('My shoplist now is ', shoppList)
