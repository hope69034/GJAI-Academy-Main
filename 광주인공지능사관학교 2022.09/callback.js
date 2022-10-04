/* 콜백이란   다른 코드가 특정코드가 마무리되기 
전에 실행되지 않도록, 즉 비동기처리를 위한 방법이다.
 */

function doHomework(subject, callback) {
   alert(`Starting my ${subject} homework.`);
   callback();
}

/* 펑션에 매스를 넣은 것이 실행 끝난 후 펑션() 즉 콜백함수가 나중에 실행
즉 비동기(순서대로)로 하게끔 콜백함수를 이용한 것 */

doHomework('math', function () {
   alert('Finished my homework');
});
//‘Starting my math homework'
//'Finished my homework'
function doHomework(subject, callback) {
   alert(`Starting my ${subject} homework.`);
   callback();
}
function alertFinished() {
   alert('Finished my homework');
}

/* 두홈워크함수에 매스를 넣은 걸 실행 끝난 후
콜백함수 얼럿피니쉬드를 실행 
즉 위와 같은 결과 */

doHomework('math', alertFinished);
 //‘Starting my math homework'
 //'Finished my homework'