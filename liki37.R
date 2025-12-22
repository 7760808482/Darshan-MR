
data(mtcars) 
cat("First few records of mtcars dataset:\n") 
head(mtcars) 

# a) Total number of observations and variables 

cat("\nTotal Observations (Rows):", nrow(mtcars), "\n") 
cat("Total Variables (Columns):", ncol(mtcars), "\n") 

# b) Car with largest and least horsepower 

max_hp <- max(mtcars$hp) 
min_hp <- min(mtcars$hp) 

cat("\nMaximum Horsepower:", max_hp, "\n") 
cat("Minimum Horsepower:", min_hp, "\n") 

cat("\nCar(s) with Maximum Horsepower:\n") 
print(mtcars[mtcars$hp == max_hp, ]) 

cat("\nCar(s) with Minimum Horsepower:\n") 
print(mtcars[mtcars$hp == min_hp, ]) 

# c) Histogram and Density plots & Skewness 

# Function to compute skewness manually 
skewness <- function(x) { 
  mean((x - mean(x))^3) / sd(x)^3 
} 

# Continuous variables 
cont_vars <- c("mpg","disp","hp","drat","wt","qsec") 

for (var in cont_vars) { 
  hist(mtcars[[var]], 
       probability = TRUE, 
       main = paste("Histogram & Density of", var), 
       xlab = var, 
       col = "lightblue") 
  lines(density(mtcars[[var]]), col = "red", lwd = 2) 
  
  cat("\nSkewness of", var, ":", skewness(mtcars[[var]]), "\n") 
} 

# d) Average hp difference and SD difference 
#     between 3-cylinder and 4-cylinder cars 

hp_3 <- mtcars$hp[mtcars$cyl == 3] 
hp_4 <- mtcars$hp[mtcars$cyl == 4] 

mean_diff <- mean(hp_3) - mean(hp_4) 
sd_diff <- sd(hp_3) - sd(hp_4) 

cat("\nAverage HP of 3-cylinder cars:", mean(hp_3), "\n") 
cat("Average HP of 4-cylinder cars:", mean(hp_4), "\n") 
cat("Difference in Average HP (3 - 4):", mean_diff, "\n") 

cat("\nSD of HP (3-cylinder):", sd(hp_3), "\n") 
cat("SD of HP (4-cylinder):", sd(hp_4), "\n") 
cat("Difference in SD (3 - 4):", sd_diff, "\n") 

# e) Pair of variables with highest Pearson correlation 

corr_matrix <- cor(mtcars) 

# Ignore self-correlations 
corr_matrix[lower.tri(corr_matrix, diag = TRUE)] <- NA 

max_corr <- max(abs(corr_matrix), na.rm = TRUE) 

cat("\nHighest Pearson Correlation Value:", max_corr, "\n") 
cat("Variable Pair with Highest Correlation:\n") 
print(which(abs(corr_matrix) == max_corr, arr.ind = TRUE)) 







