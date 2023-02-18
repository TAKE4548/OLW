from dataclasses import dataclass
from typing import TypeVar

T = TypeVar('T', bound='Point')


@dataclass
class Point:
    """画面の座標を扱う値オブジェクト

    Attributes:
        x (int): x座標
        y (int): y座標
    """
    x: int
    y: int

    def for_geometry(self) -> str:
        """tkのgeometry設定向けの文字列にして返す

        Returns:
            str: geometryに渡す座標系フォーマットの文字列
        """
        return f'+{self.x}+{self.y}'

    def copy(self: T) -> T:
        """値の全く同じ別の座標インスタンスを生成して返す

        Args:
            self (Point): 生成した新しい座標インスタンス

        Returns:
            T: _description_
        """
        return self.__class__(self.x, self.y)
