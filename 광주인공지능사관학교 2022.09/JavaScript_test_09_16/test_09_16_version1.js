//question1
// jQuery버전
function answer1() {
    $(".input1").click(function(answer1){  //클래스 쇼1 클릭
        const first = parseInt($('#first').val());
        const second = parseInt($('#second').val());
        console.log(first, second);
        let result = [];
        for (let i=first; i<=second; i++) {
            if (i == first+1 || i == second-1)
                continue;
            result.push(Math.pow(2, i));
        }
        //리턴에 3초 딜레이걸기
        setTimeout(function () {
            $('#result1').html(result.join(', '));
        } , 3000);
    });  
};
//question2
// jQuery버전
function answer2() {
    $(".input2").click(function(answer2){ 
        const text = $('#text').val();
        const noPunct = text.replace(/[-',.]/g, '').replace(/\n/g, ' ');    // 구둣점 제거, 줄바꿈은 공백으로 변경
        console.log(noPunct);
        const words = noPunct.split(' ');
        let count = 0;
        for (let word of words) {
        if (word == 'the')
            count++;
        }
        //리턴에 3초 딜레이걸기
        setTimeout(function () {
            $('#result2').html(`the의 개수는 <strong>${count}</strong>개`);
        } , 3000);
    });
};  
//question3
// jQuery버전
function answer3() {
    $(".input3").click( function(answer3) { 
        const num1 =  $('#num1').val() ;
        const num2 = $('#num2').val();
        const divisors1 = [];
        for (let i=1; i<=num1; i++) {
            if (num1 % i == 0)
                divisors1.push(i);          // num1의 약수
        }
        const divisors2 = [];
        for (let i=1; i<=num2; i++) {
            if (num2 % i == 0)
                divisors2.push(i);      // num2의 약수
        }
        const commonDivisors = divisors1.filter(val => divisors2.includes(val));
        //리턴에 3초 딜레이걸기
        setTimeout(function () {
            $('#result3').html(`Set(${commonDivisors.join(', ')})`);
        } , 3000);
    });    
};


//참고
// #아이디선택자 .클래스선택자

//question1
// js버전
/* function answer1() {
    const first = parseInt(document.getElementById('first').value);
    const second = parseInt(document.getElementById('second').value);
    console.log(first, second);
    let result = [];
    for (let i=first; i<=second; i++) {
        if (i == first+1 || i == second-1)
            continue;
        result.push(Math.pow(2, i));
    }
    document.getElementById('result1').innerHTML = result.join(', ');
} */

//question2
// js버전
/* function answer2() {
    const text = document.getElementById('text').value;
    const noPunct = text.replace(/[-',.]/g, '').replace(/\n/g, ' ');    // 구둣점 제거, 줄바꿈은 공백으로 변경
    //console.log(noPunct);
    const words = noPunct.split(' ');
    let count = 0;
    for (let word of words) {
        if (word == 'the')
            count++;
    }
    document.getElementById('result2').innerHTML = `the의 갯수는 <strong>${count}</strong>개`;
}; */

//question3
// js버전
/* function answer3() {
    const num1 = parseInt(document.getElementById('num1').value);
    const num2 = parseInt(document.getElementById('num2').value);
    const divisors1 = [];
    for (let i=1; i<=num1; i++) {
        if (num1 % i == 0)
        divisors1.push(i);          // num1의 약수
    }
    const divisors2 = [];
    for (let i=1; i<=num2; i++) {
        if (num2 % i == 0)
            divisors2.push(i);      // num2의 약수
    }
    const commonDivisors = divisors1.filter(val => divisors2.includes(val));
    document.getElementById('result3').innerHTML = `Set(${commonDivisors.join(', ')})`;
};   */
