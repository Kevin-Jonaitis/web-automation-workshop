var express = require("express");
var logfmt = require("logfmt");
var app = express();
var mongo = require('mongodb');
var mongoUri = process.env.MONGOLAB_URI ||  process.env.MONGOHQ_URL || 'mongodb://localhost/mydb';
app.use(express.json());       // to support JSON-encoded bodies
app.use(express.urlencoded()); // to support URL-encoded bodies


app.use(logfmt.requestLogger());

app.get('/', function(req, res) {
  res.send('Hello World!');
});

app.post('/signUpCheck', function(req, res) {
  var string = "You tried to sign up!"
  string = string + " username: " + res.body.username + "<br> password: " + res.body.password; 
  res.send(string);

//  mongo.Db.connect(mongoUri, function (err, db) {
//  db.collection('mydocs', function(er, collection) {
//    collection.insert({'mykey': 'myvalue'}, {safe: true}, function(er,rs) {
//    });
//  });
//});
});

app.use(express.static(__dirname + "/public"));

var port = Number(process.env.PORT || 5000);
app.listen(port, function() {
  console.log("Listening on " + port);
});
