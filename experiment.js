db = db.getSiblingDB("company");

if (!db.getCollectionNames().includes("employees")) {
    db.createCollection("employees");
}

db.employees.deleteMany({});

db.employees.insertMany([
    {
        emp_id: 101,
        name: "Alice",
        department: "HR",
        salary: 50000
    },
    {
        emp_id: 102,
        name: "Bob",
        department: "IT",
        salary: 60000
    },
    {
        emp_id: 103,
        name: "Charlie",
        department: "Finance",
        salary: 55000
    }
]);

print("\n--- CREATE: All inserted employees ---");
db.employees.find().forEach(printjson);

print("\n--- READ: IT department employees ---");
db.employees.find({ department: "IT" }).forEach(printjson);

print("\n--- READ: Employee names and salaries ---");
db.employees.find(
    {},
    { _id: 0, name: 1, salary: 1 }
).forEach(printjson);

db.employees.updateOne(
    { emp_id: 103 },
    { $set: { salary: 58000 } }
);

db.employees.updateMany(
    { department: "IT" },
    { $inc: { salary: 2000 } }
);

print("\n--- UPDATE: Employees after salary changes ---");
db.employees.find().forEach(printjson);

db.employees.deleteOne({ emp_id: 101 });

db.employees.deleteMany({ department: "HR" });

print("\n--- DELETE: Remaining employees ---");
db.employees.find().forEach(printjson);

print("\nExperiment completed successfully.");
