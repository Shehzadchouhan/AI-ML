s = set() #empty set
s.add(20) #{20}
s.add(20.0) #{20} because 20 == 20.0
s.add('20') # length of s after these operations?
# {20,,'20'}=3

print(len(s))