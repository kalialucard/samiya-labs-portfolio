

1.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt`**
    *   **Explanation:** This is a basic command to start a directory brute-force scan.
        *   `-u http://example.com`: Specifies the target URL.
        *   `-w /path/to/wordlist.txt`: Specifies the wordlist file to use for brute-forcing.

2.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt -t 50`**
    *   **Explanation:** This command adds multithreading to speed up the scan.
        *   `-t 50`: Sets the number of threads to 50. More threads can speed up the scan but can also overwhelm the target or your network.

3.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt -o output.txt`**
    *   **Explanation:** This command saves the results to a file.
        *   `-o output.txt`: Specifies the output file name.

4.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt -x .php,.html,.js`**
    *   **Explanation:** This command filters the results to only show specific file extensions.
        *   `-x .php,.html,.js`: Only reports files with these extensions.

5.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt -s 200,201,301,302,403`**
    *   **Explanation:** This command specifies which HTTP status codes to report.
        *   `-s 200,201,301,302,403`: Reports directories/files that return these status codes (e.g., 200 OK, 301 Moved Permanently, 403 Forbidden).

6.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt -e .bak,.old`**
    *   **Explanation:** This command excludes specific file extensions from the scan.
        *   `-e .bak,.old`: Excludes files with these extensions.

7.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt -r`**
    *   **Explanation:** This command enables recursive scanning.
        *   `-r`: If a directory is found, DirBuster will attempt to scan within it using the same wordlist.

8.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt -p http://proxy.example.com:8080`**
    *   **Explanation:** This command routes the traffic through a proxy.
        *   `-p http://proxy.example.com:8080`: Uses the specified proxy server.

9.  **`dirbuster -u http://example.com -w /path/to/wordlist.txt -a "User-Agent: MyCustomAgent"`**
    *   **Explanation:** This command allows you to set a custom User-Agent header.
        *   `-a "User-Agent: MyCustomAgent"`: Sets a custom User-Agent string. This can sometimes bypass simple WAFs or logging mechanisms.

10. **`dirbuster -u http://example.com -w /path/to/wordlist.txt -d 5`**
    *   **Explanation:** This command sets the maximum depth for recursive scanning.
        *   `-d 5`: Limits the recursive scan to a depth of 5 directories.

### The Most Powerful Command

The "most powerful" command is subjective and depends on the specific scenario and target. However, a command that combines several options for a comprehensive and potentially aggressive scan would be:

**`dirbuster -u http://example.com -w /path/to/large_wordlist.txt -t 100 -r -s 200,201,301,302,403,401 -a "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"`**

**Explanation of why this is powerful:**

*   **`-u http://example.com`**: Targets the specific website.
*   **`-w /path/to/large_wordlist.txt`**: Utilizes a comprehensive wordlist. A larger, well-curated wordlist increases the chances of finding hidden directories and files.
*   **`-t 100`**: Uses a high number of threads (100). This significantly speeds up the scan, allowing for quicker discovery. **Caution:** This can be very resource-intensive and may trigger security alerts or cause instability on the target.
*   **`-r`**: Enables recursive scanning. This is crucial for discovering nested directories and a deeper structure of the web application.
*   **`-s 200,201,301,302,403,401`**: Reports common successful responses (200, 201), redirects (301, 302), and access-related errors (403 Forbidden, 401 Unauthorized). Finding 401 or 403 can indicate protected areas that might be vulnerable to further attacks.
*   **`-a "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"`**: Uses a common, legitimate-looking User-Agent string. This can help evade basic detection systems that might block default or suspicious User-Agents.

**Important Considerations:**

*   **Legality and Ethics:** Always ensure you have explicit permission to perform such scans on any target. Unauthorized scanning is illegal and unethical.
*   **Wordlists:** The effectiveness of DirBuster heavily relies on the quality and size of the wordlist. Common wordlists include SecLists, FuzzDB, or custom-built lists.
*   **Target Environment:** The "most powerful" command can vary. For a highly secured environment, you might need slower, stealthier scans. For a less protected one, aggressive scanning might be more effective.
*   **Resource Usage:** High thread counts and large wordlists consume significant CPU, memory, and network bandwidth.
*   **False Positives/Negatives:** No tool is perfect. DirBuster might report false positives or miss valid directories. Always verify findings manually.