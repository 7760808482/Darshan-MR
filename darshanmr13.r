sieve_eratosthenes<-function(n){
  if(n<2){
    return("No prime exit below 2")
  }
  prime<-rep(TRUE,n)
  prime[1]<-FALSE
  for(i in 2:floor(sqrt(n))){
    prime[j]<-FALSE
  }
  }
}
return(which(prime))
}
num<M-50
result<sieve_eratosthenes(num)
cat("PRime number up to ",num,"are:\n")
print(result)