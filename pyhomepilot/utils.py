import hashlib


def sha256hex(value) -> str:
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def reverse_percentage(percentage) -> int:
    return 100 - percentage

def format_url(url) -> str:
    if url.startswith('http://') or url.startswith('https://'):
        return url
    return f"http://{url}"