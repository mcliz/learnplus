##字典实践
favorite_language = {'lmd': 'python',
                     'gjj': 'jave',
                     'zx': 'c',
                     'lk': 'python'}
# 访问字典中的值
print(favorite_language['lmd'])
# 遍历所有键值对
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
# 遍历键keys
for name in favorite_language.keys():
    print(name.upper())
# 遍历值values
for language in favorite_language.values():
    print(language.title())


# def add(name_add, language_add):
#     add_fav = {name_add: language_add}
#     return add_fav
# favorite_language[add(name_add='myh')] = [add(language_add='c++')]
# for name, language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")

# favorite_language = add('myh','c++')
# print(favorite_language)
# add_fav = {}
# name_add = input('请输入你要添加的姓名')
# language_add = input('请输入最喜欢的语言')


# add('myh','c++')
# for name,language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")
