'use strict';

const express = require('express');

const PORT = 82;
const HOST = '0.0.0.0';

var badips = require('./badips');

const app = express();
app.get('/', (req,res) => {

    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*')
    var text = req.query.items;
    if (!text){
        res.end(JSON.stringify({
            error: true, input: [], answer: [],
            message: "No inputs were given"
        }))
    }
    var arrayIPs = text.split(',');
    arrayIPs = arrayIPs.map(IP=>IP.trim())
    var answer = badips.badIPs(arrayIPs);

    var output = {
        error: false,
        input: arrayIPs,
        answer:answer
    }
    res.end(JSON.stringify(output));
});

app.listen(PORT, HOST)