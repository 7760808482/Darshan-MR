item_df<- data.frame(
  itemCode=c(1001,1002,1003,1004,1005),
  itemCategory=c("Electronics","Desktop Supplies","Office Supplies","USB","CD Drive"),
  itemPrice=c(700,300,350,400,800)
)
print("Main data frame:")
print(item_df)
subset_price<-subset(item_df,itemPrice>=350)
print("Items with price>=350:")
print(subset_price)
subset_category<-subset(item_df,itemCategory %in% c("office supplies","desktop suppiles:"))
print("Items from Office Supplies orDesktop Supplies:")
print(subset_category)
item_details<-data.frame(
  itemCode=c(1001,1002,1003,1004,1005),
  ItemQtyonHand=c(50,30,45,60,20),
  ItemReorderLvl=c(10,8,12,15,5)
)
print("Item Details Data frame:")
print(item_details)
merged_df<-merge(item_df,item_details,by="itemCode")
print("Merged data Frame:")
print(merged_df)

