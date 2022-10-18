const express = require('express');
const mysql = require('mysql');

const router = express.Router();

let conn = mysql.createConnection({
    host:'127.0.0.1',
    user:'root',
    password:'!ing12924103',
    port:'3306',
    database:'nodejs_db'
})

//express기능중라우터를 사용하겟다선언           
// http://127.0.0.1:5500/public/ex01plus.html
router.get('/plus', function (request, response) {       //  /plus라우터 기능정의및등록
    /* /plus객체가가진 req res
    c 가보낸정보 req에잇다
    res > html 을 c 에게 응답 */
    console.log(request.query.num1);
    console.log(request.query.num2);

    //200은정상응답이란뜻                    html로응답
    response.writeHead(200, { 'Content-Type': 'text/html;charset=utf-8' });
    response.write('<html>')
    response.write('<body>')
    response.write('<h1>응답성공</h1>')
    response.write('결과값' + (parseInt(request.query.num1) + parseInt(request.query.num2)))
    response.write('</body>')
    response.write('</html>')
    response.end();
});

router.get('/cal', (request, response) => {
    console.log('cal router')

    // cal라우터 기능정의및등록
    //1.사용자가입력한값가져오기
    let num1 = request.query.num1;
    let cal = request.query.cal;
    let num2 = request.query.num2;
    console.log(num1 + cal + num2);

    response.writeHead(200, { 'Content-Type': 'text/html;charset=utf-8' });
    response.write('<html>')
    response.write('<body>')
    if (cal == '+') {
        response.write('결과값' + (parseInt(num1) + parseInt(num2)))
    } else if (cal == '-') {
        response.write('결과값' + (parseInt(num1) - parseInt(num2)))
    } else if (cal == '*') {
        response.write('결과값' + (parseInt(num1) * parseInt(num2)))
    } else if (cal == '/') {
        response.write('결과값' + (parseInt(num1) / parseInt(num2)))
    }

    response.write('<h1>응답성공</h1>')
    response.write('결과값' + eval(parseInt(num1) + cal + parseInt(num2)))
    response.write('</body>')
    response.write('</html>')
    response.end();
});

router.post('/Grade', (request, response) => {      // cal라우터 기능정의및등록
    //쿼리는 유알엘로올때 겟 여기선 body로
    // router.get으로 올 땐 겟은 url로 보내는 것 유알엘로 올땐 query로 받아야함

    response.writeHead(200, { 'Content-Type': 'text/html;charset=utf-8' });
    response.write('<html>')
    response.write('<body>')
    response.write('<h1>응답성공1</h1>')
    response.write('이름' + request.body.name+'<br>')
    response.write('자바' + request.body.java+'<br>')
    response.write('웹' + request.body.web+'<br>')
    response.write('아이오티' + request.body.iot+'<br>')
    response.write('안드로이드' + request.body.android+'<br>')
    const name = request.body.name
    const java = request.body.java
    const web = request.body.web
    const iot = request.body.iot
    const android = request.body.android
    let avg = (parseInt(java) + parseInt(web) + parseInt(iot) + parseInt(android)) / 4
    response.write('<h1>응답성공2</h1>')
    response.write('<h1>응답성공3</h1>')
    response.write(name+'님의' +' avg는 ' + avg + '이고 ')
    if (avg <= 75 && avg >= 0 ) {
        response.write('grade는 F')
    } else if (avg <= 79) {
        response.write('grade는 c')
    } else if (avg <= 84) {
        response.write('grade는 b')
    } else if (avg <= 89) {
        response.write('grade는 b+')
    } else if (avg <= 94) {
        response.write('grade는 a')
    } else if (avg <= 100) {
        response.write('grade는 a+')
    }
    response.write('입니다')
    response.write('<h1>응답성공4</h1>')
    response.write('</body>')
    response.write('</html>')
    response.end();
});

router.post('/join', (request, response) => {
    
    response.writeHead(200, { 'Content-Type': 'text/html;charset=utf-8' });
    response.write('<html>')
    response.write('<body>')
    response.write('<h1>응답성공1</h1>')
    response.write('id: ' + request.body.id+'<br>')
    response.write('name: ' + request.body.name+'<br>')
    response.write('email: ' + request.body.email+'<br>')
    response.write('tel: ' + request.body.tel+'<br>')
    response.write('gender: ' + request.body.gender+'<br>')
    response.write('country: ' + request.body.country+'<br>')
    response.write('birth: ' + request.body.birth+'<br>')
    response.write('color: ' + request.body.color+'<br>')
    response.write('hobby: ' + request.body.hobby+'<br>')
    response.write('talk: ' + request.body.talk+'<br>')
    response.write('<h1>응답성공4</h1>')
    response.write('</body>')
    response.write('</html>')
    response.end();
});

router.post('/login', (request, response) => {

    let id = request.body.id
    let pw = request.body.pw

    if (id =='a' && pw =='a'){
        response.redirect('http://127.0.0.1:5500/public/ex05LoginS.html')
        //html파일에서 우클릭 오픈위드라이브서버 로 페스확인
    }else{
        response.redirect('http://127.0.0.1:5500/public/ex05LoginF.html')
    }
});

router.post('/JoinDB', (request, response) => {

    let id = request.body.id
    let pw = request.body.pw
    let nick = request.body.nick;
    
    //let sql="insert into member values('1','1','1')";
//유저가보낸걸넣기 []을추가
    let sql="insert into member values(?,?,?)";
    //      어떤sql? + 실패햇을떄와성공했을떄함수
    conn.query(sql,[id,pw,nick],(err,row)=>{  //[id,pw,nick]는물음표순서대로그대로
if(!err){//에러가없으면
console.log('입력성공'+row)
response.redirect('http://127.0.0.1:5500/public/ex06Main.html');
}else{
    console.log('입력실패'+err)
}
    })


});

router.get('/Delete', (request, response) => {

//회원삭제라우터만들기
//겟방식의딜리트라우터생성
//사용자가입력한아이디가져오기
//아이디값을통해 멤버테이블에잇는아이디값삭제하기
//삭제성공후 main에이치티엠엘로돌아가기
    
    //let sql="insert into member values('1','1','1')";
//유저가보낸걸넣기 []을추가
 //let sql="DELETE FROM member WHERE id=id;"; 여기서 =id는 문자 id로 인식

    let id = request.query.id
    let sql = "DELETE FROM member WHERE id=?";
    //      어떤sql? + 실패햇을떄와성공했을떄함수
    conn.query(sql, [id], (err, row) => {  //[id,pw,nick]는물음표순서대로그대로
        if (row.affectedRows>0) {//에러가없으면
            console.log('명령에성공한수:'+row.affectedRows);
            console.log('삭제성공' + row)
            response.redirect('http://127.0.0.1:5500/public/ex06Main.html');
        } else if (row.affectedRows==0){
            console.log('삭제된값없음')
            response.redirect('http://127.0.0.1:5500/public/ex06Main.html');
        }else {
            console.log('삭제실패' + err)
        }
    })


});



router.get('/Update', (request, response) => {

    //sql업데이트문으로
    let sql = `
    UPDATE member 
    SET pw=?, nick=?
    WHERE id=?;
    `;
    let pw = request.query.pw2
    let nick = request.query.nick2
    let id = request.query.id
    conn.query(sql, [pw,nick,id], (err, row) => {  //[id,pw,nick]는물음표순서대로그대로
        if (!err) {//에러가없으면
            console.log('수정성공' + row)
            response.redirect('http://127.0.0.1:5500/public/ex06Main.html');
        } else {
            console.log('수정실패' + err)
        }
    })


});
//업데이트까지완료










//라우터를외부에서사용할수있게
module.exports = router;
