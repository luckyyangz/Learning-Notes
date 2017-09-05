#matches
String[] ss=new String[]{"a98b","c0812d","c10b","ab","ad"};
for(String s:ss)
  System.out.println(s.matches("[ac]\\d*[bd]"));
  
#split 重载形式
String s="GET /insex.html HTTP/1.1";
String ss[]=s.split(" +");  
for(String str:ss)
  System.out.println(str);
/*out:
GET
/index.html
HTTP/1.1 */
#replaceAll and replaceFirst
 public String replaceAll(String regex,String replacement)
 public String replaceFirst(String regex,String replacement)
 
