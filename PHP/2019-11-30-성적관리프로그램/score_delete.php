<?php
 // 아래 dbid, dbpw, dbname을 변경해주시기 바랍니다.
 $connect=mysql_connect("localhost", "dbid", "dbpw");
 $dbconn=mysql_select_db("dbname", $connect);
 
 // 필드 num이 $num 값을 가지는 레코드 삭제
 $sql="delete from stud_score where num=$num";
 mysql_query($sql, $connect);
 
 mysql_close($connect);
 
 // score_list.php 로 돌아감
 Header("Location:score_list.php");
?>