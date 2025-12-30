---
title: Cyberheroes
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Cyberheroes
  machine on TryHackMe.
slug: cyberheroes
---




**Target:** `10.201.62.16`

**Summary:** Found a login page (`login.html`). Inspecting the page revealed client-side JavaScript that checks credentials by reversing a hard-coded string. The username and password can be derived from the script and used to either submit the form or request the flag file directly.

---

## Discovery

* Found `login.html` on the webroot.
* Open the page in your browser ([http://10.201.62.16/login.html](http://10.201.62.16/login.html)) and use the browser inspector to view the JS.

## Relevant JavaScript (as found in the page)

```js
function authenticate() {
  a = document.getElementById('uname')
  b = document.getElementById('pass')
  const RevereString = str => [...str].reverse().join('');
  if (a.value=="h3ck3rBoi" & b.value==RevereString("54321@terceSrepuS")) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("flag").innerHTML = this.responseText ;
        document.getElementById("todel").innerHTML = "";
        document.getElementById("rm").remove() ;
      }
    };
    xhttp.open("GET", "RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_"+a.value+"_"+b.value+".txt", true);
    xhttp.send();
  }
  else {
    alert("Incorrect Password, try again.. you got this hacker !")
  }
}
```

## What the script does (plain English)

* The script expects `uname` to be `h3ck3rBoi`.
* The script uses a helper `RevereString` (which reverses a string) on the literal `"54321@terceSrepuS"` and compares that to the password field.
* So the actual password is the **reverse** of `54321@terceSrepuS`.
* When both username and password match, the page requests a flag file named:

```
RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_<username>_<password>.txt
```

(constructed by concatenating the string with `a.value` and `b.value`).

## Derived credentials

* **Username:** `h3ck3rBoi`
* **Password:** reverse of `54321@terceSrepuS` -> `SuperSecret@12345`

> Note: the code uses a single `&` where you'd normally expect `&&`. In this context it still evaluates the conditional as intended, but it is sloppy JavaScript.

## Fetch the flag directly (recommended)

Because the server fetches a predictable filename, you can request the file directly. Remember to URL-encode special characters (the `@` becomes `%40`).

* **Raw filename (with special char):**

```
RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_h3ck3rBoi_SuperSecret@12345.txt
```

* **URL-encoded filename:**

```
RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_h3ck3rBoi_SuperSecret%4012345.txt
```

* **curl command (HTTP):**

```bash
curl -s "http://10.201.62.16/RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_h3ck3rBoi_SuperSecret%4012345.txt"
```

* **Browser:** open the URL in the address bar (same encoded path) while connected to the lab network:

```
http://10.201.62.16/RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_h3ck3rBoi_SuperSecret%4012345.txt
```

If the file exists and is accessible, the server will return the flag contents.

## Alternate: use the login form

1. Open `http://10.201.62.16/login.html` in your browser.
2. Enter `h3ck3rBoi` as username and `SuperSecret@12345` as password.
3. Submit — the page will run the JS and, on success, display the flag inside the page element with id `flag` (or it will remove some DOM elements as the script indicates).

## Quick commands to reproduce locally

* Reverse string with `rev`:

```bash
echo "54321@terceSrepuS" | rev
# -> SuperSecret@12345
```

* Reverse with Python:

```bash
python3 -c "print('54321@terceSrepuS'[::-1])"
# -> SuperSecret@12345
```

* Fetch the file (curl):

```bash
curl -s "http://10.201.62.16/RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_h3ck3rBoi_SuperSecret%4012345.txt"
```

---

## Notes & tips

* If the server returns 404 or 403, try fetching the directory listing (if allowed) or re-check the exact filename/punctuation. Pay attention to case-sensitivity.
* If the lab requires the request to come from the same origin (CORS or auth), attempting to fetch directly via curl may still work since it is a simple HTTP GET; if not, use the browser form.
* Save this walk-through entry to your `walkin.md` collection so you can reference it later.

##

* **Username:** `h3ck3rBoi`
* **Password:** `SuperSecret@12345`
* **Direct file (encoded):** `RandomLo0o0o0o0o0o0o0o0o0o0gpath12345_Flag_h3ck3rBoi_SuperSecret%4012345.txt`
* Use curl or your browser to retrieve the flag.