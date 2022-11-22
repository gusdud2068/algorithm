// 이곳에 코드를 작성합니다.
const inputs = [
	[3, 10, 5, [1, 3, 5, 7, 9]],    // 3
	[3, 10, 5, [1, 3, 7, 8, 9]],    // 0
	[5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
	// solution 함수 완성
	let now = 0
	while (true){
		now += K
		if (chargers.includes(now)){
			
		}



	}
}

for (const input of inputs) {
	solution(input[0], input[1], input[2], input[3])
}

