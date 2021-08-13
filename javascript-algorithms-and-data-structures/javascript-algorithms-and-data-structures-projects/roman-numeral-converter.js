function convertToRoman(num) {
  // let num_str = num.toString();
  let roman = "";
  let roman_num = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  //ローマ数字のルール
  let bigger_digit = "";
  //でっかい方からにじゅんばんを入Keysれ替える
  roman_num = Object.keys(roman_num).map((k) => ({ key:k, value: roman_num[k]}));//obj->arr
  roman_num.sort((a,b) => b.value - a.value);//sort
  roman_num = Object.assign({},...roman_num.map((item) =>({ [item.key]:item.value,})));//arr->obj

  //convert
  console.log(num);
  for (const key of Object.keys(roman_num)){
    console.log(roman_num[key],roman_num[key].toString()[0],Math.floor(9*roman_num[key]/10));
    if(num >= roman_num[key]){
      if(bigger_digit != ""){
        roman = roman + key + bigger_digit;
        bigger_digit = ""
        num %= roman_num[key]; 
      }
      console.log("num >= *",roman_num[key]);
      let digit = Math.floor(num/roman_num[key]);
      for (let i = 0; i < digit ; i++)roman += key;
      num %= roman_num[key];
      console.log("roman digit",key,digit,roman);
    }else if(roman_num[key] >num){
      console.log("more small",num,(9*roman_num[key])/10);
      if(roman_num[key].toString()[0] == 1 && num >= (9*roman_num[key])/10 ){
        bigger_digit = key;
        num -= roman_num[key] -num;
        }
      else if(roman_num[key].toString()[0] == 5 && num >= roman_num[key]*0.8)bigger_digit = key;
    }
  }console.log("-------------------");
  // console.log(num[0])

  // if(num >= 1000){
  //   console.log("M * ",Math.floor(num/1000));
  //   roman += "M"*Math.floor(num/1000);
  //   num %= 1000;
  return roman;
}
convertToRoman(36);
