let config = {};
let loadedConfig = false;
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".button-active").forEach(btn => btn.disabled = true)
  fetch("config.json")
      .then(response => response.json())
      .then(json => {
        console.log("Loaded config:", config);
        console.log("saveURL =", config.saveURL);
        console.log("loadURL =", config.loadURL);
        config = json; loadedConfig = true;
        document.querySelectorAll(".button-active").forEach(btn=>btn.disabled = false);
      })
      .catch(err => {
        alert("Couldn't load config.json")
        console.log("Couldn't load config.json", err)
    })
})

function displayTotalIP(total_ips)
{
    document.getElementById('output-text').value = 'Total IP addresses = ' + total_ips;
}

function displayTotalEmpty(total_empty_ips)
{
    document.getElementById('output-text').value = 'Total empty IP addresses = ' + total_empty_ips;
}

function displayTotalValid(total_valid_ips)
{
    document.getElementById('output-text').value = 'Total valid IP addresses = ' + total_valid_ips;
}

function displayTotalBadGood(total_bad_good){
    document.getElementById('output-text').value = 'Good/bad IP addresses = ' + total_bad_good;
}

function displayIPClassifications(ip_classifications){
    document.getElementById('output-text').value = 'IPClassifications = ' + ip_classifications;
}
function displayIPCountries(country_ips){
        document.getElementById('output-text').value = 'IP Countries = ' + country_ips;

}

function clearText()
{
    document.getElementById('input-text').value = '';
    document.getElementById('output-text').value = '';
}

function getTotalIPs(){
  if (!loadedConfig){
    alert("config.json not yet loaded");return;
  }
  //read items
  let items = document.getElementById('input-text').value
  //alert if none given
  if (!items){
    alert("Please enter some items")
    return;
  }
  // make http req
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState != 4){
      return;
    }
    if(this.status != 200){
      alert("Error: backend service status " + this.status);
      return;
    } 
    //catch incorrect JSON
    try{var j = JSON.parse(this.response)}
    catch (e){
      alert("Invalid JSON returned by backend: " + e)
      return;
    };
    //broader check for json errors, catch-all
    if (j.error){
      alert("JSON returned an error: " + j.error + ". " + j.answer);
      return;
    }
    console.log('test -- ' + j.total_ips);
    let total_ips = j.total_ips;
    displayTotalIP(total_ips);
  };
  //catch-all httpreq error
  xhttp.onerror=function(){
    alert("Backend communication error occurred")
    return;
  }
  xhttp.open("GET",config.totalIPURL+"&items=" + encodeURIComponent(items));
  xhttp.send();
  return;
}

function getTotalEmptyIPs(){
  if (!loadedConfig){
    alert("config.json not yet loaded");return;
  }
  let items = document.getElementById('input-text').value
  if (!items){
    alert("Please enter some items")
    return;
  }
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState != 4){
      return;
    }
    if(this.status != 200){
    alert("Error: backend service status " + this.status);
    return;
    } 
    //catch incorrect JSON
    try{var j = JSON.parse(this.response)}
    catch (e){
      alert("Invalid JSON returned by backend: " + e)
      return;
    };
    //broader check for json errors, catch-all
    if (j.error){
      alert("JSON returned an error: " + j.error + ". " + j.message)
      return;
    }
    console.log('test -- ' + j.total_empty_ips);
    let total_empty_ips = j.total_empty_ips;
    displayTotalEmpty(total_empty_ips);
  }
  xhttp.onerror=function(){
    alert("Backend communication error occurred")
    return;
  }
  xhttp.open("GET",config.totalEmptyIPURL+"&items=" + encodeURIComponent(items));
  xhttp.send();
  return;
}

function getTotalValidIPs(){
  if (!loadedConfig){
    alert("config.json not yet loaded");return;
  }
  //read items
  let items = document.getElementById('input-text').value
  //alert if none given
  if (!items){
    alert("Please enter some items")
    return;
  }
  // make http req
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState != 4){
      return;
    }
    if(this.status != 200){
      alert("Error: backend service status " + this.status);
      return;
    } 
    //catch incorrect JSON
    try{var j = JSON.parse(this.response)}
    catch (e){
      alert("Invalid JSON returned by backend: " + e)
      return;
    };
    //broader check for json errors, catch-all
    if (j.error){
      alert("JSON returned an error: " + j.error)
      return;
    }
    console.log('test -- ' + j.totalValid);
    let total_valid_ips = j.totalValid;
    displayTotalValid(total_valid_ips);
  };
  //catch-all httpreq error
  xhttp.onerror=function(){
    alert("Backend communication error occurred")
    console.error("Backend comm error");
    return;
  }
  xhttp.open("GET",config.totalValidIPURL+"&items=" + encodeURIComponent(items));
  xhttp.send();
  return;
}

function findBadIPs(){
  if (!loadedConfig){
    alert("config.json not yet loaded");return;
  }
    //read items
  let items = document.getElementById('input-text').value
  //alert if none given
  if (!items){
    alert("Please enter some items")
    return;
  }
  // make http req
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState != 4){
      return;
    }
    if(this.status != 200){
      alert("Error: backend service status " + this.status);
      return;
    } 
    //catch incorrect JSON
    try{var j = JSON.parse(this.response)}
    catch (e){
      alert("Invalid JSON returned by backend: " + e)
      return;
    };
    //broader check for json errors, catch-all
    if (j.error){
      alert("JSON returned an error: " + j.error + 
      ". Check for non-hex characters")
      return;
    }
    console.log('test -- ' + j.total_valid_ips);
    let good_bad_array = j.answer;
    displayTotalBadGood(good_bad_array);
  };
  //catch-all httpreq error
  xhttp.onerror=function(){
    alert("Backend communication error occurred")
    return;
  }
  xhttp.open("GET",config.badIPURL+"&items=" + encodeURIComponent(items));
  xhttp.send();
  return;
}

function classifyIPs(){
  if (!loadedConfig){
    alert("config.json not yet loaded");return;
  }
    let items = document.getElementById('input-text').value
    if (!items){
      alert("Please enter some items")
      return;
    }
  // make http req
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState != 4){
      return;
    }
    if(this.status != 200){
      alert("Error: backend service status " + this.status);
      return;
    }
    //catch incorrect JSON
    try{var j = JSON.parse(this.response)}
    catch (e){
      alert("Invalid JSON returned by backend: " + e)
      return;
    };
    //broader check for json errors, catch-all
    if (j.error){
      alert("JSON returned an error: " + j.error + ". Please enter hex characters only")
      return;
    }
    console.log('test -- ' + j.answer);
    let ip_classifications = j.answer;
    displayIPClassifications(ip_classifications);
  };
  //catch-all httpreq error
  xhttp.onerror=function(){
    alert("Backend communication error occurred")
    return;
  }
  xhttp.open("GET",config.classifierIPURL+"&items=" + encodeURIComponent(items));
  xhttp.send();
  return;
}

function findCountry(){
  if (!loadedConfig){
    alert("config.json not yet loaded");return;
  }
  let items = document.getElementById('input-text').value
  if (!items){
    alert("Please enter some items")
    return;
  }
  // make http req
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState != 4){
      return;
    }
    if(this.status != 200){
      alert("Error: backend service status " + this.status);
      return;
    } 
    //catch incorrect JSON
    try{var j = JSON.parse(this.response)}
    catch (e){
      alert("Invalid JSON returned by backend: " + e)
      return;
    };
    //broader check for json errors, catch-all
    if (j.error){
      alert("JSON returned an error: " + j.error + ". Check for non-hex characters")
      return;
    }
    console.log('test -- ' + j.answer);
    let ip_countries = j.answer;
    displayIPCountries(ip_countries);
  };
  //catch-all httpreq error
  xhttp.onerror=function(){
    alert("Backend communication error occurred")
  return;
  }
  xhttp.open("GET",config.countryIPURL+"&items=" + encodeURIComponent(items));
  xhttp.send();
  return;
}
function save(){
  if (!loadedConfig){
    alert("config.json not yet loaded");return;
  }
  let items = document.getElementById("input-text").value;
  if (!items){
    alert("Please enter some items")
    return;
  }
  let xhttp = new XMLHttpRequest()
  xhttp.onreadystatechange = function(){
    if (this.readyState != 4){return;}
    if (this.status != 200){
      alert("Error: backend service error status: " + this.status)
      return;
    }
    let j = JSON.parse(this.responseText);
    alert("IPs saved. ID: " + j.id);
  }
  xhttp.onerror = function() {
      alert("Backend communication error occurred");
  };

  xhttp.open("POST", config.saveURL);
  xhttp.send(items);
  
}
function load(){
  if (!loadedConfig){
    alert("config.json not yet loaded");return;
  }
  let id = prompt("Enter saved IP set's ID")
  if (!id){return;};
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if (this.readyState != 4) {return;}
    if (this.status != 200){
      alert("Error occured, status: " + this.status);
      return;
    }
    let j = JSON.parse(this.responseText)
    document.getElementById("input-text").value = j.ips;
    alert("IPs loaded from ID " + id)
  }
  xhttp.onerror = function(){
    alert("Backend communication error occurred")
  }
  xhttp.open("GET",config.loadURL + "&id=" + encodeURIComponent(id))
  xhttp.send();
}
