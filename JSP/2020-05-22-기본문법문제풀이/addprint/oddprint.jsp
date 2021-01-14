<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTDHTML4.01Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <title>oddadd</title>
    </head>
    <body>
        <h1>1~10까지 While문으로 홀수 출력하기</h1>
        <%
            int i = 1;
            int oddResult = 0;
            while(i <= 10)
            {
                if(i%2 == 1)
                {
                    oddResult = i
                }
                i++;
            }
         %>
         <h1><%=oddResult%>는 홀수입니다.</h1>
    </body>
</html>