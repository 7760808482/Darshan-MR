db.user.insertOne({
    name:"Darshan",
    age:20,
    city:"Bengaluru"
})
db.user.find();

db.user.insertMany([
    {name:"Darshan",age:20,city:"Kanakpura"},
    {name:"pavan",age:22,city:"Bengaluru"},
    {name:"pooja",age:18,city:"Bengaluru"},
    {name:"pushpa",age:50,city:"Kanakapura"},
    {name:"krisha",age:56,city:"Kanakapura"},
    {name:"Prathibha",age:37,city:"Bengaluru"},
])
db.user.find({name:"krisha"});
db.user.countDocuments({name:"pooja"});
db.user.updateOne({name:"Darshan"},{$set:{name:"Darshan M R"}});
db.user.replaceOne({name:"hima"},{name:"Darshan",age:19,city:"Bengaluru"});
db.user.find({name:{$eq:"Darshan"}}).limit(1);
db.user.find({name:{$ne:"Darshan"}}).limit(1);
db.user.find({age:{$gte:20}&&{$lte:60}})
db.user.find({age:{$in:[20,22,18]}})
db.user.find({age:{$nin:[20,22,18]}})
db.user.find({name:{$exists:true}})
db.user.insertOne({
    name:"Darshan",
    age:20,
    city:"Bengaluru"
})
db.user.find();

db.user.insertMany([
    {name:"Darshan",age:20,city:"Kanakpura"},
    {name:"pavan",age:22,city:"Bengaluru"},
    {name:"pooja",age:18,city:"Bengaluru"},
    {name:"pushpa",age:50,city:"Kanakapura"},
    {name:"krisha",age:56,city:"Kanakapura"},
    {name:"Prathibha",age:37,city:"Bengaluru"},
])
db.user.find({name:"krisha"});
db.user.countDocuments({name:"pooja"});
db.user.updateOne({name:"Darshan"},{$set:{name:"Darshan M R"}});
db.user.replaceOne({name:"hima"},{name:"Darshan",age:19,city:"Bengaluru"});
db.user.find({name:{$eq:"Darshan"}}).limit(1);
db.user.find({name:{$ne:"Darshan"}}).limit(1);
db.user.find({$expr:{$and:[{$gte:["$age",20]},{$lte:["$age",25]}]}})

 