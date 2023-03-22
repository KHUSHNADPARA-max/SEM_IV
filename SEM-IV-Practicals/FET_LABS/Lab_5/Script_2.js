function sal(){
    var employee =[
        {name: "KHUSH",days : "30"},
        {name: "GAUTAM",days : "20"},
        {name: "JAYANT",days : "15"},
        {name: "RUSHI",days : "10"},
        {name: "NITYA",days : "25"},
    ]

    for(var i=0;i<employee.length;i++){
        var emp = employee[i];
        var sal = 10000;
        var totalsal = emp.days*sal;
        alert("The Salary Of " +emp.name +" Is : " +totalsal);
    }
}