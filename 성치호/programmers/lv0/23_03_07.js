// 문제 : 문자열 정렬하기(1)
///////////////////////// 1번째 풀이///////////////////

function solution(my_string) {
    let arr1 = my_string.split(""); 
    let answer = []; 
    for (let i = 0; i < arr1.length; i++) { 
        for(let j = 0; j <= 9; j++) {  
            if(Number(arr1[i]) === j) {
                answer.push(Number(arr1[i]));
            }
        }
    }
    return answer.sort(); // 오름차순 정렬
}

// 1. 문자열 배열로 바꿔줌
// 2. 이중 포문으로 0-9사이의 숫자(j) 와 arr1[i]가 같다면 answer 배열에 push
// 3. 오름차순 정렬

/////////////////////////// 2번째 풀이//////////////////

function solution(my_string) {
  return my_string.replace(/[^0-9]/g, "").split("").sort((a,b) => a - b).map(Number);
}

// 1. 숫자가 아닌 모든 문자 제거
// 2. split으로 배열로 변환
// 3. sort로 오름차순 정렬  ( b-a면 내림차순 )
// 4. map으로 배열 전체순환하면서 숫자로 바꿔줌




// 문제 : 대문자와 소문자

function solution(my_string) {
    let answer = "";
    for (let i = 0; i < my_string.length; i++) {
        if (my_string[i] === my_string[i].toUpperCase()) {
             answer += my_string[i].toLowerCase();
        }
        else if (my_string[i] === my_string[i].toLowerCase()) {
             answer += my_string[i].toUpperCase();
        }
    }
    return answer;
}

// 1. for문으로 각 요소가 대문잔지 소문잔지 매칭해서 그 반대걸로 바꿔서 answer에 대입


