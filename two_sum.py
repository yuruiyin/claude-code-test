"""两数之和模块 - 提供简单的两数相加功能。"""

import argparse
from typing import Union


Number = Union[int, float]


def add_two_numbers(a: Number, b: Number) -> Number:
    """计算两个数的和。

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两个数的和

    Raises:
        TypeError: 如果参数不是数字类型
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"参数 a 必须是数字类型，实际得到 {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"参数 b 必须是数字类型，实际得到 {type(b).__name__}")
    return a + b


def main() -> None:
    """命令行入口函数。"""
    parser = argparse.ArgumentParser(description="计算两个数的和")
    parser.add_argument("a", type=float, help="第一个数")
    parser.add_argument("b", type=float, help="第二个数")
    args = parser.parse_args()

    result = add_two_numbers(args.a, args.b)
    print(f"两数之和: {args.a} + {args.b} = {result}")


if __name__ == "__main__":
    main()
