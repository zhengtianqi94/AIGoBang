import math

def get_distance(p0, p1):
    """计算两个点之间的距离"""
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

def pos_in_board(x, y):
    """棋局中的点计算在棋盘中的位置"""
    return x * 30 + 25, y * 30 + 25

def pos_in_qiju(x, y):
    """棋盘中的点计算在棋局中的位置"""
    return int((x - 25) / 30), int((y - 25) / 30)

def pos_to_draw(*args):
    """计算棋子在棋盘的顶，底，左，右的位置"""
    x, y = args
    return x - 11, y - 11, x + 11, y + 11

def click_in_board(x, y):
    """判断鼠标是否点击到棋盘里面"""
    return x > 10 and x < 460 and y > 10 and y < 460
