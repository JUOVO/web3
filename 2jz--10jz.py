#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二进制转十进制工具
同时输出十进制数的位数（digits）
支持 0b 前缀、空格、超大整数
"""


def binary_to_decimal(binary_str: str) -> int:
    """清理输入并转换为十进制整数"""
    cleaned = binary_str.replace(' ', '').replace('\t', '').replace('_', '')
    if cleaned.lower().startswith('0b'):
        cleaned = cleaned[2:]
    
    if not cleaned:
        raise ValueError("请输入二进制数！")
    
    if not all(c in '01' for c in cleaned):
        raise ValueError("输入包含非法字符！只允许 0 和 1")
    
    return int(cleaned, 2)


def count_decimal_digits(n: int) -> int:
    """计算十进制位数（超级快，即使对几万位的超大整数也秒返回）"""
    if n == 0:
        return 1
    # 方法1：最快（推荐）
    import math
    return math.floor(math.log10(n)) + 1
    
    # 方法2：备选（对极大数据更稳健（Python原生支持）
    # return len(str(n))


def main():
    print("=== 二进制转十进制 + 位数统计工具 ===\n")
    
    while True:
        user_input = input("请输入二进制数（q 退出）: ").strip()
        
        if user_input.lower() in ['q', '', 'exit', 'bye']:
            print("再见！")
            break
        
        try:
            decimal = binary_to_decimal(user_input)
            digits = count_decimal_digits(decimal)
            
            print(f"十进制结果: {decimal}")
            print(f"十进制位数: {digits} 位\n")
            
        except ValueError as e:
            print(f"错误: {e}\n")


if __name__ == "__main__":
    main()
