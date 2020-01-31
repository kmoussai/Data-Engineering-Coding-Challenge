const express = require('express');
const app = express()
const logger = require('morgan')
const bodyParser = require('body-parser')
// const mongoose = require('mongoose');
const searchRoutes = require('./api/routes/Search')




app.use(logger('dev'))
app.use(bodyParser.urlencoded({ extended: false }))

// app.use((request, response, next) => {
//     //Give access to All 
//     response.header("Access-Control-Allow-Origin", "*");
//     response.header(
//         "Access-Control-Allow-Headers",
//         "Origin, X-Requested-With, Content-Type, Accept, Authorization"
//     );
//     if (request.method === 'OPTIONS') {
//         response.header("Access-Controll-Allow-Methods", "GET")
//         return response.status(200).json({});
//     }
// })
app.use('/search', searchRoutes);


app.use((request, response, next) => {
    const error = new Error("Not found");
    error.status = 404;
    next(error);
})

app.use((error, request, response, next) => {
    response.status(error.status || 500);
    response.json({
        error: {
            message: error.message
        }
    });

})




module.exports = app;