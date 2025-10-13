monthly_revenue<-c(50000,55000,60000,58000,62000,65000,70000,75000,78000,80000,85000,90000)
monthly_expenses<-c(35000,38000,40000,42000,45000,48000,50000,52000,55000,58000,60000,62000)
profit<-monthly_revenue-monthly_expenses
tax_rate<-0.3
profit_after_tax<-profit*(1-tax_rate)
profit_margin<-round(profit_after_tax/monthly_revenue*100,0)
mean_profit_after_tax<-round(mean(profit_after_tax),2)
good_months<-which(profit_after_tax>mean_profit_after_tax)
bad_months<-which(profit_after_tax<mean_profit_after_tax)
best_month<-which.max(profit_after_tax)
worst_month<-which.min(profit_after_tax)
results_vector<-c("Monthly Revenue"=monthly_revenue/1000,
                 "Monthly Expenses"=monthly_expenses/1000,
                 "Profit"=round(profit/1000,2),
                 "profit After tax"=round(profit_after_tax/1000,2),
                 "profit margin"=paste0(profit_margin,"%"),
                 "Mean profit After Tax for the Year"=mean_profit_after_tax,
                 "Good Months"=good_months,
                 "Bad Months"=bad_months,
                 "Best Month"=best_month,
                 "Worst Month"=worst_month)
print(results_vector)
results_data<-data.frame(Month=1:12,
                        Revenue=monthly_revenue,
                        Expenses=monthly_expenses,
                        Profit=profit,
                        profit_after_tax=profit_after_tax,
                        profit_margin=profit_margin)
write.csv(results_data,"financial_results.csv",row.names=FALSE)

