ch='yes'
while ch=='yes' or 'y':
    Mm=M=int(input("Enter the multiplicant:\t"))
    q=Q=int(input("Enter the multipler:\t"))
    N=2
    A1,Q0,l1,M1,l2,Q1=''.zfill(N),'0',len(format(abs(M),'b')),format(M,'b').zfill(N),\
                       len(format(abs(Q),'b')),format(Q,'b').zfill(N)
    m=max(l1,l2)+1
    if(Mm<0):M1=format(abs(~(int(M1,2)^((1<<m)-1))),'b')
    if(q<0):Q1=format(abs(~(int(Q1,2)^((1<<m)-1))),'b')
    if(M1[0]=='1' or Q1[0]=='1'):
        A1,Q1=A1.zfill(m),Q1.zfill(m)
        N=m
    def rs(x):
        l=len(x)//2
        b=x[0]+format(abs(int(x,2)>>1),'b').zfill(len(x)-1)
        A1,Q1=b[:l],b[l:]
        Q0=x[-1]
        return A1,Q1,Q0
    print('#N#','#A1#','#Q1#','#Q0#',"#REMARKS#")
    print(N,A1,Q1,Q0,"INITIALIZATION")
    while N>0:
        p=~(int(M1,2)^((1<<m)-1))
        if(Q1[-1]=='1' and Q0=='0'):
            A1=format((int(A1,2)+int(format(abs(p),'b'),2)),'b').zfill(m)[-m:]
            print(N,A1,Q1,Q0,"A=A-M")
            x=A1+Q1
            l=len(x)//2
            A1,Q1,Q0=rs(A1+Q1)
            print(N,A1,Q1,Q0,"RIGHT SHIFT")
            N-=1
        elif(Q1[-1]=='0' and Q0=='1'):
            A1=format((int(A1,2)+int(M1,2)),'b').zfill(m)[-m:]
            print(N,A1,Q1,Q0,"A=A+M")
            x=A1+Q1
            l=len(x)//2
            A1,Q1,Q0=rs(A1+Q1)
            print(N,A1,Q1,Q0,"RIGHT SHIFT")
            N-=1
        else:
            x=A1+Q1
            l=len(x)//2
            A1,Q1,Q0=rs(A1+Q1)
            print(N,A1,Q1,Q0,"RIGHT SHIFT")
            N-=1
    r=A1+Q1
    if(Mm<0 and q<0):
        print("result: ",r)
    elif(Mm<0 or q<0):
        l=len(A1+Q1)
        r=format(-abs(~(int(A1+Q1,2)^((1<<l)-1))),'b').zfill(l)
        print("2's compliment of result: ",r)
    print("result=",r,'==',int(r,2))
    ch=input("If you wants to continue ?:\t")
    if(ch!='yes'):
        break
