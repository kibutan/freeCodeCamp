  function convertToRoman(num) {
  // let num_str = num.toString();
  let roman = "";
  let numStr = num.toString()
  let roman_num = [
      {id:"M",value:1000},
      {id:"D",value:500},
      {id:"C",value:100},
      {id:"L",value:50},
      {id:"X",value:10},
      {id:"V",value:5},
      {id:"I",value:1}
    ];
  //ローマ数字のルール
  let bigger_digit = "";

  //convert
  // console.log(roman_num);
  let i=0
  
  let find = roman_num.find((element) => element.value <= num);
  console.log(num);
  let find_lower = find;
  let find_upper = find;
  // for (let i = 0; i <= numStr.length; i++){
    while(num >= 1){
      find = roman_num.find((element) => element.value <= num);
      // console.log(key);
      if(num.toString()[0] == 4){
        console.log(find.id,"*",1);
        roman += find.id;
        num += find.value;
        // console.log("After",num)
        // find = roman_num.find((element) => element.value <= num);
        // console.log(find.id,"*******",1);
        // roman += find.id;
        // num %= find.value;
      }
      else if(num.toString()[0] == 9){
        find_lower = roman_num.find((element) => element.value <= Math.floor(num/9));
        find_upper = roman_num.find((element) => element.value <= num);
        console.log(find_lower.id);
        roman += find_lower.id;
        // num += find.value/5;
        num += find_lower.value
        find = roman_num.find((element) => element.value <= num);
        // roman += find.id;
        // console.log("After",num,find.value)
      }
      else{
        console.log(find.id,"*",Math.floor(num/find.value));
        for (let i = 0 ; i < Math.floor(num/find.value) ; i++)roman += find.id;
        num %= find.value;
      }
    };
    console.log("-----",roman,"\n");
    return roman;
  }


convertToRoman(36);
