# chat/utils.py
import hashlib

def get_valid_group_name(name):
    # 유니코드 문자열을 해시하여 ASCII 문자열로 변환
    hash_object = hashlib.sha256(name.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig[:100]
