import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regex to extract the src URL from the iframe
    match = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/.*?)"', s)

    if match:
        # Extract the URL
        result = match.group(1)
        # Normalize the URL: Ensure "https" and remove "/embed" and "www."
        result = result.replace("http://", "https://").replace("/embed", "").replace("www.youtube.com", "youtu.be").replace("youtube.com", "youtu.be")
        return result
    else:
        return None


if __name__ == "__main__":
    main()
