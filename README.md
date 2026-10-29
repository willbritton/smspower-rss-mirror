This repo mirrors the RSS feed from https://www.smspower.org:443/forums/rss.php every 10 minutes, to the following URL:

https://raw.githubusercontent.com/willbritton/smspower-rss-mirror/refs/heads/main/rss.xml

It also filters out any post with '[AI]' in the title to two separate feeds, one without the tagged posts, and one with only the tagged posts:

https://raw.githubusercontent.com/willbritton/smspower-rss-mirror/refs/heads/main/no-ai.xml
https://raw.githubusercontent.com/willbritton/smspower-rss-mirror/refs/heads/main/only-ai.xml

And Atom variants:

https://raw.githubusercontent.com/willbritton/smspower-rss-mirror/refs/heads/main/no-ai-atom.xml
https://raw.githubusercontent.com/willbritton/smspower-rss-mirror/refs/heads/main/only-ai-atom.xml
