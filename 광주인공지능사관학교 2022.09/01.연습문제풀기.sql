
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
GROUP BY city.name
ORDER BY city.Population DESC 
LIMIT 10; 