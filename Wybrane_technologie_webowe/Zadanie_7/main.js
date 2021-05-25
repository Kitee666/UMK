const http = require("http");
const hello = require('./hello');
const server = http.createServer((req, res) => {
   hello.world(res);
}).listen(80,"127.0.0.1");