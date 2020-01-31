const express = require("express")

const router = express.Router()
var MongoClient = require('mongodb').MongoClient;



router.get('/:query', (request, response, next) => {

    const uri = "mongodb+srv://kmoussai:H3pthJCVOMPSgD5I@cluster0-io2fq.mongodb.net?retryWrites=true&w=majority";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    const limit = request.query._limit ? parseInt(request.query._limit) : 15;
    const toSkip = request.query._offset ? parseInt(request.query._offset) : 0;
    query = {
        $text: {
            $search: request.params.query
        }
    }
    scoreQuery = {
        score: {
            $meta: "textScore"
        }
    }
    client.connect((err, db) => {
        const articles = db.db("Challenge").collection("Articles");
        articles.find(query)
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
                db.close()
            })

    })
    // response.status(200).json({
    //     message: "from Search"
    // })
})


module.exports = router