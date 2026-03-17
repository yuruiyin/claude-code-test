"""
两数之和模块
提供简单的两数相加功能
"""


def add_two_numbers(a, b):
    """
    计算两个数的和

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两个数的和
    """
    return a + b


if __name__ == "__main__":
    # 示例：计算并输出 3 和 5 的和
    result = add_two_numbers(3, 5)
    print(f"两数之和: 3 + 5 = {result}")
