History_file="history.txt"
def show_history():
    file=open(History_file,'r')
    lines=file.readlines()
    if len(lines)==0:
        print('No History Found!.')
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def Clear_History():
    file=open(History_file,'w')
    file.close()
    print('History Cleared.')
    
def Save_To_History(Equation,Result):
    file=open(History_file,'a')
    file.write(Equation+'='+str(Result)+ '\n')
    
def Get_Number():
    num=[]
    n=int(input('No of input.'))
    for i in range(n):
        x=int(input('Enter The No: '))
        if x>0:
            num.append(x)
        else:
            print('Number Should be Greater Than 0')
            break
    Number=num
    return Number

def Calculator():
    Number=Get_Number()
    print("Options: Choose1='+',Choose2='-',Choose3='*',Choose4='/',Choose5='comparision',Choose6='**'")
    z=int(input('Enter from 1 to 6 operations.'))
    if z>6 and z<1:
        print('Wrong Option')
    elif z==1:
        s=''
        p=0
        for i in Number:
            o=int(i)
            p=p+o
            x=i
            s=str(s)+'+'+str(x)
        Equation=s.lstrip('+')
        print(Equation,p,sep='=')
        Save_To_History(Equation,p)
        
    elif z==2:
        s=''
        p=0
        for i in Number:
            o=int(i)
            p=o-p
            x=i
            s=str(s)+'-'+str(x)
        Equation=s.lstrip('-')
        print(Equation,p,sep='=')
        Save_To_History(Equation,p)
        
    elif z==3:
        s=''
        p=1
        for i in Number:
            o=int(i)
            p=p*o
            x=i
            s=str(s)+'*'+str(x)
        Equation=s.lstrip('*')
        print(Equation,p,sep='=')
        Save_To_History(Equation,p)
    
    elif z==4:
        if len(Number)==2:
            if Number[1]==0:
                raise ZeroDivisionError("Number doesn't Divisible By Zero" )
            else:
                s=''
                d=Number[0]
                n=Number[1]
                for i in Number:
                    x=i
                    s=str(s)+'/'+str(x)
                Equation=s.lstrip('/')
                Result=(d/n)
                print(Equation,Result,sep='=')
                Save_To_History(Equation,Result)
        else:
            print('Division Only Support 2 Numbers')
        
    elif z==6:
        if len(Number)==2:
            s=''
            d=Number[0]
            n=Number[1]
            for i in Number:
                x=i
                s=str(s)+'**'+str(x)
            Equation=s.lstrip('**')
            Result=(d**n)
            print(Equation,Result,sep='=')
            Save_To_History(Equation,Result)
        else:
            print('** Only Support 2 Numbers')
            
    elif z==5:
        if len(Number)==2:
            s=''
            d=Number[0]
            n=Number[1]
            if d>n:
                for i in Number:
                    x=i
                    s=str(s)+'>'+str(x)
                    print(s)
                Equation=s.lstrip('>')
                Result=(f'{d} is greater than {n}')
                print(Equation,Result,sep=' ')
                Save_To_History(Equation,Result)
            if d<n:
                for i in Number:
                    x=i
                    s=str(s)+'<'+str(x)
                    print(s)
                Equation=s.lstrip('<')
                Result=(f'{d} is lesser than {n}')
                print(Equation,Result,sep=' ')
                Save_To_History(Equation,Result)
            if d==n:
                for i in Number:
                    x=i
                    s=str(s)+'='+str(x)
                    print(s)
                Equation=s.lstrip('=')
                Result=(f'{d} is equal to {n}')
                print(Equation,Result,sep=' ')
                Save_To_History(Equation,Result)
        else:
            print('Comparision Only Support 2 Numbers')
            
def Main():
    while True:
        print('-----Calculator -----',end='\n')
        print('***** 1-Show History.*****')
        print('***** 2-Clear History.*****')
        print('***** 3-Calculator.*****')
        print('***** 4-Exit.*****')
        g=int(input('Enter The Option No: '))
        if g>4 or g<1:
            raise ValueError('1 to 4 Option Only')
        elif g==1:
            show_history()
        elif g==2:
            Clear_History()
        elif g==3:
            Calculator()
        elif g==4:
            print('Good Bye')
    
Main()