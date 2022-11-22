function solution(n) {
  let answer = 0;
  
  const dfs = (board, row) => {
    if(n === row) answer++;
    else {
      for(let i = 1; i <= n; i++) {
        board[row+1] = i;	// 다음 라인에 퀸을 배치하고
        // isValid 라는 함수를 통해 해당 위치 퀸이 유효한지 검사
        // 유효하다면 다음위치 계속 탐색
        if(isValid(board, row+1)) dfs(board, row+1);
        
        // 필요하다면 여기서 board[row+1] = 0 으로 
        // 다음 backtraking을 위한 처리가 가능하다.
        // 하지만 위에서 언급했듯 우린 배열을 1차원으로 최적화하기에
        // 이 과정이 필수는 아니다.
      }
    }
  }
  
  const isValid = (board, row) => {
    // 현재라인과 이전 라인을 검사하기 때문에
    // 1 - row 까지 반복하여 검사할 수 있다.
    for(let i = 1; i < row; i++) {
      // 같은 라인에 있는 경우 배치 불가
      if(board[i] === board[row]) return false;
      // 대각 라인에 있는 경우 배치 불가
      if(Math.abs(i-row) === Math.abs(board[i] - board[row])) return false;
    }
    // 위를 모두 통과하면 배치가 가능하다.
    return true;
  }

  for(let i = 1; i <= n; i++) {
    const board = new Array(n+1).fill(0);
    board[1] = i;	// 체스판의 첫번째 세로라인 중 i칸에 퀸을 배치
    console.log(board);
    dfs(board, 1); // 배치가 완료된 체스판과 현재 세로라인인 1을 dfs 함수에 전달
    console.log(board);
  }
  
  return answer;
}

solution(4)


// for(let i = 1; i <= 4; i++) {
//   const asd = new Array(5).fill(0);
//   asd[1] = i;	// 체스판의 첫번째 세로라인 중 i칸에 퀸을 배치
//   console.log(asd);
// }


