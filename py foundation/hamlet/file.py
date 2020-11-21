exwords={"i","my","the","and","of","you","a","in"}
txt=open("C:\\Users\\HP\\Desktop\\hamlet.txt","r").read()
txt=txt.lower()
for ch in "!@#%^&*()_-+=\|":
    txt=txt.replace(ch,"")
words=txt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
for word in exwords:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=1)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:5}".format(word,count))
