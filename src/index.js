const express = require("express");
const hbs = require("hbs");
const path = require("path");

const { collection, hostel, canteen, college } = require(path.join(__dirname, "db.js"));

const {run} = require('./ml.js');

const app = express();
console.log(__dirname);

app.set("view engine", "hbs");
app.use(express.static("public"));
app.use(express.urlencoded());

app.get("/", (req, res) => {
    res.render("login");
})

app.get("/register", (req, res) => {
    res.render("register");
});

app.get("/home", (req, res) => {
    res.render("home");
})

app.get("/admins",(req,res) => {
    res.render('admin.hbs');
})


app.post("/", async (req, res) => {
    //console.log("post recieved")
    const data = {
        name: req.body.email,
        password: req.body.password
    }
    //console.log(data.password);
    var flag = false;
    await collection.findOne({ name: data.name })
        .then((info) => {
            //console.log(info);
            if (info) {
                if (info.password == data.password) {
                    res.redirect("/home");
                }
                else {
                    res.render("login", {
                        errorValue: "Invalid user name or password!!"
                    })
                }
                flag = true;
            }
        })
    if (!flag) {
        res.render("login", {
            errorValue: "Invalid user name or password!!"
        })
    }
})
app.post("/register", async (req, res) => {
    const data = {
        name: req.body.email,
        password: req.body.password
    };
    var flag = false;
    await collection.find({ name: data.name })
        .then((userInfo) => {
            //console.log(userInfo);
            if (userInfo.length != 0) {
                res.render("register", {
                    errorValue: "User already exits..Please login"
                })
                flag = true;
            }
        })
    //console.log("After the error");
    if (!flag) {
        await collection.insertMany(data);
        res.redirect("/home");
    }
    //res.end();
})

app.post("/home", async (req, res) => {
    var category = req.body.category;
    var text = req.body.statement
    var date = new Date();

    //console.log('This is the data' + JSON.stringify(data));
    
    run(text)
    .then(result => {
      //console.log(result);
    data = {
        text : text,
        category : result.slice(0,8),
        date : date
      }
    try{
        if(category == '1'){
            canteen.insertMany(data).then((data) => console.log("canteen data inserted successfully.."));
        }
        else if(category =='2'){
            hostel.insertMany(data).then(data => console.log("hostel data inserted successfully.."));
        }
        else{
            college.insertMany(data).then(data => console.log("College data inserted successfully"));
        }    
    }catch(err){
        console.log('error while inserting data to DB' + err);
    }
    
    })
    .catch(error => {
      console.error(error);
    });
    
    res.render("success");
})


//Adims login and views

app.post('/admins',async (req,res) => {
    var data = req.body;
    //console.log(data);
    if(data.email === 'canteen@nsrit.edu.in'){
        if(data.password === 'c1a2n3t4'){
            const results = await canteen.find();
            const positives = results.filter((element) => {
                return element.category == 'Positive';
            }).map(item => ({
                text : item.text,
                date : new Date(item.date)
            }))
            const negatives = results.filter((element) => {
                return element.category == 'Negative';
            }).map(item => ({
                text : item.text,
                date : item.date
            }))
            //console.log(typeof results[0].date)
            //console.log(negatives[0].date);

            res.render('view.hbs',{positives ,negatives ,categoryName: 'Canteen Grievences Of NSRIT'});
        }
        else{
            res.render('admin.hbs',{errorValue : 'Not an adimin!!'});
        }
    }
    else if(data.email === 'hostel@nsrit.edu.in'){
        if(data.password === 'h1o2s3t4'){
            const results = await hostel.find();
            const positives = results.filter((element) => {
                return element.category == 'Positive';
            }).map(item => ({
                text : item.text,
                date : new Date(item.date)
            }))
            const negatives = results.filter((element) => {
                return element.category == 'Negative';
            }).map(item => ({
                text : item.text,
                date : item.date
            }))
            //console.log(typeof results[0].date)
            //console.log(negatives[0].date);

            res.render('view.hbs',{positives ,negatives ,categoryName: 'Hostel Grievences Of NSRIT'});

        }
        else{
            res.render('admin.hbs',{errorValue : 'Not an adimin!!'});
        }
    }
    else if(data.email === 'college@nsrit.edu.in'){
        if(data.password === 'c1o2l3l4'){
            const results = await college.find();
            const positives = results.filter((element) => {
                return element.category == 'Positive';
            }).map(item => ({
                text : item.text,
                date : new Date(item.date)
            }))
            const negatives = results.filter((element) => {
                return element.category == 'Negative';
            }).map(item => ({
                text : item.text,
                date : item.date
            }))
            //console.log(typeof results[0].date)
            //console.log(negatives[0].date);

            res.render('view.hbs',{positives ,negatives ,categoryName: 'College Mangement Grievences Of NSRIT'});
        }
        else{
            res.render('admin.hbs',{errorValue : 'Not an adimin!!'});
        }
    }
    else{
        res.render('admin.hbs',{errorValue : 'Not an adimin!!'});
    }
})

app.listen(5000, () => console.log("app is listening on port number 5000"));