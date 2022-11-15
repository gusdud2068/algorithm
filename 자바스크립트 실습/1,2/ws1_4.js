const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	for (p in p1_choice){
		let p11 = p1_choice[p]
		let p22 = p2_choice[p]

		if (p11 === p22){
			console.log(0)
		} else if ((p11 === 'rock' && p22 === 'scissors') || (p11 === 'paper' && p22 === 'rock') || (p11 === 'scissors' && p22 === 'papaer')){
			console.log(1)
		} else {
			console.log(2)
		}

	}
}

playGame(p1,p2)
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2
