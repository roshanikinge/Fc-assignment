tuple=(1,4,9,16,25,36,49,64,81,100)
x=25 #put number to check similar or not to find it
i=0 #start zero indexing this also use (indexing) in list
while i<len(tuple): #logic here find all length of tuple
    if tuple[i]==x:  #check tuple index ==x number
        print("found at it:",i) #yes print found at
    else:
        print("finding:") #no finding print
    i+=1  #incremnt one by one
