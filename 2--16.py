# bin_to_hex.py
def bin_to_hex(binary_str):
    """将二进制字符串转换为十六进制字符串（带 0x 前缀）"""
    # 去掉空格和常见前缀
    binary_str = binary_str.replace(" ", "").strip()
    if binary_str.lower().startswith("0b"):
        binary_str = binary_str[2:]
    
    # 检查是否只包含 0 和 1
    if not all(c in "01" for c in binary_str):
        return "错误：请输入有效的二进制数（只含 0 和 1）"
    
    if binary_str == "":
        return "错误：输入不能为空"
    
    # 补齐到 4 的倍数（每 4 位二进制 = 1 位十六进制）
    while len(binary_str) % 4 != 0:
        binary_str = "0" + binary_str
    
    # 直接用 Python 内置函数（最快最准）
    try:
        decimal = int(binary_str, 2)
        hex_result = hex(decimal)[2:].upper()  # 去掉 0x 前缀并大写
        return "0x" + hex_result
    except:
        return "转换失败"

print("=== 二进制转十六进制转换器 ===")
print("支持超大数字，直接回车或输入 q 退出\n")

while True:
    user_input = input("请输入二进制数：").strip()
    
    if user_input.lower() in ["q", "quit", "exit", ""]:
        print("再见！")
        break
    if user_input == "":
        continue
    
    result = bin_to_hex(user_input)
    print(f"结果：{result}\n")
