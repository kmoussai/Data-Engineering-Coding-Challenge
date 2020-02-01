const MongoClient = require('mongodb').MongoClient;



const uri = "mongodb+srv://"
    + process.env.MONGO_USER + ":"
    + process.env.MONGO_PASSWORD + "@"
    + process.env.MONGO_SERVER
    + "?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

module.exports = client;