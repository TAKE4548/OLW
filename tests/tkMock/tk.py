from __future__ import annotations

import re
import tkinter as tk
from dataclasses import dataclass
from enum import IntEnum
from typing import Any, Callable, ClassVar


class _GeometryPatterns(IntEnum):
    SIZE_ONLY = 0
    POSITION_ONLY = 3
    FULL = 6


@dataclass
class _Geometry:
    """geometryの管理をやりやすくするためのクラス

    Args:
        width (int): 画面の幅
        height (int): 画面の高さ
        x (int): 画面位置のx座標
        y (int): 画面位置のy座標
    """
    width: int
    height: int
    x: int
    y: int
    ptn: ClassVar[re.Pattern] = re.compile(
        '({size})|({pos})|({size}{pos})'.format(size=r'(\d+)x(\d+)', pos=r'\+(\d+)\+(\d+)'), )

    def __str__(self) -> str:
        return f'{self.width}x{self.height}+{self.x}+{self.y}'

    def from_str(self, value: str) -> _Geometry:
        """geometryの文字列パターンからオブジェクトを生成する

        Args:
            value (str): 生成元のgeometry文字列パターン

        Raises:
            ValueError: 文字列がgeometryのパターンにあってない時

        Returns:
            _Geometry: 生成したオブジェクト
        """
        m = self.ptn.fullmatch(value)

        if m is None:
            raise ValueError(f'{value}はgeometryの文字列パターンにマッチしてない')

        # サイズだけ指定された場合、位置は現在の値を使う
        if m.groups()[_GeometryPatterns.SIZE_ONLY]:
            w, h = tuple(m.groups()[_GeometryPatterns.SIZE_ONLY + i] for i in range(2))
            x = self.x
            y = self.y
        # 位置だけ指定された場合、サイズは現在の値を使う
        elif m.groups()[_GeometryPatterns.POSITION_ONLY]:
            x, y = tuple(m.groups()[_GeometryPatterns.POSITION_ONLY + i] for i in range(2))
            w = self.width
            h = self.height
        # すべて指定された場合、全部の値を指定値にする
        else:
            w, h, x, y = tuple(m.groups()[_GeometryPatterns.FULL + i] for i in range(4))

        return self.__class__(*map(int, (w, h, x, y)))


class TkMock(tk.Tk):
    """tk.Tkのテスト用モック"""

    def __init__(self, *args, **kwargs):
        self.__is_destroyed = False
        self.__protocols: dict[str, Callable[[], object] | str] = {}
        self.__attributes: dict[str, Any] = {}
        self.__geometry = _Geometry(100, 100, 0, 0)
        super().__init__(*args, **kwargs)

    @property
    def is_destroyed(self) -> bool:
        return self.__is_destroyed

    def destroy(self):
        """本家Tkのdestroyの代わりに、自身のフラグを制御する"""
        self.__is_destroyed = True

    def protocol(self, name: str, func: Callable[[], object] | str):
        """本家Tkのprotocolの代わりに、自身のコールバック設定履歴に登録する

        Args:
            name (str): protocolの設定するイベント名
            func (Callable[[], object] | str): 設定するコールバック関数の実体若しくは関数名
        """
        self.__protocols[name] = func

    def find_callback(self, name: str) -> Callable[[], object] | str | None:
        """protocolで設定されたコールバックを返す

        Args:
            name (str): コールバックを取得するイベント名

        Returns:
            Callable[[], object] | str | None: 設定済みのコールバック関数若しくは関数名.未設定の場合はNone
        """
        return self.__protocols.get(name, None)

    def attributes(self, option: str, value: Any | None = None) -> Any | None:
        """本家Tkのattributesの代わりに、自身のアトリビュート設定履歴に登録する

        Args:
            option (str): 設定するアトリビュートの名前
            value (Any | None): 設定するアトリビュートの値.None渡すと現在値が返る

        Return:
            Any | None: optionで指定したアトリビュートの現在値.valueに設定値を渡した場合はNone
        """
        if value is None:
            return self.__attributes.get(option)
        self.__attributes[option] = value

    def find_attribute(self, option: str) -> Any:
        """attributeで設定された値を返す

        Args:
            option (str): 値を取得するアトリビュート名

        Returns:
            Any: アトリビュートの値
        """
        return self.__attributes.get(option, None)

    def geometry(self, value: str | None = None) -> str:
        """本家Tkのgeometryに代わって、geometryの設定を保存する

        Args:
            value (str | None): 設定するgeometryの文字列パターン.Noneだと現在の設定をそのまま返す

        Returns:
            str: geometryの設定値
        """
        if value is None:
            return str(self.__geometry)
        self.__geometry = self.__geometry.from_str(value)
        return str(self.__geometry)
