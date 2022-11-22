const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

// 3
// 100
// 62
for (eachTC of participantNums){
	for (i in eachTC){
		let flag = false

		for (j in eachTC){
			if (eachTC[i] === eachTC[j]){
				if (i !== j){
				flag = true
				}
			}
		}

		if (flag === false){
			console.log(eachTC[i])
		}
		
	}
}


for (let i = 0; i < participantNums.length; i++) {
    const eachTC = participantNums[i]
    for (let i = 0; i < eachTC.length; i++) {
        let count = eachTC.filter(element => {
            return eachTC[i] === element
        }).length;
        if (count === 1) {
            console.log(eachTC[i])
        }
    }
}
