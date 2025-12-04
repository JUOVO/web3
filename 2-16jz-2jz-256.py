def hex_to_256bit_bin(hex_str):
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    try:
        int_val = int(hex_str, 16)
        binary_str = bin(int_val)[2:]
        return binary_str.zfill(256)
    except ValueError:
        raise ValueError("无效的十六进制")
if __name__ == "__main__":

    user_input = input("请输入：").strip()
    try:
        binary_256bit = hex_to_256bit_bin(user_input)
        print(f"\n{binary_256bit}")
    except ValueError as e:
        print(f"错误: {e}")
