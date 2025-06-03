# from multiprocessing.connection import address_type
#
# dict= {
#         "name":"roshani",
#         "subject":["math","physics","chemistry"],
#         "city":"pune"
#      }
# print(dict)
# #add value
# dict["surname"]="kinge"
# print (dict)
# #find specific value
# print(dict["name"])
# #empty dict create
# dict2={}
# print (dict2)
# #len of dict
# print(len(dict))
#
# #nested dict create
#
# dict3={
#     "name":"rk",
#     "score":{
#         "math":45,
#          "chem":49,
#         "bio":50
#     },
#     "address":"pune"
# }
# print (dict3)
#
# print(dict3["score"])
# print(dict3["score"]["math"])
#
#

#dictonires methods

dict={
 "name":"roshani",
      "subject":["math","physics","chemistry"],
        "city":"pune"
}
print (dict)
 #print all keys   # here we also perform function in function we write in only in comment part
print(dict.keys())  #here we can do type cast  like  print (List.(dict.keys())
                   # then it give the dict in list

#print all  also values
print(dict.values())  #here we can do type cast  like  print (List.(dict.values())
                      #then it give the dict in list
#print all keys and value
print(dict.items()) #here we can do type cast  like  print (List.(dict.items())
                    # then it give the value in list
print(dict.get("name"))
#here we add new key value paire into dict
dict.update({"surname":"kinge"})
print(dict)

#it gives value as same as but in list



