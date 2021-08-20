function checkCashRegister(price, cash, cid) {
  var change = {};
  let cid100 = decimalToInt(cid);
  // console.log(cash)
  let price100 = decimalToIntChange(price)
  let cash100 = decimalToIntChange(cash)
  let change100 = cash100-price100;
  // let cidDecimal = intToDecimal(cid100);
  let sumChange100 = 0
  let sumChange1 = 0

  for (let i = 0 ; i < cid100.length ; i++){
    sumChange1 += cid[i][1]
    sumChange100 += cid100[i][1]
  }

  // console.log("cid100",cid,"\n\n",cid100)
  console.log("sumchg100->",sumChange100," price100->",price100," cash100->",cash100,"change100->",change100,"change1",change,"\n");
  if(change100 > sumChange100){
    change["status"]= "INSUFFICIENT_FUNDS";
    change["change"] = [];
  console.log("INSUFFICIENT_FUNDS",change);
  return change;
  }
  else if(change100 == sumChange100){
    change["status"]= "CLOSED";
    change["change"] = intToDecimal(cid100);
  console.log("CLOSED",change);
  return change;
  }else{
    // console.log("Return Answer",calcChange100(cid100,change100),intToDecimal(calcChange100(cid100,change100)))
    // console.log
    // makeAns(change100)
    change["change"] = intToDecimal(calcChange100(cid100,change100));
    console.log("OPENOPENOPENOPENOPENOPEN",change["change"],(!change["change"].length))
    if (!change["change"].length){change["status"] = "INSUFFICIENT_FUNDS";} 
    else change["status"] = "OPEN";
    console.log("OPEN or INSUFFICIENT_FUNDS",change);
  return change;
  }
  console.log("-----------------------\n");
}
function decimalToIntChange(decimal){
  let int = "";
  let pointIndex = String(decimal).indexOf(".")
  // let pointLength = String(decimal).slice(String(decimal).indexOf(".")).length
  let pointLength = String(decimal).slice(pointIndex).length
  // console.log("converting Change",decimal,pointIndex,pointLength, pointLength-pointIndex)
  if( pointIndex != -1 && pointLength == 2){
      int = String(decimal).replace(".","")
      // for (let i = 0;i < pointLength-1; i++)int += "0";
      int += "0"
    }else if(pointIndex != -1 && pointLength == 3){
      int = String(decimal).replace(".","")
    }else int = String(decimal)+"00"
  // int[i] = String(cid[i][1]).replace(".","")
  // console.log("return int",int)
  let toInt = Number(int);
  return toInt;
}

// function makeAns(cid){
// let toInt=[]
// let int = []
// for (let i = 0 ; i < cid.length ; i++){
//     let pointIndex = String(cid[i][1]).indexOf(".")
//     let pointLength = String(cid[i][1]).slice(String(cid[i][1]).indexOf(".")).length
//     if( pointIndex != -1){
//       // console.log(".??",pointLength-pointIndex)
//         int[i] = String(cid[i][1]).replace(".","")
//         if(pointLength-pointIndex == 1) int[i]+= "0";
//       }else int[i] = String(cid[i][1])+"00"
//     // int[i] = String(cid[i][1]).replace(".","")
//     toInt.push([cid[i][0],Number(int[i])]);
//   };
//   return toInt;
// } 
function calcChange100(cid100,change100){
  const money100 = {"PENNY100":1,"NICKEL100":5,"DIME100":10,"QUARTER100":25,"DOLLAR100":100,"FIVEDOLLAR100":500,"TENDOLLAR100":1000,"TWENTYDOLLAR100":2000,"ONE HUNDREDDOLLAR100":10000};
  let i = Object.keys(money100).length-1;//配列であるcidのためのイテレータ金額の高いものから低いものの順。
  let changeReturn100 =[];
  const amount = {
    "ONE HUNDREDDOLLAR100":cid100[8][1]/money100["ONE HUNDREDDOLLAR100"],
    "TWENTYDOLLAR100":cid100[7][1]/money100["TWENTYDOLLAR100"],
    "TENDOLLAR100":cid100[6][1]/money100["TENDOLLAR100"],
    "FIVEDOLLAR100":cid100[5][1]/money100["FIVEDOLLAR100"],
    "DOLLAR100":cid100[4][1]/money100["DOLLAR100"],
    "QUARTER100":cid100[3][1]/money100["QUARTER100"],
    "DIME100":cid100[2][1]/money100["DIME100"],
    "NICKEL100":cid100[1][1]/money100["NICKEL100"],
    "PENNY100":cid100[0][1]/money100["PENNY100"],
  }
  // console.log("cC100",cid100,amount);
  // console.log("cC100",cid100);
  for (let key of Object.keys(amount)){
    if(change100 <= 0)break;
    if(change100 >= money100[key]){
      let coins = Math.floor(change100/money100[key])
      // console.log("coins",change100,money100[key],"*" ,coins,amount[key],"\ncoin> amout?",coins > amount[key]);
      if (coins <= amount[key]){
        change100 -= money100[key]*coins;
        amount[key] -= coins;
        cid100[i][1] = amount[key] * money100[key]
        changeReturn100.push([cid100[i][0],money100[key]*coins])
      }else if(amount[key] != 0){
        change100 -= money100[key]*amount[key];
        changeReturn100.push([cid100[i][0],money100[key]*amount[key]])
        amount[key] = 0;
        cid100[i][1] = 0
      }
    }
  i--;
  };
  if (change100 == 0)console.log("return change100",changeReturn100);
  else console.log("INSUFFICIENT_FUNDS",change100);
  if (change100 == 0) return changeReturn100;
  else return [];
}

function decimalToInt(cid){
let toInt=[]
let int = []
for (let i = 0 ; i < cid.length ; i++){
    let pointIndex = String(cid[i][1]).indexOf(".")
    let pointLength = String(cid[i][1]).slice(String(cid[i][1]).indexOf(".")).length
    if( pointIndex != -1){
      // console.log(".??",pointLength-pointIndex)
        int[i] = String(cid[i][1]).replace(".","")
        if(pointLength-pointIndex == 1) int[i]+= "0";
      }else int[i] = String(cid[i][1])+"00"
    // int[i] = String(cid[i][1]).replace(".","")
    toInt.push([cid[i][0],Number(int[i])]);
  };
  return toInt;
} 

function intToDecimal(cid_){
let toDecimal=[]
let decimal = []
console.log("input decimal cid",cid_);
for (let i = 0 ; i < cid_.length ; i++){
  let decimalOrNot = false;
    console.log("Covert cid",cid_[i],String(cid_[i][1]).length,i);
    if (cid_[i][0] == "QUARTER" ||
        cid_[i][0] == "DIME"    ||
        cid_[i][0] == "NICKEL"  ||
        cid_[i][0] == "PENNY"){decimalOrNot = true}
    let length = String(cid_[i][1]).length

    if(decimalOrNot && length == 1)decimal[i] = "0.0"+cid_[i][1]
    else if(decimalOrNot && length == 2)decimal[i] = "0."+cid_[i][1]
    else {
      decimal[i] = String(cid_[i][1]).slice(0,-2)+"."+String(cid_[i][1]).slice(-2,)
    }
  toDecimal.push([cid_[i][0],Number(decimal[i])]);
  };
  console.log("int -> Decimal",decimal,toDecimal)
  return toDecimal; 
}


checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
