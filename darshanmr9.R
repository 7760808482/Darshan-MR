monthly_revenue<-c(50000,55000,58000,63000,65000,67000)
monthly_expenses<-c(20000,23500,24000,19000,29500,26000)
savings<-monthly_revenue-monthly_expenses
tax_rate<-0.4
savings_after_tax<-savings*(1-tax_rate)
savings_margin<-round(savings_after_tax/monthly_revenue*100,0)
mean_savings_after_tax<-round(mean(savings_after_tax),2)
best_month<-which.max(savings_after_tax)
worst_month<-which.min(savings_after_tax)
results_vector<-c("Monthly Revenue"=monthly_revenue/1000,
                  "Monthly Expenses"=monthly_expenses/1000,
                  "savings"=round(savings/1000,2),
                  "mean savings after tax"=mean_savings_after_tax,
                  "Best Month"=best_month,
                  "Worst Month"=worst_month)
print(results_vector)
results_data<-data.frame(Month=1:6,
                         Revenue=monthly_revenue,
                         Expenses=monthly_expenses,
                         savings=savings,
                         savings_after_tax=savings_after_tax,
                         savings_margin_margin=savings_margin)
write.csv(results_data,"financial_results.csv",row.names=FALSE)



