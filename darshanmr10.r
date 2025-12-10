A<-matrix(c(1,2,3,
            4,5,6,
            7,8,9),
          nrow=3,ncol=3,byrow=TRUE)
B<-matrix(c(9,8,7,
            6,5,4,
            3,2,1),
          nrow=3,ncol=3,byrow=TRUE)
cat("Matrix A:\n")
print(A)
cat("Matrix B:\n")
print(B)
cat("\n Transpose of matrix A:\n")
print(t(A))
cat("\n Transpose of matrix B:\n")
print(t(B))
cat("\n Addition of matrix A and B (A+B):\n")
print(A+B)
cat("\n Subtraction of  matrix A and B (A-B):\n")
print(A-B)
cat("\n Matrix Multiplication of A and B (A%*%B):\n")
print(A%*%B)

