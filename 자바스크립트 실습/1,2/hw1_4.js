const nums = [1, 2, 3, 4]

const CubicCal = function (num) {
    return num**3
}
const CubicNum = nums.map(CubicCal)
console.log(CubicNum)