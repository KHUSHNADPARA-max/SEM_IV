let array=[NaN,0,15,false,-22,' ',undefined,47,null];
alert(array)

function check_nan(nan){
    for(i=0;i<array.length;i++){
        if(typeof(array[i]) === 'number'){
            if(Number.isNaN(array[i]) || array[i] == 0){
                array.shift();
           }
        }
        else if(typeof(array[i]) === 'boolean'){
            array.splice(i,1).shift();
        }
        else if(typeof(array[i]) === 'undefined'){
            array.splice(i,1).shift();

        }
        else if(typeof(array[i]) === 'string'){
            array.splice(i,1).shift();

        }
        else if(array[i] === null){
            array.splice(i,1).shift();

        }   
    }    
}

function shuffle(array){
    var cur_index= array.length,random_index
    while(cur_index != 0 ){
        random_index= Math.floor(Math.random()* cur_index);
        cur_index--;

        var temp = array[cur_index];
        array[cur_index]=array[random_index];
        array[random_index]= temp;
        
    }
}

result = array.filter(check_nan);
shuffle(array);
alert(array)