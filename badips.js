//100.200.300.400 
//101.201.301.401
//102.202.302.402
//103.203.303.403

function badIPs(ipArray){
    const badIPList = [
    "100.200.300.400",
    "101.201.301.401",
    "102.202.302.402",
    "103.203.303.403"
    ];
    const results = []

    for(let i=0;i<ipArray.length;i++){
        const currentIP = ipArray[i]
        if (badIPList.includes(currentIP)){
            results.push("bad")
        }else if(currentIP == ""){
            results.push("bad")
        }else{
            results.push("good")
        }
    }
    return results
}
module.exports = {
    badIPs
}