# Python---My-Project-with-MIT
#This code lets you find the longest substring in a string sequence

initial=0
final=0
for i in range(0,len(s)-1):
    if s[i]<=s[i+1]:
        initial=i
        while s[i]<=s[i+1]:
            i+=1
            if i>len(s)-2:
                break
        final=i
        break
for j in range(i,len(s)-1):
    if s[j]<=s[j+1]:
        start=j
        while s[j]<=s[j+1]:
            j+=1
            if j>len(s)-2:
                break
        end=j
        if (end-start)>(final-initial):
            final=end
            initial=start
print ('Longest substring in alphabetical order is: ' + s[initial:final+1])
        
