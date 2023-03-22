x=Math.floor((Math.random()*5) +1)
alert(x)
let guess=prompt("Guess the number : " , 0)

if (guess == x){
    alert(" GOOD WORK ")
}
else {
    alert("Not matched")
}