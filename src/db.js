const db = require("mongoose");

db.connect("mongodb://127.0.0.1:27017/Users")
    .then(() => console.log("Database connected"))
    .catch((err) => console.log(err));

const loginSchema = new db.Schema({
    name: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    }
})

const hostelSchema = new db.Schema({
    text: {
        type: String,
        required: true
    },
    category : {
        type : String,
        required : true
    },
    date : {
        type: Date,
        required: true
    }
})

const canteenSchema = new db.Schema({
    text: {
        type: String,
        required: true
    },
    category : {
        type : String,
        required : true
    },
    date : {
        type: Date,
        required: true
    }
})

const collegeSchema = new db.Schema({
    text: {
        type: String,
        required: true
    },
    category : {
        type : String,
        required : true
    },
    date : {
        type: Date,
        required: true
    }
})


const collection = new db.model("userData", loginSchema);
const hostel = new db.model("hostelGrievence", hostelSchema);
const canteen = new db.model("canteenGrievence", canteenSchema);
const college = new db.model("collegeGrievence", collegeSchema);

module.exports = { collection, hostel, canteen, college };