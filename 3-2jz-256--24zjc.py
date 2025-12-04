import hashlib
def entropy_to_mnemonic(entropy_bin, wordlist_path='english.txt'):
    if len(entropy_bin) != 256 or not all(c in '01' for c in entropy_bin):
        return "必须是256位"
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            wordlist = [line.strip() for line in f.readlines() if line.strip()]
        print(f"加载 {len(wordlist)} 个单词（应为2048）")
    except FileNotFoundError:
        return "错误: 请确保路径 '{wordlist_path}' 正确。"
    except Exception as e:
        return f"加载文件错误: {e}"
    if len(wordlist) != 2048:
        return f"警告: 单词列表{len(wordlist)}，应为2048"
    entropy_bytes = int(entropy_bin, 2).to_bytes(32, 'big')
    hash_bytes = hashlib.sha256(entropy_bytes).digest()
    hash_bin = bin(int.from_bytes(hash_bytes, 'big'))[2:].zfill(256)
    checksum_bits = hash_bin[:8]
    print(f"计算的8位校验码: {checksum_bits}")
    total_bin = entropy_bin + checksum_bits
    print(f"总序列长度: {len(total_bin)}")
    words = []
    for i in range(0, 264, 11):
        group = total_bin[i:i+11]
        if len(group) < 11:
            group = group.zfill(11)
        index = int(group, 2)
        if 0 <= index < len(wordlist):
            words.append(wordlist[index])
        else:
            words.append(f"[无效索引: {index}]")
    return ' '.join(words)
if __name__ == "__main__":
    print("请输入:")
    entropy_input = input().strip()
    mnemonic = entropy_to_mnemonic(entropy_input)
    print(f"\n{mnemonic}")
    if "[无效索引" in mnemonic:
        print("警告: 检查二进制字符串")
