
let n = 4

for (let i=0 ; i < n ; i++ ) {
	let a = ''
	for (let j=0; j<n-i-1; j++){
		a += ' '
	}
	for (let k=0; k<2*i+1; k++){
		a += '*'
	}
	console.log(a)
}



