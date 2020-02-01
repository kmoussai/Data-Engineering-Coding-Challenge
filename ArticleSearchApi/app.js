const express = require('express');
const app = express()
const logger = require('morgan')
const bodyParser = require('body-parser')
const searchRoutes = require('./api/routes/Search')

app.use(logger('dev'))
app.use(bodyParser.urlencoded({ extended: false }))

app.use('/search', searchRoutes);

app.use((request, response, next) => {
    const repoUrl = "https://github.com/kmoussai/Data-Engineering-Coding-Challenge"
    const error = new Error("Not found, More info in GitRepo :" + repoUrl);
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