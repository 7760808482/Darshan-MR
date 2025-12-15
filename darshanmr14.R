library(MASS)
data(mammals)

cat("First few records of mammals dataset :\n")
head(mammals)

pearson_corr<-cor(mammals$body,mammals$brain,method="pearson")
spearman_corr<cor(mammals$body,mammals$brain,method="spearman")
cat("\n Pearson Correlation Coeffient",pearson_corr,"\n")
cat("spearman Correlation Coeffient",spearman_corr,"\n")
plot(mammals$body,mammals$brain,
     main="Body Weight vs Brain Weight",
     xlab="Body weight(kg)",
     ylab="brain weight(g)",
     pch=19,
     col="blue")
plot(log(mammals$body),log(mammals$brain),
     main="Log(Body Weight) vs Log(Brain Weight)",
     xlab="Log Body Weight",
     ylab="Log Brain Weight",
     pch=19,
     col="red")
     