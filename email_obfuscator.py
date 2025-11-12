# email_obfuscator.py

# blathnaid@iremail.ie -> b********@i******.ie

import sys
import re

email_pattern = "([A-Za-z0-9._%+-])([A-Za-z0-9._%+-]*)(@[\\w.-]+\\.[A-Za-z]{2,})"

def obfuscate(matches):
    # print (matches.group(1))
    # print (matches.group(2))
    # print (matches.group(3))
    # print (f"{matches.group(1)}{"*" * len(matches.group(2))}{matches.group(3)}")
    return f"{matches.group(1)}{"*" * len(matches.group(2))}{matches.group(3)}"

for line in sys.stdin:
    result = re.sub(email_pattern, lambda m: f"{m.group(1)}{"*" * len(m.group(2))}{m.group(3)}", line)
    print (result, end="")