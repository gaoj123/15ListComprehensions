#Checks to make sure password contains a mixture of upper- and lowercase letters, and at least one number
def checkPass(passw):
    upper=["u" for x in range(0,len(passw)) if passw[x].isupper()==True]
    lower=["l" for x in range(0,len(passw)) if passw[x].islower()==True]
    num=["n" for x in range(0,len(passw)) if unicode(passw[x], 'utf-8').isnumeric()==True]
    return len(upper)>=1 and len(lower)>=1 and len(num)>=1 and len(passw)>0 ##also checks if password is empty string


#print checkPass("FaB1")
#print checkPass("a1")
#print checkPass("FB1")
#print checkPass("1")
#print checkPass("")

def strength(passw):
    stren=1
    upper=["u" for x in range(0,len(passw)) if passw[x].isupper()==True]
    lower=["l" for x in range(0,len(passw)) if passw[x].islower()==True]
    num=["n" for x in range(0,len(passw)) if unicode(passw[x], 'utf-8').isnumeric()==True]
    nonal=["nonAl" for x in range(0,len(passw)) if passw[x]=="." or passw[x]=="?" or passw[x]=="!" or passw[x]=="&" or passw[x]=="#" or passw[x]=="," or passw[x]==";" or passw[x]==":" or passw[x]=="-" or passw[x]=="_" or passw[x]=="*"]
    if len(passw)==0:
        stren-=1
    else:
        if len(upper)>0:
            stren+=2
        if len(lower)>0:
            stren+=2
        if len(num)>0:
            stren+=2
        if len(nonal)>0:
            stren+=3
    return stren

#print strength("%a,B2")
#print strength("%,B2")
#print strength("%aB2")
#print strength("%a2")
#print strength("%abc")
#print strength("%")
#print strength("")
