**SQLi & HTML Injection** 

### SQL Injection & HTML Injection

#### Aim:
To learn how to perform HTML Injection and SQL Injection attacks on vulnerable web applications and understand the implications of these security vulnerabilities.

#### Tools:
- **SQLMAP**: An open-source penetration testing tool used to detect and exploit SQL injection vulnerabilities in web applications.

#### Theory:
**HTML Injection**:  
HTML Injection is a technique that exploits vulnerabilities in web applications by injecting malicious HTML code into the web pages presented to users. This often occurs due to the application's failure to validate user inputs. Attackers can craft HTML-formatted text that modifies the displayed content, allowing for the inclusion of attacker-controlled elements that can alter how the application behaves or presents information.

**SQL Injection (SQLi)**:  
SQL Injection is a code injection technique that allows attackers to execute malicious SQL queries against a web application's database. By exploiting vulnerabilities in input fields, attackers can manipulate database queries, potentially gaining unauthorized access to sensitive information. SQLMAP automates the process of detecting SQL injection vulnerabilities and performing various database operations, such as fetching database names, table names, and column names.

#### Outcome:
Upon completion of this experiment, students will be able to:
1. Identify and perform HTML Injection on vulnerable parameters within a web application.
2. Detect and exploit SQL Injection vulnerabilities using the SQLMAP tool.

#### Result & Discussion:
**HTML Injection Results**:  
Students executed basic payloads, such as `<marquee>test</marquee>` and `<h1>test</h1>`, in the search box of a web application to test for HTML injection vulnerabilities. The responses reflected the injected HTML code, indicating a successful injection. This activity demonstrated the potential for attackers to alter web page content and highlighted the importance of input validation to prevent such attacks.

**SQL Injection Results**:  
Using SQLMAP, students performed a series of commands to enumerate databases, tables, and columns. They successfully executed commands to fetch database names (`--dbs`), list tables (`--tables`), and dump data from a specified table (`--dump`). Each step illustrated how SQL injection could be used to extract sensitive information from databases. 

The discussion emphasized the importance of securing web applications against both HTML and SQL injection vulnerabilities. Students recognized the need for robust validation and sanitation of user inputs to mitigate the risks associated with these types of attacks. Furthermore, the ethical implications of performing such attacks were highlighted, underscoring the necessity for responsible usage in security testing contexts.

