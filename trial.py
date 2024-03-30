import requests

def validate_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:  # URL is valid and accessible
            return True
        else:
            return False  # URL is valid but returns an error (e.g., 404)
    except requests.exceptions.RequestException:
        return False  # URL is invalid or inaccessible

# Example usage:
url = "https://docs.python.org/3/library/pwinput.html#module-pwinput"
if validate_url(url):
    print(f"{url} is valid and accessible.")
else:
    print(f"{url} is either invalid or inaccessible, or it returns an error (e.g., 404).")
