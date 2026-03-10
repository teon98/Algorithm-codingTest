add = lambda x,y: x+y
print(add(5,4))

num = [1,2,3,4,5]
squares = list(map(lambda x: x**2, num))
print(squares)

"""
map함수
map(적용시킬 함수, 적용할 요소들) 
return -> iterator
"""