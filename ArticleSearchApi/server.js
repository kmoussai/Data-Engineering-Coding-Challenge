http = require('http');

app = require("./app")

const port = process.env.PORT || 3003;

const server = http.createServer(app);

server.listen(port);

