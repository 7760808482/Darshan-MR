// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.


use("coolageDB");
db.student.insertOne({
    name:"Darshan",
    age:20,
    branch:"ALML",
})
db.student.insertMany([
    {name:"Ram",age:21,branch:"ALML"},
    {name:"Shyam",age:22,branch:"ALML"},
])
db.student.find();
db.student.find({name:"Darshan"});
db.student.deleteOne({name:"Ram"});
db.student.drop();
