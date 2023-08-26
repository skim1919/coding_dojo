# drawers = ["documents", "envelopes", "pens"]
# drawers[0] = "tchotchkes"
# drawers[1]= drawers[0]
# # print(drawers)

# words = ["start", "going", "till", "the", "end"]

# # print(words[:4])

# copy_of_words = words[:]
# copy_of_words.append("dojo")
# # print(copy_of_words)
# # print(words)

# my_list = [1, 'Zen', 'hi']
# # print(len(my_list))
# x = my_list.index('hi')
# # print(x)

# #for loop
# bikes = []
# for bike in bikes: #after colon indentation 
# #print(bike) #indentation means inside of for loop
# # print("I want")

# monster = {
#         'make': 'Ducati',
#         'model' : 'Monster 1200R',
#         'engine': {
#             'size' : 1200,
#             'configuration': 'L-Twin',
#             'cylinders' : 2,
#     }
# }
# # print(monster['model'])

# for key in monster:
    # print(key)
    #make: Ducati
    # print(monster[key])
    # print(f'{key} ; {monster[key]}')

# for x in range(10):
#     # print(x)

               #start, end, incremint
# for i in range(10, 0, -1):
#     print(i)

# bikes = ['Yamaha', 'Suzuki', 'Honda', 'Ducati', 'KTM', 'Husky']

# for index in range(len(bikes)):
#     print(bikes[index])

# def add_nums(num1, num2): #parameter
#     sum = num1 + num2
#     return sum

# new_num = add_nums(2, 5) #arguments # return value?
# print(new_num)

# def call_name(name):
#     print( f'Hello {name}')

# # call_name('jimm')

# def create_person_object(name, age, money):
#     person = {
#         'name' : name,
#         'age' : age,
#         'money' : money,
#     }
#     return person
# print(create_person_object('John', 36, 100))
                         
                    #positional argument               
# def create_person_object(name, age=18, money=0):
#     person = {
#         'name' : name,
#         'age' : age,
#         'money' : money,
#     }
#     return person
# print(create_person_object('John'))

# number = 1
# score_list = [90, 45, 70, 60, 55]
# for score in score_list:
#     if score >= 60:
#         result = "합격"
#     else:
#         result = "불합격"
# #     print("{} 학생은 {} 입니다.".format(number, result))
# #     number += 1

# #while
# number = 0
# while number < 13:
#     # print("파이썬이 최고다")
# #     number += 1

# # number = 1
# # while True:
# #     # print(number)
#     number += 1
#     if number > 3:
#         break

# while True:
#     # num1 = int(input("첫 번째 정수 입력 >> "))
#     # num2 = int(input("두 번째 정수 입력 >> "))
#     if num1==0 and num2==0:
#         break
#     print("두 수의 합 : {}".format(num1 + num2))
# print("프로그램이 종료되었습니다.")
    
# for count in range (0,5):
#     print("looping =", count)

# count = 0
# while count < 5:
#     print("looping -", count )
#     count += 1

# y = 3
# while y > 0:
#     print(y)
#     y = y -1
# else:
#     print("Final else statement")


# def number_sum(num1, num2):
#     result = num1 + num2
#     return result
    
# x = number_sum(10, 30)
# print(x)
# print(x)
# print(x)

# def add(a, b):
#     x = a + b
#     print(x)
# add(2, 2)

# def say_hi(name):
#     print("Hi, " + name)
# say_hi('Michael')
# say_hi('Anna')
# # say_hi('Eli')

# def be_cheerful(name='', repeat=2):
#     print(f"good morning {name}\n" * repeat)

# be_cheerful(repeat=2, name="Benny")

# def multiply(num_list, num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

#1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

# person = {"first": "Ada", "last": "Lovelace", "age":42, "is_organ_donor": True}
# capitals = {}
# capitals["svk"] = "Brastislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# print(capitals)

my_dict = {"name": "Noelle", "language": "Python"}
# for each_key in my_dict:
#     # print(each_key)
#     print(my_dict[each_key])

# for key in my_dict.keys():
#     print(key)
# for val in my_dict.values():
#     print(val)
# for key, val in my_dict.items():
#     print(key + " = " + val)
# print(resumes[1]["languages"][0])


# def number_minus(num1, num2):
#     result = num1 - num2
#     return result

# num1 = int(input("첫 번째 정수 입력 >> "))
# num2 = int(input("두 번째 정수 입력 >> "))
# result = number_minus(num1, num2)
# print(result)



# def s_replace(str_test):
#     return str_test.replace("ㅋ", "")

# s = input("문자열 입력 >>")
# result = s_replace(s)
# print(result)


