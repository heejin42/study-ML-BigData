# SQL
### SQL
SQL은 structured query language(구조적 쿼리 언어)로 관계형 데이터베이스에 정보를 저장하고 처리하는 프로그래밍 언어를 말한다. 관계형 데이터베이스는 정보를 테이블(표 형식)으로 저장하며 행과 열은 다양한 데이터 속성과 값의 관계를 나타낸다.

### SQL 시스템 구성요소
- SQL 테이블: 행과 열로 구성된 데이터베이스 테이블
- SQL 문: 관계형 데이터베이스 관리 시스템에서 이해하는 유효한 명령어
- 저장 프로시저: 저장 프로시저는 관계형 데이터베이스에 저장된 하나 이상의 SQL 문 모음이다. 소프트웨어 개발자는 저장 프로시저를 사용해서 효율성과 성능을 개선한다. 

### SQL 프로세스
- 구문 분석기: SQL 문의 단어들을 토큰화하거나 바꾼 후, 여러 사항을 확인한다. SQL 문이 쿼리 문의 정확성을 보장하는지 SQL 규칙 준수 여부를 확인하고 세미콜론으로 끝나는지 확인한다. 더불어 쿼리를 실행하는 사용자가 해당 데이터를 조작하는 데 필요한 권한이 있는지도 검증한다. 이 단계에서 문제가 발견되면 쿼리를 실행하지 않고 구문 분석기가 오류를 반환한다.
- 관계형 엔진(쿼리 프로세서): 가장 효과적인 방법으로 데이터를 조작하기 위한 (검색,쓰기,업데이트 등의) 계획을 만든다. 그런 다음, 바이트 코드라는 sql 중간 수준 표현으로 계획을 다시 작성한다. 
- 스토리지 엔진(데이터베이스 엔진): 바이트 코드를 처리함으로써 의도한 sql 문을 실행한다. 

### SQL 명령어
- DDL (Data Definition Language, 정의어)   
데이터베이스의 구조를 정의,수정,삭제하는 언어 (예 - alter, create, drop)   
- DML (Data Manipulation Language, 조작어)
데이터베이스 내의 자료를 검색하고 삽입하고 갱신하는 언어 (예 - select, insert, update, delete)
- DCL (Data Control Language, 제어어)
데이터에 대해 무결성을 유지하고 병행 수행을 제어하며 보호와 관리를 위한 언어 (예 - commit, rollback, grant, revoke)

## 기본 문법 
### SELECT문
```sql
SELECT [ALL┃DISTINCT] 속성이름(들)
[FROM 테이블이름(들)]
[WHERE 검색조건(들)] 
/* =, <>, <, <=, >, >=, BETWEEN AND, IN, NOT IN, LIKE '', IS NULL, IS NOT NULL, AND, OR, NOT   
LIKE 조건은 문자열에만 사용 가능, %(0개 이상 문자열), _(1개문자), [^조건], [조건]
*/

[GROUP BY 속성이름]
[HAVING 검색조건(들)]
[ORDER BY 속성이름 [ASC┃DESC]]
```

### 집계 함수
특정 속성 값을 통계적으로 계산한 결과를 검색한다. 널인 속성 값은 제외, SELECT 절이나 HAVING 절에서만 사용 가능하다.
- SUM : 속성 값의 합계 계산
- AVG : 속성 값의 평균 계산
- COUNT : 속성 값의 개수 계산
- MAX : 속성 값의 최댓값
- MIN : 속성 값의 최솟값

[예시] 가격이 8,000원 이상인 도서를 구매한 고객에 대하여 고객별 주문 도서의 총 수량을 구하시오. 단, 두 권 이상 구매한 고객만 구한다.
```sql
SELECT custid, COUNT(*) AS 도서수량
FROM Orders
WHERE saleprice >= 8000
GROUP BY custid
HAVING count(*) >= 2;
```

### CREATE TABLE
테이블 구성, 속성과 속성에 관한 제약 정의, 기본키 및 외래키를 정의한다.


### ALTER TABLE
```sql
ALTER TABLE 테이블이름
    [ADD 속성이름 데이터타입]
    [DROP COLUMN 속성이름]
    [MODIFY 속성이름 데이터타입]
    [MODIFY 속성이름 [NULL┃NOT NULL]]
    [ADD PRIMARY KEY(속성이름)]
    [[ADD┃DROP] 제약이름]
```

### DROP TABLE
DROP TABLE 문은 테이블을 삭제하는 명령이다. DROP 문은 테이블의 구조와 데이터를 모두 삭제하며 데이터만 삭제하려면 DELETE 문을 사용해야 한다.

### INSERT
테이블에 새로운 튜플을 삽입하는 명령으로 INTO 테이블(속성) VALUES (속성값들)의 구문을 사용한다.
[예시]
```sql 
INSERT INTO Book(bookid, bookname, publisher, price)
VALUES (11, '스포츠 의학', '한솔의학서적', 90000);
```

### UPDATE
테이블에 저장된 투플에서 특정 속성의 값을 수정하는 명령으로 SET 키워드 다음에 속성 값을 어떻게 수정할지 지정한다. 일반적으로 WHERE 절에 제시된 조건을 만족하는 투플에 대해서만 속성 값을 수정하고 WHERE 절을 생략하면 테이블에 존재하는 모든 투플을 대상으로 수정한다.

### DELETE
테이블에 있는 기존 튜플을 삭제하는 명령 WHERE 절에 제시한 조건을 만족하는 튜플만 삭제하며 만약 WHERE 절을 생략하면 테이블에 존재하는 모든 튜플을 삭제해서 빈 테이블이 된다.

-----------------------------------------

# MySQL
MySQL은 Oracle에서 제공하는 오픈 소스 관계형 데이터베이스 관리 시스템으로, SQL 쿼리를 사용하는 관계형 데이터베이스 프로그램이다. SQL 명령은 국제 표준에 의해 정의되지만 MySQL 소프트웨어는 지속적인 업그레이드 및 개선을 거친다.
   

# PostgreSQL

