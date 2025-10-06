my_vector <- c(1, 2, 3, 4, 5) 
element_from_vector <- my_vector[3] 
print(paste("Element from vector:", element_from_vector)) 
my_matrix <- matrix(1:9, nrow = 3) 
element_from_matrix <- my_matrix[2, 3] 
print(paste("Element from matrix:", element_from_matrix)) 
my_array <- array(1:27, dim = c(3, 3, 3)) 
element_from_array <- my_array[2, 2, 3] 
print(paste("Element from array:", element_from_array))

