function telephoneCheck(str) {
  let myRegax = /^([1]?[-| ]?\(?(?=[0-9]{3}\))[0-9]{3}(?<=\([0-9]{3})\)?[-| ]?[0-9]{3}[-| ]?[0-9]{4})|([1]?[-| ]?[0-9]{3}[-| ]?[0-9]{3}[-| ]?[0-9]{4})$/
  let result = false;
  // console.log(myRegax.test(str),myRegax.exec(str),myRegax.exec(str)[0] == myRegax.exec(str)["input"])
  // console.log(myRegax.test("555-5555"))
  if(myRegax.test(str)) result = (myRegax.exec(str)[0] == myRegax.exec(str)["input"])
  // console.log(myRegax.exec(str)[0],"=?",myRegax.exec(str)["input"],result);
  return result;
}
// [1]?[-| ]?[0-9]{3}[-| ]?[0-9]{3}[-| ]?[0-9]{4} 数字のみ
//\((?=[0-9]{3}\))?[0-9]{3}(?<=\([0-9]{3})\)?
telephoneCheck("555-555-5555");
