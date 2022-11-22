// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log()
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// answer)) const는 변수의 재할당이 안되므로 i++와 같이 값이 변할 때 에러가 발생하게 되므로
// let을 사용해서 재할당이 가능하게 해줘야 한다.

// 2번
for (num of nums) {
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string

// answer)) in을 사용하게 되면 속성이름을통해 반복하게 되므로, 
// of를 사용해서 속성 값을 통해 반복을 하게 하면 된다.