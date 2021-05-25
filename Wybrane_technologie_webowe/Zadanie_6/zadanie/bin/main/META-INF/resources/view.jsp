<%@ include file="/init.jsp" %>

<%  String fullName = renderRequest.getPreferences().getValue("fullName", "ERROR");
	String check = renderRequest.getPreferences().getValue("check", "ERROR");
	String email = renderRequest.getPreferences().getValue("email", "ERROR");
	String ip = renderRequest.getPreferences().getValue("ip", "ERROR");

if("true".equals(check)){
	%> <p>Zalogowany jako: <%= fullName %>. </p>
	<p>Adres email: <%= email %> </p>
	<p>Adres ip: <%= ip %></p> <% 
} else {
	%> <p>Zaloguj sie aby zobaczyc informacje.</p> <% 
}
%>
	