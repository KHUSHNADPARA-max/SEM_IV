function perfectnumber(num) {
   
        var nextPerfect = num;
        var sum = 0;
        while (sum !== nextPerfect) {
            nextPerfect++;
            sum = 0;
            for (var i = 1; i < nextPerfect; i++) {
                if (nextPerfect % i === 0) {
                    sum += i;
                }
            }
        }
        alert("The next perfect number is: " + nextPerfect);
    
    
}
  var num = prompt("Enter a number");
  let nearestPerfectNumber = perfectnumber(num);