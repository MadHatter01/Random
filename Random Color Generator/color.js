//Random Color Generator Method 1

var red= Math.floor(Math.random() * 256);
var green = Math.floor(Math.random() * 256);
var blue = Math.floor(Math.random() * 256);
var opacity = Math.random().toFixed(1);
colorHex = "rgba("+red+","+green+","+blue+","+opacity+")"; 
document.body.style.backgroundColor = colorHex;
document.getElementById('parentColor').innerText=colorHex;

//Random Color Generator Method 2

var num=(Math.floor(Math.random() * (16777215-0) +0).toString(16));
hex=(num.length < 6 ? '0':'')+num;

var colorBox=document.getElementById('colorBox');
console.log(hex);
document.getElementById('colorLabel').innerText='#'+hex;
colorBox.style.backgroundColor='#'+hex;

