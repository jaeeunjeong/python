//https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
# n개의 이름과 폰 넘버(친구와 번호임)
n = int(input())
phone_book  = dict()

for i in range(0, n) :
    name,number = input().split()
    phone_book[name] = number

for i in range(0, n) :
    name = input()
    if (name in phone_book) :
        info = phone_book[name]
        print(name+"="+info)
    else:
        print("Not found")
#runtime error
