import base64
import hashlib


def md5_short_hash(prefix: str, value: str) -> str:
    try:
        value = prefix + str(int(value))
        md5 = hashlib.md5(value.encode('utf-8')).digest()
        b64hash = base64.urlsafe_b64encode(md5).decode('ascii')
        b64hash = b64hash.removesuffix('==')
        return b64hash
    except:
        return ''