data(airquality)
head(airquality)
ozone_data<-na.omit(airquality$Ozone)
hist(ozone_data,
     main=-"Histogram of Ozone Levals",
     xlab="Ozone Concentration",
     ylab="Frequency")
hist(ozone_data,
     main="Colored Histogram of Ozone Levels",
     xlab="Ozone Concentration",
     ylab="Frequency",
     col="lightblue",
     border="darkblue")
hist(ozone_data,
     main="Histogram without Axis",
     xlab="Ozone Concentartion",
     ylab="Frequency",
     axes=FALSE,
     col="lightblue")
axis(1)
axis(2)
box()
hist(ozone_data,
     main="Histogram with Modified Axis Limits",
     xlab="Ozone Concentration",
     ylab="Frequency",
     xlim=c(0,200),
     ylim=c(0,40),
     col="orange")
hist(ozone_data,
     probability=TRUE
     main="Histogram with Density Curve",
     xlab="Ozone Concentration",
     col="lightgray",
     border="black")
lines(density(ozone_data),
      col="red",
      lwd=2)



