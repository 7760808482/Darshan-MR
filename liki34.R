employee <- data.frame( 
  id = 1:20, 
  name = c("Arun","Bala","Chitra","Deepak","Esha", 
           "Farhan","Geetha","Hari","Indu","Jay", 
           "Kiran","Latha","Manoj","Nisha","Om", 
           "Pooja","Qadir","Ravi","Sneha","Tejas"), 
  salary = c(18000,22000,25000,19000,30000, 
             21000,17000,26000,28000,20000, 
             24000,16000,27000,23000,19000, 
             31000,22000,18000,26000,29000), 
  start_date = as.Date(c("2022-01-10","2021-03-15","2020-06-20","2023-02-01", 
                         "2019-11-05","2021-07-18","2022-04-12","2020-09-09", 
                         "2018-08-25","2023-01-05","2021-10-10","2022-05-15", 
                         "2019-03-22","2020-12-01","2023-06-10","2018-07-07", 
                         "2021-02-14","2022-09-19","2020-01-30","2019-05-28")), 
  dept = c("HR","IT","IT","Finance","IT", 
           "IT","HR","IT","IT","Admin", 
           "IT","HR","Finance","IT","Admin", 
           "IT","IT","HR","IT","Finance") 
) 
write.csv(employee, "input.csv", row.names = FALSE) 
cat("input.csv file created successfully\n") 
emp_data <- read.csv("input.csv") 
cat("\nEmployee Data:\n") 
print(emp_data) 
cat("\nTotal Rows:", nrow(emp_data), "\n") 
cat("Total Columns:", ncol(emp_data), "\n") 
max_salary <- max(emp_data$salary) 
cat("\nMaximum Salary:", max_salary, "\n") 
max_salary_emp <- emp_data[emp_data$salary == max_salary, ] 
cat("\nEmployee with Maximum Salary:\n") 
print(max_salary_emp) 
it_employees <- subset(emp_data, dept == "IT") 
cat("\nEmployees working in IT Department:\n") 
print(it_employees) 
it_high_salary <- subset(emp_data, dept == "IT" & salary > 20000) 
write.csv(it_high_salary, "output.csv", row.names = FALSE) 
cat("\nIT Employees with salary > 20000 written to output.csv\n")