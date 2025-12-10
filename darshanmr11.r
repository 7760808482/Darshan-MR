factorial_fun<-function(n){
  if(n==0||n==1)
  {
    return(1)
  }
  else  
  {
    return(n*factorial_fun(n-1))
  }
}
num<-4
result<-factorial_fun(num)
cat("factorial of",num,"is",result,"\n")
