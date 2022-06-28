def conditioner(type_of_filter,compare_str,str_name, number_of_words):
    """
    DESCRIPTION:
    Assign "type_of_filter" campare from where ( strart(1), anywhere(2), end(3) ), "str_name" a string, "number_of_words" a integer.

    
    PARAMETERS:               
    <<< compare_str >>> campared string
    <<< type_of_filter >>> ( strart(1), anywhere(2), end(3) )                 
    <<< str_or_list_name >>> This can be variable that is a list or str                         
    <<< number_of_words_at_first >>>
    
    RETURNS:               
    string only

    USE:                      
    k="hello are you there
    h="hello you"
    if(canditioner(1,h,k,2) == true):
        print("true")
    else:
        print("false")
    ---------------------------------------------------------------------------------
    < for > conditioner(1,k,2)
    < out-put > false
    < because > here conditioner(1,h,k,2)="hello are" but the 
    "hello you" has as its first two words different condition not satisfied  
    ---------------------------------------------------------------------------------
    < for > conditioner(1,k,1)
    < out-put > true
    < because > here conditioner(1,k,1)="hello" 
    and "hello you" has its first word same as conditioner hence condition satisfied
    ---------------------------------------------------------------------------------
    < end > same for end too, difference is that it starts comparing the given string to the end of compared string from end of string 
    
    < anywhere > this one checks if words in given string are anywhere in compared string and for anywhere number_of_words can be any number no problem."""
    
    #variables
    h=compare_str 
    we=type_of_filter
    n=number_of_words
    ty=str_name

    #converting to lists
    pom=list(h.split(" "))
    li = list(ty.split(" "))

    #conditions
    if(we==1):
        p=""
        if(len(li)<=len(pom)):
            for i in range(0,n):
                if(i==n-1):
                    p=p+pom[i]
                elif(i<n):
                    p=p+pom[i]+" "
            if(p==ty):
                p="true"
                return p
            else:
                p="false"                               #POM IS WHAT U SPEAK IN MIC-------H 
                return p
        else:                                        #LI IS WHAT U GIVE AS CONDITION-----TY
            pass
    elif(we==2):
        if(2>1):
            count=0
            for i in range(0,len(li)):
                if(li[i] in pom):
                    count+=1
                else:
                    pass
            if(count>0):
                p="true"
                return p
            else:
                p="false"
                return p
        else:
            pass
    elif(we==3):
        if(len(li)<=len(pom)):
            six=len(pom)-len(li)#ex
            if(six>0):
                for i in range(0,six):
                    pom.pop(0)
                if(pom==li):
                    p="true"
                    return p 
                else:
                    p="false"
                    return p
        
            else:
                count=0
                for i in range(0,len(pom)):
                    if(li[i]in pom):
                        count+=1
                if(len(pom)==count):
                    p="true"
                    return p 
                else:
                    p="false"
                    return p
        else:
            pass
def nom(number_str):

    """this will convert any string number like "one" to int number 1.
     So cool right"""
    print(number_str)
    h=type(0)
    loki="%s"%h
    if('int' in loki):
        lom=int(number_str)
        return lom

    else:
        print("else")
        l={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
        if(number_str in l):
            return l[number_str]
        else:
            p=1
            return p
    
