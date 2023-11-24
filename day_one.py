name='li mengda'
print(name.title())

print(name.upper())
print(name.lower())
#转化大小写

first_name='li'
last_name='mengda'
full_name=f"{first_name} {last_name}"
print(f"Hello,{full_name}")
print(f"Hello,{full_name.upper()}")
#f：在插入变量的值/直接print变量full_name

favorite_language=' python  '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
#.表示方法    ：删除数据空白


url='http://www.python.org'
print(url.removeprefix('http://www.'))

a=0.1+0.3
print(a)

Teammate=['liz','jj','xiang','lk']
print(Teammate)
print(Teammate[0],'\n',Teammate[1].strip())#value的空白无法除去
print(Teammate[1])
print(f"The members of our team are {Teammate[0].title()} {Teammate[1].title()} {Teammate[2].title()} and {Teammate[3].title()}")
T=print(f"The members of our team are {Teammate[0].title()} {Teammate[1].title()} {Teammate[2].title()} and {Teammate[3].title()}")

Guiders=[]
Guiders.append('Han Yiliang')
Guiders.append('Li Yv')
G=print(f"Our guider are {Guiders[0].title()} and {Guiders[1].title()}")

print(f"{T} {G}")

Guider_new=Guiders.pop()
#pop弹出元素并继续使用
print(Guiders)
print(Guider_new)


#record time：2023.11.23

Guiders.append('Song Chaoyue')

for Guider in Guiders:
    print(Guider)
#元素形式

Guider_girl='Song Chaoyue'
Guiders.remove(Guider_girl)
Guiders.append('Li Yv')
print(Guiders)
#列表形式
print(f"\nBecause {Guider_girl} is a girl")

#test git
#test git 2
#test git 3
#test git 3


#record time：2023.11.24
#Today is over，tomorrow will be more good
#exactly 2023.11.24 0:20

name_2='gu junjie'
print(f"{name_2.title()} is on my bed at 23:00")
test=[value**2 for value in range(10)]
print(test)
#列表表达式

#record time：2023.11.24 exactly 23：24
