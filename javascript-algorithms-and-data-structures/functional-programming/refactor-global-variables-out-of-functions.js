// The global variable
var bookList = ["The Hound of the Baskervilles", "On The Electrodynamics of Moving Bodies", "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae"];

// Change code below this line
function add (list,name) {
  var listInClass = []
  listInClass.push(...list);
  console.log("boooooooooooooooooooooooooooooooook",bookList);


  var book_index = listInClass.indexOf(name);
  if (book_index < 0) {
    console.log("add bookname",name);
    listInClass.push(name);
    console.log("add bookList",listInClass);
  }
  return listInClass;
  
  // Change code above this line
}

// Change code below this line
function remove (list,name) {
  console.log("bxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxk",bookList);
  var listInClass = []
  listInClass.push(...list);
  var book_index = listInClass.indexOf(name);
  if (book_index >= 0) {
    console.log("remove BookList",listInClass[book_index]);
    listInClass.splice(book_index, 1);
    
    return listInClass;

    // Change code above this line
    }
}

var newBookList = add(bookList, 'A Brief History of Time');
var newerBookList = remove(bookList, 'On The Electrodynamics of Moving Bodies');
var newestBookList = remove(add(bookList, 'A Brief History of Time'), 'On The Electrodynamics of Moving Bodies');

console.log(bookList);
