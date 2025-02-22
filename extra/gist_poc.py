# /// script
# dependencies = [
#   "requests<3",
# ]
# ///

# Interesting idea here - we can store SFAs in gist - curl them then run them locally. Food for thought.

import requests


def fetch_gist_content():
    # 1. The raw link to your specific file in the Gist
    raw_url = "https://gist.githubusercontent.com/disler/d8d8abdb17b2072cff21df468607b176/raw/sfa_poc.py"

    try:
        # 2. Use requests to fetch the file's content
        response = requests.get(raw_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # 3. Get the content
        sfa_poc_file_contents = response.text

        # 4. Print the content
        print(sfa_poc_file_contents)

        return sfa_poc_file_contents

    except requests.RequestException as e:
        print(f"Error fetching gist content: {e}")
        return None


if __name__ == "__main__":
    fetch_gist_content()
