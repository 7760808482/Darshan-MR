experience_data <- data.frame(
  Experience = c(1,2,3,4,5,6,7,8,9,10),
  Salary = c(18000,22000,26000,30000,35000,
             40000,45000,50000,55000,60000)
)
write.csv(experience_data, "salary_experience_input.csv", row.names = FALSE)
model <- lm(Salary ~ Experience, data = experience_data)
summary(model)
png("salary_vs_experience.png")
plot(experience_data$Experience, experience_data$Salary,
     main = "Salary vs Years of Experience",
     xlab = "Years of Experience",
     ylab = "Salary",
     pch = 19,
     col = "blue")
abline(model, col = "red", lwd = 2)
dev.off()
experience_data$Predicted_Salary <- predict(model)
png("actual_vs_predicted.png")
plot(experience_data$Salary, experience_data$Predicted_Salary,
     main = "Actual vs Predicted Salary",
     xlab = "Actual Salary",
     ylab = "Predicted Salary",
     pch = 19,
     col = "green")
abline(0,1,col="red",lwd=2)
dev.off()
coefficients <- coef(model)
write.csv(coefficients, "model_coefficients.csv")
write.csv(experience_data, "salary_experience_output.csv", row.names = FALSE)
cat("Program executed successfully.\n")