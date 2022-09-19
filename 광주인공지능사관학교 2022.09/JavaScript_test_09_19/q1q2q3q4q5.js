//문제1
/* 두개의 값이 다른 정수를 매개변수로 받아 두수 중 작은 수부터
+3씩 증가시켜서  배열로 만들어 반환하는 함수 ans1(num1, num2) 를 만드세요.
단, 배열에는 매개변수의 큰 수 보다 더 큰 수는 포함될 수 없다. 또한 이 함수를
검증하는 코드, 즉 ans1(2,10)과 ans1(12,3)의 결과를 출력하는 코드도 만드세요 */

//두 수 중 작은 수를 +3 씩 증가  > 배열로 만들어 반환하는 함수
function ans1(num1,num2) {
   array=[];
   if (num1 > num2) {
      for (k=num2; k <= num1; k+=3) {
         array.push(k);
      } 
      return array
   }
   else if (num1 < num2) {
      for (i=num1; i <= num2; i+=3) {
         array.push(i);
      } 
      return array
   }
   else // num1==num2
      console.log("값이 다른 두 정수를 입력하세요")
};

//단  배열에는 매개변수의 큰 수 보다 더 큰 수는 포함될 수 없다

//검증코드  ans1(2,10)과 ans1(12,3)을 출력
console.log("문제1답: ", ans1(2,10), ans1(12,3))
console.log()







// 문제2
/* 991205’와 같이 년월일 6자리 문자를 매개변수로 받아 만 나이를 반환하는 함수 
ans2(birthday)를 만드세요. 또한 이 함수를 검증하는 코드, 즉 ans2(‘991003’)과
ans2(‘000919’)의 결과를 출력하는 코드도 만드세요. */
// 23년부터1923년 22까지는 2022년으로

function ans2(string) {    
   const byear = (string[0]+string[1] > 22) ? parseInt("19"+string[0]+string[1]) : parseInt("20"+string[0]+string[1])  
   const bmonth = parseInt(string[2]+string[3]) 
   const bday = parseInt(string[4]+string[5])
   const cyear = new Date().getFullYear()
   const cmonth = new Date().getMonth() + 1
   const cday = new Date().getDate()
   let age;
   if ((cmonth-bmonth) > 0 ) {age=cyear-byear} //생일지낫으면
   else if ((cmonth-bmonth) == 0 && (cday-bday) >= 0) {age=cyear-byear}
   else if ((cmonth-bmonth) == 0 && (cday-bday) < 0) {age=cyear-byear-1}
   else if ( (cmonth-bmonth) < 0  ) {age=cyear-byear-1} //생일안지낫으면
   return age
}
console.log("문제2답: ", ans2("991003"), ans2("000919"));
console.log()





// 문제3
/* 라인의 수(홀수)를 매개변수로 받아 다음과 같은 모양을 출력하는 함수 ans3(num)을  만드세요.
예를 들어 ans3(5)의 결과는 다음과 같습니다. 
*****  
 ***   
  *  
 *** 
*****    
또한 이 함수를 검증하는 코드 즉, ans3(5)과 ans3(9)의 결과를 출력하세요  */

function ans3(num) {  // num은 줄의 수, 홀수

   if (num % 2 != 0) {
      const numC =  parseInt(num) 
      let nt1='';
      let nt3='';

      for (let k=1; k <= parseInt(numC/2); k++) {  // num은 최대별 개수면서 줄 수
         let t1 =''; 
         for (let t=1; t<=(Math.ceil(numC/2)-k-1);    t++) {t1 += ' '}  //  3 2 1 0   넘뺴기1나누기2부터0까지 -1씩   1 2 3
            for (let t=1; t<=(2*k+1);  t++) {t1 += '*'}   // 1 3 5 7  1부터넘까지지 +2씩              5 3 1   
            for (let t=1; t<=(Math.ceil(numC/2)-k);    t++) {t1 += ' '}    // 3 2 1 0  넘뺴기1나누기2부터0까지  -1씩   1 2 3       
            nt1 += t1 + '\n'    //덮어씌워지지않도록엔터
      }   
      
      for (let k=parseInt(numC/2)+1; k >=1 ; k--) {  // num 줄만큼 줄 반복
         let t3 =''; 
         for (let t=1; t<=(Math.ceil(numC/2)-k);    t++) {t3 += ' '}  //  3 2 1 0   넘뺴기1나누기2부터0까지 -1씩   1 2 3
         for (let t=1; t<=(2*k-1);  t++) {t3 += '*'}   // 1 3 5 7  1부터넘까지지 +2씩              5 3 1   
         for (let t=1; t<=(Math.ceil(numC/2)-k);    t++) {t3 += ' '}    // 3 2 1 0  넘뺴기1나누기2부터0까지  -1씩   1 2 3      
         nt3 += t3 + '\n'    //덮어씌워지지않도록엔터
      }
      return nt3  +  nt1;
   }

   else { 
      console.log("홀수를 입력하세요.")
   }

};

console.log("문제3답:");
console.log()
console.log(ans3(5));
console.log(ans3(9));







// 문제4
/* 매개변수로 물품 가격 여러 개가 문자열 하나로 전해지고, 각 가격은 세미콜론(;) 
으로 구분되어 있습니다. 이 가격을 배열로 만들고, 내림차순으로 정렬하여   반환하는 함수 
ans4(str) 함수를 만드세요.   또한 이 함수를 검증하는 코드로 
ans4("51900;83000;158000;367500;250000;59200;128500;1304000")의 결과를 출력하는 코드도 만드세요. */

function ans4(str) {
   let array = str.split(";") 
   array.sort(function(a, b)  {
      return b - a;
   });
   return array
}

console.log("문제4답: ")
console.log(ans4("51900;83000;158000;367500;250000;59200;128500;1304000"));
console.log()






// 문제5
/* id, 이름, 전화번호, email 을 속성으로 갖고 toString() 메쏘드를 갖는 Member   클래스를 만드세요.   
또한 이 클래스로 james와 maria 객체를 생성하고, toString() 메쏘드를 사용하여   객체안의 속성 
정보를 출력하는 코드도 만드세요. */


class Member {
   constructor (id, name, phonenumber, email) {       // 속성
      this.id = id; 
      this.name = name;
      this.phonenumber = phonenumber;
      this.email = email;
   }
   toString() {                               // 메쏘드
      console.log(` 
아이디: ${this.id}
이름: ${this.name}
전화번호: ${this.phonenumber}
이메일: ${this.email}`);
   }
}

console.log("문제5답: ")
james = new Member("james77", "james", "01024364544", "james77@naver.com");
maria = new Member("maria45", "maria", "01088459932", "maria45@daum.net");
james.toString();
maria.toString();
