
/* 연습문제 3문제 풀기*/


USE world; 
SHOW TABLES;
DESC city;
DESC country;
DESC countrylanguage;
SELECT * FROM city;
SELECT * FROM country;
SELECT * FROM countrylanguage; 



3) 대륙별로 국가숫자, GNP의 합, 평균 국가별 GNP는?
SELECT continent, COUNT(*), sum(gnp), avg(gnp) 
FROM country 
GROUP BY continent

/* 대륙별 국가숫자
SELECT continent, COUNT(*) FROM country GROUP BY continent
대륙별  gnp합
SELECT continent, sum(gnp) FROM country GROUP BY continent
평균굮가쥐엔피
SELECT avg(gnp) FROM country
 */



4) 아시아 대륙에서 인구가 가장 많은 도시 10개를 내림차순으로 보여줄 것
(대륙명, 국가명, 도시명, 인구수)

/* 인구가많은도시10ㄱ */
SELECT country.continent as `대륙명`, 
country.Name as `국가명`, 
city.name as `도시명`, 
city.Population as `인구수`  
FROM city 
JOIN country 
ON city.countrycode = country.Code  
WHERE country.continent="asia"
ORDER BY city.Population DESC 
LIMIT 10; 
/* 아시아대륙조건누락 */



5) 전 세계에서 인구가 가장 많은 10개 도시에서 사용하는 공식언어는?
(도시명, 인구수, 언어명)
/* 이스오피셜에 T 가 공식언어임 */
SELECT 
city.name as `도시명`, 
city.Population as `인구수` , 
countrylanguage.language as `언어`,  
country.continent as `대륙명`, 
country.Name as `국가명` 

FROM city 
inner JOIN country 
ON city.countrycode = country.Code
inner JOIN countrylanguage
ON country.Code = countrylanguage.countrycode 

WHERE countrylanguage.isofficial="t"
GROUP BY city.name
ORDER BY city.Population DESC 
LIMIT 10; 

/* 선생님코드 */
SELECT 
city.name as `도시명`, 
city.Population as `인구수` , 
countrylanguage.language as `언어`

FROM city 
JOIN countrylanguage 
ON city.CountryCode=countrylanguage.countrycode 

WHERE countrylanguage.isofficial="t"
GROUP BY city.name
ORDER BY city.Population DESC 
LIMIT 10; 



/* 추가문제 */
/* 국가명과 gnp셀렉트 gnp내림차순 리밋10 */
SELECT 
country.name as `국가명`, 
country.gnp as `gnp`  
FROM city
JOIN country 
ON city.CountryCode=country.code 
group BY country.name
ORDER BY country.gnp DESC 
LIMIT 10; 
