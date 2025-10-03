def factorial(n):
    if n==0 or n==1:
        return 1
    else :
        result=1
        for i in range(2,n+1) :
            result*=1
        return result       
def binomial_coffient(N,R):
    return factorial(N)//factorial(R)*factorial(N-R)    
N=int(input('enter the value of N='))  
R=int(input('enter the value of R=')) 
if R>N:
    print('invalid syntax R value must be less than or equal to N')
else:
    binomial_coff=binomial_coffient(N,R)
    print(f"binomial_coffient C({N},{R})=",{binomial_coff})
        
     