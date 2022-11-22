function palindrome(str) {
  const reversed = str.split('').reverse().join('');
  return reversed === str ? true : false;
}


// 출력

console.log(palindrome('level') )
console.log(palindrome('hi') )
