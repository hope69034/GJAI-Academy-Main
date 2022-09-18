/*  q1
random number로 두개의 정수가 주어집니다.(첫번째 값의 범위는 120,
두 번째 값의 범위는 1030이며 첫 번째 값은 두 번째 값보다 작아야 합니다).
첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 배열을
출력하는 프로그램을 만드세요. */

// 두 난수 범위 설정
const number1 =  Math.floor(Math.random() *20) +1 ; // 1~20
////Math.ceil(Math.random()*20)
const number2 =  Math.floor(Math.random() *21) +10; // 10~30
console.log(number1,number2)
 
// 첫번째 값이 두번째보다 4이상 작아야 한다
// 성립할때까지돌린다

//펑션1 선언
function star(number1, number2) {
    let array = [];
    if (number1 <= number2 -4 ) {
        for (let i = number1; i <= number2; i++) {
            array.push(2**i);
        }
        array.splice(1, 1);
        array.splice(array.length-2, 1);
    }
    //답 제출
    console.log()
    console.log(`문제1답: ${array}`)
}

//펑션2 선언 재귀함수 넘버리셋
function star2() {
    const number1 =  Math.floor(Math.random() *20) +1 ; // 1~20
    const number2 =  Math.floor(Math.random() *21) +10; // 10~30
    console.log(number1,number2)
    if (number1 <= number2 -4 ) {star(number1,number2)}
    else {star2()}
}

//메인문
if (number1 <= number2 -4 ) {
    star(number1,number2)
}
else {
    star2()
}


console.log()
console.log("구분선-----------------------------")
console.log()



/* q2
문자열에서 ‘the’의 개수를 출력하는 프로그램을 만드세요. */

const text = "the grown-ups response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the";

// 모든문자가 소문자인 the
// them there their 등은 제외
/* console.log(text) 
console.log(text.split(" ")) */

text.split(" ") //공백기준스플릿한 배열

// the를 찾아서 배열로 만든다
const result = text.split(" ").filter( (the) => {
    return (the === "the");
});
console.log(result)

// result배열에서 원소의 수를 센다

//답 제출
console.log()
console.log(`문제2답: ${result.length}`)


console.log()
console.log("구분선-----------------------------")
console.log()



/* q3
random number로 10보다 크고 100보다 작은 두개의 정수가 주어집니다.
두 숫자의 공약수를 세트 형태로 구하도록 프로그램을 작성하세요. */

//난수범위 10초과~100미만 인 두개의 정수 선언
const num1 = Math.floor(Math.random() *89) +11 ;
const num2 =  Math.floor(Math.random() *89) +11 ;
//floor는 소수점버림
/* console.log(num1)
console.log(num2) */

//두숫자의 약수를 구한다
let input1 = num1;
let divisors1 = [];      
for (let i=1; i<=input1; i++) {
    if (input1 % i == 0) {
        divisors1.push(i);
    }
}
console.log(divisors1);

let input2 = num2;
let divisors2 = [];      
for (let i=1; i<=input2; i++) {
    if (input2 % i == 0) {
        divisors2.push(i);
    }
}
console.log(divisors2);

//두숫자의 공약수를 구한다
const result2 = [];
for (let i of divisors1) {
    for (let j of divisors2) {
        if (i==j){
            result2.push(i)
        }
    }
}

//답 제출
console.log()
console.log(`문제3답: ${result2}`)





console.log()
console.log("구분선-----------------------------")
console.log()


/* q4
다음 배열에서 제조사(manufacturer)와 모델명(model)을 분리해서
별도의 배열을 각각 만드세요.
 */

const cars =
 ["buick skylark 320", 
  "plymouth satellite",
  "amc rebel sst", 
  "ford torino"       ];
 
let manufacturer =[];
let model = [];
for (let i=0; i < cars.length; i++) {
    //원소하나를뽑고 첫공백인덱스미만까지는 매뉴팩처러로 푸시
    manufacturer.push( cars[i].slice(0, cars[i].indexOf(" "))  )  // 이상미만 슬라이스
    //첫공백인덱초과 부터 끝인덱까지 모델로 푸시
    model.push( cars[i].slice( cars[i].indexOf(" ")+1 , cars[i].length  ) )  //슬라이스끝인덱 미만으로 잡아주는거니까 카아이렝스에서 -1안해야함
} //슬라이스함수 시작점만 잡아주고 끝점 생략하면 자동으로 시작부터 끝까지 가기 때문에 cars[i].length 생략가능 

//답 제출
console.log(`문제4답:`)
console.log(manufacturer)
console.log(model)
 

