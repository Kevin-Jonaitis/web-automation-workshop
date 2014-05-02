var express = require("express");
var logfmt = require("logfmt");
var app = express();
var mongo = require('mongodb');
var mongoUri = process.env.MONGOLAB_URI ||  process.env.MONGOHQ_URL || 'mongodb://localhost/mydb';
var bodyParser = require('body-parser');
app.use(bodyParser());

app.use(logfmt.requestLogger());

app.get('/', function(req, res) {
  res.send('Hello World!');
});


app.post('/login', function(req, res) {
	var username = req.body.username;
	var password = req.body.password;
	mongo.Db.connect(mongoUri, function(err, db) {

	db.mydocs.find_one({username:password});
	if(result) {
		res.send("You are signed in, " + username);
	}
	});
});

app.post('/signUpCheck', function(req, res) {
  var string = "Welcome, " + " with passowrd " + password;
  var username = String(req.body.username);
  var password = String(req.body.password);
  string = string + req.body.username; 
  res.send(string + " "  + password);

  mongo.Db.connect(mongoUri, function (err, db) {
  db.collection('mydocs', function(er, collection) {
    collection.insert({username: password}, {safe: true}, function(er,rs) {
	console.log("ERROR: " + er);
	console.log("REASON: " + rs);
    });
  });
});

});

app.use(express.static(__dirname + "/public"));

var port = Number(process.env.PORT || 5000);
app.listen(port, function() {
  console.log("Listening on " + port);
});
