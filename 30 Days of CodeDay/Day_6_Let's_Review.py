# Enter your code here. Read input from STDIN. Print output to STDOUT
cnt = int(input())
for i in range(cnt) : 
    s = input()
    odd_string = ""
    even_string = ""
    for s_index in range(len(s)) :
        if (s_index+1) % 2 ==0 : 
            even_string = even_string + s[s_index]
        else : 
            odd_string = odd_string + s[s_index]
    print(odd_string + ' ' + even_string)
