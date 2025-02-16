#!/usr/bin/env bash

# Interesting idea here - we can store SFAs in gist - curl them then run them locally. Food for thought.

# 1. The raw link to your specific file in the Gist.
#    Note: The exact raw link may change if the Gist is updated, so check the "Raw" button
#    in your Gist to make sure you have the correct URL.
RAW_URL="https://gist.githubusercontent.com/disler/d8d8abdb17b2072cff21df468607b176/raw/sfa_poc.py"

# 2. Use curl to fetch the file's content and store it in a variable.
SFA_POC_FILE_CONTENTS="$(curl -sL "$RAW_URL")"

# 3. Now you can do whatever you want with $SFA_POC_FILE_CONTENTS.
#    For example, just echo it:
echo "$SFA_POC_FILE_CONTENTS"
