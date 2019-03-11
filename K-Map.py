# CSE 101 - IP HW2
# K-Map Minimization 
# Name:Tanya Sanjay Kumar
# Roll Number:2018109
# Section:A
# Group:05
# Date:16-10-2018
import copy
#matches two characters and replaces the non-matched character with a "-"
def matchingChars(x,y):
        x=str(x)
        y=str(y)
        n=len(x)
        c=0
        for i in range(n):
                if x[i]==y[i]:
                        c+=1
        if c!=n-1:
                return 'False'                  #returns false when two characters have 2 or more non-matched characters
        else:
                a=0
                for i in x:
                        if i==y[a]:
                                a+=1
                        else:
                                if a==n-1:
                                        ans=x[0:a]+"-"
                                else:
                                        ans=x[0:a]+"-"+x[a+1:]
                                        return ans
        return ans

def matchCharno(x,y):                      #returns number of matched characters
        x=str(x)
        y=str(y)
        n=len(x)
        c=0
        for i in range(n):
                if x[i]==y[i]:
                        c+=1
        return c

def matched(x,y):                          #checks if the minterm (whose binary is x) matches with y i.e x is involved in making y term
        n=len(x)
        c=0
        for i in range(n):
                if x[i]==y[i] or y[i]=="-":   #checks if the characters of x and y match or the character in y is '-'
                        c+=1
        if c!=n:
                return 'False'
        else:
                return 'True'
        

def nonMatch(x,y):                         #this function appends those minterms into the list which cannot be further merged by other minterms
        n=len(y)
        for i in y:
                a=y.count(i)
                if a!=1:
                        y.remove(i)
        if y==[]:
                for i in x:
                        y.append(i)
        else:
                for i in x:
                        for j in y:
                                a=matchCharno(i,j)
                                if a==3:
                                        break
                                elif j==y[n-1]:
                                        y.append(i)
                                else:
                                        continue
        return y

def nullList(l):                          #returns the only non-empty list in the given set of lists or False when all lists are empty or two or more are non-empty
        a=0
        l1=[]
        for i in l:
                if len(i)!=0:
                        a+=1
                        l1=list(i)
                        
        if a==1:
                return l1
        else:
                return 'False'
                           
def essential(list1,stringlist):       #from a list of given prime implicants, it returns essential prime implicants
        essen=[]
        while list1!=[]:               #executes the loop till list of prime implicants is not empty
                a=[]
                b=[]
                
                for i in list1:
                        a.extend(i)
                
                for i in a:
                        if a.count(i)==1 and i in stringlist:
                                b.append(i)  #list of those minterms which appear only once in the prime implicant list
                
                list2=copy.deepcopy(list1)
                #if no minterm appears only once, we append the first list in essen list and remove the same list from list2
                if b==[]:                     
                        essen.append(list1[0])
                        list2.remove(list1[0])
                #if few minterms appear only once, the prime implicants containing these minterms are appended in the essen list and removed from list2.
                else:
                        
                        for i in list1:
                                c=0
                                for j in i:
                                        if j in b:
                                                c+=1
                                if c!=0:
                                        essen.append(i)
                                        list2.remove(i)
                                        
                d=[]
                for i in essen:
                        for j in i:
                                d.append(j)  #d is a list of minterms which are already a part of essential prime implicants             
                list1=copy.deepcopy(list2)
                
                
                for i in list2:
                        e=0
                        for j in i:
                                if j in d:
                                        e+=1
                        if e!=0:
                                list1.remove(i) #removing those PI(Prime implicants) whose minterms are a part of d
        return essen


def null(list1):                               #returns if the lists in list1 are all empty or not
        a=0
        for i in list1:
                if len(str(i))!=0:
                        a+=1
        if a==0:
                return 'True'
        else:
                return 'False'


def minFunc(numVar, stringIn):
        
        '''      This python function takes function of maximum of 4 variables as input and gives the corresponding minimized function(s)as the output (minimized using the K-Map
                 methodology), considering the case of Don’t Care conditions.

                 Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm) Output is a string representing the simplified Boolean Expression in SOP form.        '''  
     
        nostr=stringIn.find("()")                                       #the code returns 0 for no input
        if nostr!=-1:
                return "0"
        c=stringIn.find(")")                                           #extracting string and dont care terms from input
        string1=stringIn[1:c+1]
        stringlist=[]
        n1=string1.count(",")
        c=string1.find(",")
        d=string1[0:c]
        string1=string1[c+1:]
        stringlist.append(int(d))
        for i in range(n1-1):
                c=string1.find(",")
                d=string1[0:c]
                stringlist.append(int(d))
                string1=string1[c+1:]
        stringlist.append(int(string1[0:-1]))                                        #stringlist is a list of normal minterms
                                                             
        
        dash=stringIn.find("-")                                                      #'-' used when there is no dont care term
        if dash==-1:
                if stringIn.find("d (")==-1:
                        stringIn=stringIn.replace(") d(",",")
                else:
                        stringIn=stringIn.replace(") d (",",")
        else:
                if stringIn.find("d -")==-1:
                        stringIn=stringIn.replace(" d-","")
                else:
                        stringIn=stringIn.replace(" d -","")
        n=stringIn.count(",")
        x=[]
        a=stringIn.find(",")
        if a!=-1:
                b=stringIn[1:a]
                x.append(b)
                stringIn=stringIn[a+1:]
                for i in range(n-1):
                        a=stringIn.find(",")
                        b=stringIn[0:a]
                        x.append(b)
                        stringIn=stringIn[a+1:]
                x.append(stringIn[0:-1])                                                    #x is a list of all minterms- normal as well as don't care terms
        else:
                x=stringlist                                                               #when there is only one minterm and no don't care terms
        y=[]
        binary={}
        dict1={}
        for i in stringlist:
                i=int(i)
                c=bin(i)
                c=c.replace("0b","")
                length=len(c)
                for j in range(4):
                        if length!=numVar:
                                c="0"+c
                                length+=1
                binary[i]=c                                                        #creates a dictionary of normal terms and their binary representation
                
        for i in x:
                
                i=int(i)
                c=bin(i)
                c=c.replace("0b","")
                length=len(c)
                for j in range(4):
                        if length!=numVar:
                                c="0"+c
                                length+=1
                
                dict1[i]=c                                                         #creates a dictionary of all terms and their binary representation                
                y.append(c)
        dontcare=[]
        for i in x:
                if i not in stringlist:
                        dontcare.append(i)                                          #creates a list of don't care terms

        '''We have separated the normal terms and don't care terms from the given input and also created a dictionary of normal terms and don't care terms with their binary representation.
           Now we will divide these terms on the basis of number of ones that appear in their binary representation.'''
        g0=[]
        g1=[]
        g2=[]
        g3=[]
        g4=[]
        for j in y:
                j=str(j)
                a=j.count("1")           #counts number of 1s
                if a==0:
                        g0.append(j)
                elif a==1:
                        g1.append(j)
                elif a==2:
                        g2.append(j)
                elif a==3:
                        g3.append(j)
                else:
                        g4.append(j)
        '''Now we create lists which store terms formed by merging any two terms from consecutive group.Terms formed by merging terms of g0 and g1 are stored in gr1 , merged terms of g1
         and g2 are stored in gr2 , merged terms of g2 and g3 are stored in gr3 and merged terms of g3 and g4 are stored in gr4'''
        gr1=[]
        gr2=[]
        gr3=[]
        gr4=[]
        nonmatChr=[]
        m=[]
        #merging process 1
        for i in g0:
                for j in g1:
                        t=matchingChars(i,j)                  #returns merged character if possible or else 'False'
                        if t!='False':
                                gr1.append(t)
                                m.append(i)
                                m.append(j)
                                
        for i in g1:
                for j in g2:
                        t=matchingChars(i,j)
                        if t!='False':
                                gr2.append(t)
                                m.append(i)
                                m.append(j)
                                
        if numVar==3 or numVar==4:
                for i in g2:
                        for j in g3:
                                t=matchingChars(i,j)
                                if t!='False':
                                        gr3.append(t)
                                        m.append(i)
                                        m.append(j)
                
        if numVar==4:
                for i in g3:
                        for j in g4:
                                t=matchingChars(i,j)
                                if t!='False':
                                        gr4.append(t)
                                        m.append(i)
                                        m.append(j)
        
        #minterms which could not be merged are appended in nonmatChr.        
        for i in y:
                if i not in m:
                        nonmatChr.append(i)
        m=[]
        #in case no minterm can be merged,the minterms as it is are further carried upon for conversion
        bul=null([gr1,gr2,gr3,gr4])
        if bul=='True':
                
                g0.extend(g1)
                g0.extend(g2)
                g0.extend(g3)
                g0.extend(g4)
                stringOut=g0
        #if all lists except one are empty, the non-empty list is carried upon for further conversion
        elif nullList([gr1,gr2,gr3,gr4])!="False":
                stringOut=nullList([gr1,gr2,gr3,gr4])
        #if more merging is possible, the below command is executed.
        # The above process (for gr1,gr2,gr3 and gr4) are repeated till no more merging is possible or we reach the final state
        else:
                #merging process 2
                grp2=[]
                grp3=[]
                grp4=[]

                for i in gr1:
                        for j in gr2:
                                p=matchingChars(i,j)
                                if p!='False':
                                        grp2.append(p)
                                        m.append(i)
                                        m.append(j)
                                        
                        
                if numVar==3 or numVar==4:
                        for i in gr2:
                                for j in gr3:
                                        p=matchingChars(i,j)
                                        if p!='False':
                                                grp3.append(p)
                                                m.append(i)
                                                m.append(j)
                        
                        
                
                if numVar==4:
                        for i in gr3:
                                for j in gr4:
                                        p=matchingChars(i,j)
                                        if p!='False':
                                                grp4.append(p)
                                                m.append(i)
                                                m.append(j)
                        
                for i in gr1+gr2+gr3+gr4:
                        if i not in m:
                                nonmatChr.append(i)
                m=[]
                bul=null([grp2,grp3,grp4])
                if bul=='True':
                        gr1.extend(gr2)
                        gr1.extend(gr3)
                        gr1.extend(gr4)
                        stringOut=gr1
                
                elif nullList([grp2,grp3,grp4])!='False':
                        stringOut=nullList([grp2,grp3,grp4])
                else:
                        #merging process 3
                        f1=list(grp2)
                        i2=[]
                        i3=[]
                        f2=[]
                        f3=[]
                        if numVar==3 or numVar==4:
                                for i in grp2:
                                        for j in grp3:
                                                q=matchingChars(i,j)
                                                if q!='False':
                                                        i2.append(q)
                                                        m.append(i)
                                                        m.append(j)
                
                                
                                f2=list(i2)
                        if numVar==4:
                                for i in grp3:
                                        for j in grp4:
                                                q=matchingChars(i,j)
                                                if q!='False':
                                                        i3.append(q)
                                                        m.append(i)
                                                        m.append(j)
                                
                                for i in grp2+grp3+grp4:
                                        if i not in m:
                                                nonmatChr.append(i)
                                m=[]

                                for a in i2:
                                        for b in i3:
                                                v=matchingChars(a,b)
                                                if v!='False':
                                                        f3.append(v)
                                                        m.append(a)
                                                        m.append(b)
                                
                                for i in i2+i3:
                                        if i not in m:
                                                nonmatChr.append(i)
                        '''If f1,f2,f3 are null , grp2+grp3+grp4 will be passed on for further processing.
                        If our input, numVar is 2, f2 is the final state. If input is 3, f3 will be final state but if f3 is null, f2 becomes the final state.
                        If our input is 4, f4 will be the final state . If f4 is null, f3 becomes the final state and if f3 is also null, then f2 is the final state.'''
                        bul=null([f1,f2,f3])
                        if bul=='True':
                                grp2.extend(grp3)
                                grp2.extend(grp4)
                                stringOut=grp2
                        
                        elif numVar==2:
                                stringOut=f1
                        elif numVar==3:
                                if f2==[]:
                                        stringOut=f1
                                else:
                                        
                                        stringOut=f2
                        else:
                                if f3==[]:
                                        if f2==[]:
                                                stringOut=f1
                                        else:
                                                stringOut=f2
                                else:
                                        stringOut=f3
        
        
        stringOut.extend(nonmatChr)     #appending non-matched characters
  
        stringOut=list(set(stringOut))  #removing duplicate elements from the list
       
        stringOut.sort(reverse=True)    #re-arranging the list in reverse order.
        m1=[]
        m2=[]
        d1={}
        for i in stringOut:
                for j in binary:
                        a=matched(binary[j],i)
                        if a=="True":
                                m1.append(j)
                                m2.append(j)
                if m1!=[]:              #if m1 is not blank,it is added to a dictionary d1 with the corresponding merged term as the key
                        d1[i]=m1
                m1=[]
        
        ess=essential(list(d1.values()),stringlist)   #returns essential PIs
        stringOut=[]
        for a in d1:
                if d1[a] in ess:
                        stringOut.append(a)           #appending corresponding merged terms 

        ans=[]
        stringOut=list(set(stringOut))
        stringOut.sort(reverse=True)
        
        for i in stringOut:
                
                term=''
                noDash=i.count("-")
                if noDash==len(i):
                        return "1"                   #if the final term consists of only dashes, return 1.
                else:
                        '''chr(119) gives w. Alphabet at first position used is w, then x, y and z.
                           Thus,converting terms into SOP form by using chr function so that it returns w for first position, x for second etc.'''
                        for j in range(numVar):
                        
                                char=i[j]
                        
                                if char=='0':
                                        ch=str(chr(j+119))+"'"
                                
                                elif char=='1':
                                        ch=str(chr(j+119))
                                else:
                                        ch=""
                        
                                term+=ch
                                
                        
                ans.append(term)
                ans.sort()

        answer=''
        for i in ans:
                answer=answer+"+"+i
        stringOut=answer[1:]       #starting from 1 as ans consists of extra '+' in the start.
        #returns the processed answer 
        return stringOut


             


	
