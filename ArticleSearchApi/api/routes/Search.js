const express = require("express")

const router = express.Router()
var client = require('../models/dbClient')

const repoUrl = "https://github.com/kmoussai/Data-Engineering-Coding-Challenge"


router.get('/', (request, response, next) => {

    //limit and toSkip for pagination
    const limit = request.query._limit ? parseInt(request.query._limit) : 20;
    const toSkip = request.query._offset ? parseInt(request.query._offset) : 0;
    const query = request.query.query;
    if (!query) {
        const error = new Error("Query param Not found, More info in GitRepo :" + repoUrl);
        error.status = 400;
        next(error);
        return
    }
    searchQuery = {
        $text: {
            $search: query
        }
    }
    scoreQuery = {
        score: {
            $meta: "textScore"
        }
    }
    client.connect((err, db) => {
        const articles = db.db(process.env.MONGO_DB_NAME)
            .collection(process.env.MONGO_DB_COLLECTION);
        articles.find(searchQuery)
            .project(scoreQuery)
            .skip(toSkip)
            .limit(limit)
            .sort(scoreQuery)
            .toArray((err, result) => {
                if (err) throw err
                finalResult = {
                    resultsize: result.length,
                    result
                }
                response.status(200).json(finalResult)
            })
    })
})

module.exports = router