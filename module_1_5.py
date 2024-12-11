immutable_var=([0], "name", True, 34.2)
print (immutable_var)
immutable_var [0] [0] = 10
print (immutable_var)
# сам кортеж изменяться не может, но может хранить в себе какие-либо изменяемые объекты
mutable_list= (["two name", 5, False])
mutable_list [0:3] = "firs name", 3 , True
print (mutable_list)