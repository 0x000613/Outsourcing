<meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
<?php
 // 아래 dbid, dbpw, dbname을 변경해주시기 바랍니다.
 $connect=mysql_connect("localhost", "dbid", "dbpw");
 $dbconn=mysql_select_db("dbname", $connect);
 
 $sql="create table stud_score (";
 $sql.="num int not null auto_increment, ";
 $sql.="name varchar(12), ";
 $sql.="sub1 int, ";
 $sql.="sub2 int, ";
 $sql.="sub3 int, ";
 $sql.="sub4 int, ";
 $sql.="sub5 int, ";
 $sql.="sum int, ";
 $sql.="avg float, ";
 $sql.="primary key(num))";
 
 $result=mysql_query($sql, $connect);
 
 if ($result)
  echo "데이터베이스 테이블 stud_score가 생성되었습니다!";
 else
  echo "데이터베이스 테이블 생성 에러!!!";
 
 mysql_close();
?>