---
cssclass: dashboard
---

# 🚀 Mission Control

> [!TIP]
> This dashboard requires the **Dataview** plugin. 
> Go to **Settings > Community Plugins > Browse** and install **Dataview**.

## ⚡ Active Writeups
```dataview
TABLE category as "Platform", date as "Date", enrich as "AI Ready"
FROM "content/writeups"
WHERE file.name != "Untitled"
SORT date DESC
LIMIT 10
```

## 🧩 Templates
```dataview
LIST
FROM "content/templates"
```

## 📊 Stats
```dataviewjs
let ft = dv.pages('"content/writeups"').where(p => p.category == "tryhackme").length;
let htb = dv.pages('"content/writeups"').where(p => p.category == "hackthebox").length;

dv.paragraph(`
**TryHackMe**: ${ft}  
**HackTheBox**: ${htb}
`)
```
