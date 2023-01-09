a={'alan':40,'joo':15,'carl':20,'jio':30}
print("dictionry=",a)
l=list(a.items())
l.sort()
print("asending order",l)
l=list(a.items())
l.sort(reverse=True)
print("decending order",l)