<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
    request.setCharacterEncoding("utf-8");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>oddeven</title>
</head>
<body>
    <%
        int num = Integer.parseInt(request.getParameter("num"));
        String result = "";
        switch (num%2) {
        case 0:
            switch(num)
            {
                case 0:
                    result = "0"
                    break;

                default:
                    result = "짝수";
                    break;
            }
            break;
        default:
            result = "홀수"
        }
        out.println("입력하신 수는 <b>" + result + "</b> 입니다.");
    %>
 
</body>
</html>