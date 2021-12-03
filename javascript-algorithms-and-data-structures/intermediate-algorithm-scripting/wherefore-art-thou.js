function whatIsInAName(collection, source) {
  var arr = [];
  // Only change code below this line
  // for (let i = 0 ; i < collection.length ; i++)console.log(Object.keys(collection[i]))  
  // console.log(Object.keys(source)) 
  let arr_copy = [];
  collection.filter((obj,index,self) => {
    // console.log(obj,index)
    console.log("比較",obj,"-------------",source)
    let badCase = false;
    for (const key of Object.keys(source)){
      if(!(key in obj)){
        console.log("Key in obj?",obj,key,key in obj);
        badCase  = true;
        break;
      }
      if(!(source[key] == obj[key])){
      // console.log(obj,key in obj ,source[key] , obj[key])
        badCase  = true;
        break;
      }
    };
    if(!(badCase)){
      console.log("Hogehoge",obj)
      arr_copy.push(obj)
      let _set = new Set(arr_copy)
      arr = Array.from(_set)
    }
    }); 
  console.log("return",arr)
  console.log("====================")
  // Only change code above this line
  return arr;
}

whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });
