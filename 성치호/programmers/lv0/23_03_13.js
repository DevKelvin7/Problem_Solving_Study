// 프로그래머스 최댓값 만들기(2) https://school.programmers.co.kr/learn/courses/30/lessons/120862

//내풀이

function solution(numbers) {
  let max = numbers[0] * numbers[1];
  
  for(let i = 0; i < numbers.length-1; i++) {
    let first = numbers[i];

    for(let j = i+1; j < numbers.length; j++) {
      let second = numbers[j];

      if (max < first * second) {
        max = first * second;
      }
    }
  }
  return max;
}

// 맥스 정해준 후 이중 for문 돌면서 max값 계속 갱신 값 하나 고정해서 도는식으로 전부 순회하므로 언젠간 max값 나옴



// 다른 사람 풀이
function solution(numbers) {
  numbers.sort((x, y) => x - y);
  return Math.max(numbers[0]*numbers[1], numbers[numbers.length-1]*numbers[numbers.length-2]);
}

//오름차순 정렬 -> 맨 앞 두개가 음수이면서 숫자가 큰경우엔 곱한 값이 가장크므로 1,2번째 요소 곱해주거나 마지막 요소 두개 곱해줌




//문제 : 인덱스 바꾸기  https://school.programmers.co.kr/learn/courses/30/lessons/120895

//내풀이

function solution(my_string, num1, num2) {
  let arr1 =  my_string.split("");
  let indexNum1 = arr1[num1];
  let indexNum2 = arr1[num2];

  arr1[num1] = indexNum2;
  arr1[num2] = indexNum1;

  return arr1.join("");
}

// 문자열 배열로 만든 후 indexNum1, indexNum2 변수를 만든 후 배열의 num1, num2 자리에 바꿔서 대입.

//다른 사람 풀이

function solution(my_string, num1, num2) {
  my_string = my_string.split("");

  [ my_string[num1], my_string[num2] ] = [ my_string[num2], my_string[num1] ];
  
  return my_string.join("");
}

// 배열 구조 분해 할당... -> 매우 간단하여 놀랐음



// 문제 : 배열 회전시키기  https://school.programmers.co.kr/learn/courses/30/lessons/120844

function solution(numbers, direction) {
  if (direction === "right") {
    numbers.unshift(numbers.pop());
  } else {
    numbers.push(numbers.shift());
  }

  return numbers;
}

// 오른쪽방향으로 이동이면 맨뒤에있는 요소를 꺼내서 맨앞으로 넣어줌,
// 왼쪽방향으로 이동 -> 맨 앞에있는 요소를 맨 뒤로 넣어줌
