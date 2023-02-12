from enum import StrEnum


class MouseEvents(StrEnum):
    LeftClick = '<Button-1>'
    CenterClick = '<Button-2>'
    RightClick = '<Button-3>'
    LeftRelease = '<ButtonRelease-1>'
    CenterRelease = '<ButtonRelease-2>'
    RightRelease = '<ButtonRelease-3>'
