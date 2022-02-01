import operator
def most_frequent(string):
    d=dict()
    for i in string:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    new=d
    sorted_d=dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    for key, value in sorted_d.items():
        print(key,"=",value)
inp=input("Please enter a string:")
print(most_frequent(inp))
