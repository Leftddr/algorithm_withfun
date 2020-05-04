var events = require('events');
var mongoose = require('mongoose');

var eventEmitter = new events.EventEmitter();

var UserSchema;
var UserModel;

var connectHandler = function connected(){
    console.log("Connection Successful");
    connectDB();
    eventEmitter.emit("data_received");
}

eventEmitter.on('connection', connectHandler);

eventEmitter.on('data_received', function(){
    console.log('Data Received');
});

eventEmitter.emit('connection');

function connectDB(){
    var db_url = "mongodb://localhost:27017/test1";

    mongoose.Promise = global.Promise;
    mongoose.connect(db_url);
    database = mongoose.connection;

    database.on('open', function(){
        console.log('connection complete');
    });

    database.on('error', function(){
        console.log('error occur');
    });

    UserSchema = mongoose.Schema({
        id : String,
        name : String,
        password : String
    });

    console.log('definition complete');
    
    UserModel = mongoose.model("users", UserSchema);
    console.log('Model definition complete');

    database.on('disconnected', function(){
        console.log('disconnected, try to reconnect after five seconds');
        setInterval(connectDB, 5000);
    });

    var user = new UserModel({"id" : "qhddnjs1", "name" : "bongwon", "password" : "bongwon"});
    user.save(function(err){
        if(err) {
            console.log('save error occur');
            return;
        }
        console.log('save complete');
    })
}

console.log('Program has ended');