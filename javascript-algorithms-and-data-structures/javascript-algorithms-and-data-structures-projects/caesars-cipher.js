function rot13(str) {
  // const alphabet_lower = "abcdefghijklmnopqrstuvwxyz";
  const alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let result = [];
  for (let i = 0; i < str.length ; i++){
    let index = alphabet_upper.indexOf(str[i]);
    console.log(alphabet_upper[index]);
    if(index >= 13)result[i] = alphabet_upper[index - 13]
    else if(index != -1 && index <= 12)result[i] = alphabet_upper[index + 13]
    else result[i] = str[i];
  }
  console.log(...result,result.join(""));
  return result.join("");
}

rot13("SERR PBQR PNZC");
