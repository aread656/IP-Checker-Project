'use strict';
const express = require('express');
const PORT = 82;
const HOST = '0.0.0.0';
var badips = require('./badips');
const app = express();
app.get('/', (req,res) => {
    const validIPChars = "0123456789abcdef.:, "
    res.setHeader('Content-Type', 'application/json');
    var text = req.query.items.trim();
    if (!text){
        res.end(JSON.stringify({
            error: true, input: [], answer: [],
            message: "No inputs were given"
        }))
        return;
    }
    for (let c of text){
        if(!validIPChars.includes(c)){
            res.end(JSON.stringify({
                error:true,input:text, answer:[],
                message:"invalid characters inputted"
            }))
            return;
        }
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