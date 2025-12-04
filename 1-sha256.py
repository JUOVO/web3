import hashlib
def text_to_sha256(text):
    hash_object = hashlib.sha256(text.encode('utf-8'))
    return hash_object.hexdigest()
if __name__ == "__main__":
    user_input = input("请输入：")
    sha256_hash = text_to_sha256(user_input)
    print(f" {sha256_hash}")
