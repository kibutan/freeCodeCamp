function palindrome(str) {
  str = str.toLowerCase()
  // console.log(str.match(/[0-9a-zA-Z]{1}/g))
  let str_arr = str.match(/[0-9a-zA-Z]{1}/g)
  // console.log(Math.floor(str_arr.length/2));
  for (let i = 0; i < Math.floor(str_arr.length/2);i++){
    if(!(str_arr[i] == str_arr[str_arr.length-(i+1)])){
    console.log("i and i",str_arr[i],str_arr[str_arr.length-(i+1)])
    return false;
    }
  };
  console.log("passed",str_arr)
  return true;
}



palindrome("eye");
