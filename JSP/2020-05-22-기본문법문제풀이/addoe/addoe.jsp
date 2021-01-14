<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTDHTML4.01Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <title>oddoe</title>
    </head>
    <body>
        <h1>1~10까지 짝수, 홀수합 구하기</h1>
        <%
            int oddResult = 0;
            int evenResult = 0;
            for (int i = 1; i <= 10; i++)
            {
                if (i%2 == 1)
                {
                    oddResult += i;
                }
                else
                {
                    evenResult += i;
                }
            }
         %>
        <h1>홀수합 : <%=oddResult%></h1>
        <h1>짝수합 : <%=evenResult%></h1>
    </body>
</html>