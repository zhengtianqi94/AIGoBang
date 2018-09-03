class Robot(object):
    '''基于五子棋规则写的一个机器人'''

    def __init__(self, _board):
        self.board = _board

    def haveValuePoints(self, player, enemy, board):
        """算出棋盘中所有有价值的点"""
        points = []

        for x in range(15):
            for y in range(15):
                list1 = []
                list2 = []
                list3 = []
                list4 = []
                if self.board[x][y] == -1:
                    for tmp in range(9):
                        i = x + tmp - 4
                        j = y + tmp - 4
                        if i < 0 or i > 14:
                            list1.append(-2)
                        else:
                            list1.append(board[i][y])
                        if j < 0 or j > 14:
                            list2.append(-2)
                        else:
                            list2.append(board[x][j])
                        if i < 0 or j < 0 or i > 14 or j > 14:
                            list3.append(-2)
                        else:
                            list3.append(board[i][j])
                        k = y - tmp + 4
                        if i < 0 or k < 0 or i > 14 or k > 14:
                            list4.append(-2)
                        else:
                            list4.append(board[i][k])


                    playerValue = self.value_point(player, enemy, list1, list2, list3, list4)
                    enemyValue = self.value_point(enemy, player, list1, list2, list3, list4)
                    if enemyValue >= 10000:
                        enemyValue -= 500
                    elif enemyValue >= 5000:
                        enemyValue -= 300
                    elif enemyValue >= 2000:
                        enemyValue -= 250
                    elif enemyValue >= 1500:
                        enemyValue -= 200
                    elif enemyValue >= 99:
                        enemyValue -= 10
                    elif enemyValue >= 5:
                        enemyValue -= 1
                    value = playerValue + enemyValue
                    if value > 0:
                        points.append([x, y, value])
        return points

    def MaxValue_po(self, player, enemy):
        """算出最大价值的点"""
        points = self.haveValuePoints(player, enemy, self.board)
        flag = 0
        _point = []
        for p in points:
            if p[2] > flag:
                _point = p
                flag = p[2]
        return _point[0], _point[1], _point[2]

    def value_point(self, player, enemy, list1, list2, list3, list4):
        """算出点的价值"""
        flag = 0
        flag += self.willbefive(player, list1)
        flag += self.willbefive(player, list2)
        flag += self.willbefive(player, list3)
        flag += self.willbefive(player, list4)
        flag += self.willbealive4(player, list1)
        flag += self.willbealive4(player, list2)
        flag += self.willbealive4(player, list3)
        flag += self.willbealive4(player, list4)
        flag += self.willbesleep4(player, enemy, list1)
        flag += self.willbesleep4(player, enemy, list2)
        flag += self.willbesleep4(player, enemy, list3)
        flag += self.willbesleep4(player, enemy, list4)
        flag += self.willbealive3(player, list1)
        flag += self.willbealive3(player, list2)
        flag += self.willbealive3(player, list3)
        flag += self.willbealive3(player, list4)
        flag += self.willbesleep3(player, enemy, list1)
        flag += self.willbesleep3(player, enemy, list2)
        flag += self.willbesleep3(player, enemy, list3)
        flag += self.willbesleep3(player, enemy, list4)
        flag += self.willbealive2(player, enemy, list1)
        flag += self.willbealive2(player, enemy, list2)
        flag += self.willbealive2(player, enemy, list3)
        flag += self.willbealive2(player, enemy, list4)
        flag += self.willbesleep2(player, enemy, list1)
        flag += self.willbesleep2(player, enemy, list2)
        flag += self.willbesleep2(player, enemy, list3)
        flag += self.willbesleep2(player, enemy, list4)
        return flag

    def willbefive(self, player, checklist):
        """下在这个点将会得到连无"""
        if checklist[0] == player and checklist[1] == player and \
                checklist[2] == player and checklist[3] == player:
            return 10000
        elif checklist[5] == player and checklist[6] == player and \
                checklist[7] == player and checklist[8] == player:
            return 10000
        elif checklist[2] == player and checklist[3] == player and \
                checklist[5] == player and checklist[6] == player:
            return 10000
        elif checklist[1] == player and checklist[2] == player and \
                checklist[3] == player and checklist[5] == player:
            return 10000
        elif checklist[3] == player and checklist[5] == player and \
                checklist[6] == player and checklist[7] == player:
            return 10000
        else:
            return 0

    def willbealive4(self, player, checklist):
        """下在这个点将会形成活四"""
        if checklist[0] == -1 and checklist[1] == player and \
                checklist[2] == player and checklist[3] == player \
                and checklist[5] == -1:
            return 5000
        elif checklist[3] == -1 and checklist[5] == player and \
                checklist[6] == player and checklist[7] == player \
                and checklist[8] == -1:
            return 5000
        elif checklist[1] == -1 and checklist[2] == player and \
                checklist[3] == player and checklist[5] == player \
                and checklist[6] == -1:
            return 5000
        elif checklist[2] == -1 and checklist[3] == player and \
                checklist[5] == player and checklist[6] == player \
                and checklist[7] == -1:
            return 5000
        else:
            return 0

    def willbesleep4(self, player, enemy, checklist):
        """下在这个点会形成眠四"""
        if checklist[0] == enemy and checklist[1] == player and \
                checklist[2] == player and checklist[3] == player \
                and checklist[5] == -1:
            return 1700
        elif checklist[1] == enemy and checklist[2] == player and \
                checklist[3] == player and checklist[5] == player \
                and checklist[6] == -1:
            return 1700
        elif checklist[2] == enemy and checklist[3] == player and \
                checklist[5] == player and checklist[6] == player \
                and checklist[7] == -1:
            return 1700
        elif checklist[3] == enemy and checklist[5] == player and \
                checklist[6] == player and checklist[7] == player \
                and checklist[8] == -1:
            return 1700
        elif checklist[0] == -1 and checklist[1] == player and \
                checklist[2] == player and checklist[3] == player \
                and checklist[5] == enemy:
            return 1700
        elif checklist[1] == -1 and checklist[2] == player and \
                checklist[3] == player and checklist[5] == player \
                and checklist[6] == enemy:
            return 1700
        elif checklist[2] == -1 and checklist[3] == player and \
                checklist[5] == player and checklist[6] == player \
                and checklist[7] == enemy:
            return 1700
        elif checklist[3] == -1 and checklist[5] == player and \
                checklist[6] == player and checklist[7] == player \
                and checklist[8] == enemy:
            return 1700
        else:
            return 0

    def willbealive3(self, player, checklist):
        """下在这个点会形成活三"""
        if checklist[0] == -1 and checklist[1] == -1 and \
                checklist[2] == player and checklist[3] == player \
                and checklist[5] == -1:
            return 1900
        elif checklist[1] == -1 and checklist[2] == -1 and \
                checklist[3] == player and checklist[5] == player \
                and checklist[6] == -1:
            return 1900
        elif checklist[2] == -1 and checklist[3] == -1 and \
                checklist[5] == player and checklist[6] == player \
                and checklist[7] == -1:
            return 1900
        elif checklist[1] == -1 and checklist[2] == player and \
                checklist[3] == player and checklist[5] == -1 \
                and checklist[6] == -1:
            return 1900
        elif checklist[2] == -1 and checklist[3] == player and \
                checklist[5] == player and checklist[6] == -1 \
                and checklist[7] == -1:
            return 1900
        elif checklist[3] == -1 and checklist[5] == player and \
                checklist[6] == player and checklist[7] == -1 \
                and checklist[8] == -1:
            return 1900
        elif checklist[0] == -1 and checklist[1] == player and \
                checklist[2] == player and checklist[3] == -1 \
                and checklist[5] == -1:
            return 1600
        elif checklist[2] == -1 and checklist[3] == player and \
                checklist[6] == player and checklist[5] == -1 \
                and checklist[7] == -1:
            return 1600
        elif checklist[3] == -1 and checklist[5] == player and \
                checklist[7] == player and checklist[6] == -1 \
                and checklist[8] == -1:
            return 1600
        elif checklist[3] == -1 and checklist[5] == -1 and \
                checklist[7] == player and checklist[6] == player \
                and checklist[8] == -1:
            return 1600
        elif checklist[0] == -1 and checklist[1] == player and \
                checklist[2] == player and checklist[3] == -1 \
                and checklist[6] == -1:
            return 1600
        elif checklist[0] == -1 and checklist[1] == player and \
                checklist[2] == player and checklist[3] == -1 \
                and checklist[6] == -1:
            return 1600
        else:
            return 0

    def willbesleep3(self, player, enemy, checklist):
        """下在这个点会形成眠三"""
        if checklist[1] == enemy and checklist[2] == player and \
                checklist[3] == player and checklist[5] == -1 \
                and checklist[6] == -1:
            return 350
        elif checklist[2] == enemy and checklist[3] == player and \
                checklist[5] == player and checklist[6] == -1 \
                and checklist[7] == -1:
            return 350
        elif checklist[3] == enemy and checklist[5] == player and \
                checklist[6] == player and checklist[7] == -1 \
                and checklist[8] == -1:
            return 350
        elif checklist[0] == -1 and checklist[1] == -1 and \
                checklist[2] == player and checklist[3] == player \
                and checklist[5] == enemy:
            return 350
        elif checklist[1] == -1 and checklist[2] == -1 and \
                checklist[3] == player and checklist[5] == player \
                and checklist[6] == enemy:
            return 350
        elif checklist[2] == -1 and checklist[3] == -1 and \
                checklist[5] == player and checklist[6] == player \
                and checklist[7] == enemy:
            return 350
        elif checklist[0] == enemy and checklist[1] == -1 and \
                checklist[2] == player and checklist[3] == player \
                and checklist[5] == -1 and checklist[6] == enemy:
            return 300
        elif checklist[1] == enemy and checklist[2] == -1 and \
                checklist[3] == player and checklist[5] == player \
                and checklist[6] == -1 and checklist[7] == enemy:
            return 300
        elif checklist[2] == enemy and checklist[3] == -1 and \
                checklist[5] == player and checklist[6] == player \
                and checklist[7] == -1 and checklist[8] == enemy:
            return 300
        elif checklist[0] == enemy and checklist[1] == player and \
                checklist[2] == -1 and checklist[3] == player \
                and checklist[5] == -1 and checklist[6] == enemy:
            return 300
        elif checklist[1] == enemy and checklist[2] == player and \
                checklist[3] == -1 and checklist[5] == player \
                and checklist[6] == -1 and checklist[7] == enemy:
            return 300
        elif checklist[2] == enemy and checklist[3] == player and \
                checklist[5] == -1 and checklist[6] == player \
                and checklist[7] == -1 and checklist[8] == enemy:
            return 300
        elif checklist[0] == enemy and checklist[1] == player and \
                checklist[2] == -1 and checklist[3] == player \
                and checklist[5] == -1 and checklist[6] == enemy:
            return 300
        elif checklist[1] == enemy and checklist[2] == player and \
                checklist[3] == -1 and checklist[5] == player \
                and checklist[6] == -1 and checklist[7] == enemy:
            return 300
        elif checklist[3] == enemy and checklist[5] == -1 and \
                checklist[6] == player and checklist[7] == player \
                and checklist[8] == -1:
            return 300
        elif checklist[0] == enemy and checklist[1] == player and \
                checklist[2] == player and checklist[3] == -1 \
                and checklist[5] == -1:
            return 300
        elif checklist[2] == enemy and checklist[3] == player and \
                checklist[5] == -1 and checklist[6] == player \
                and checklist[7] == -1:
            return 300
        elif checklist[3] == enemy and checklist[5] == player and \
                checklist[6] == -1 and checklist[7] == player \
                and checklist[8] == -1:
            return 300
        elif checklist[0] == player and checklist[1] == player and \
                checklist[2] == -1 and checklist[3] == -1 \
                and checklist[5] == enemy:
            return 300
        elif checklist[2] == enemy and checklist[3] == player and \
                checklist[5] == -1 and checklist[6] == -1 \
                and checklist[7] == player:
            return 300
        elif checklist[3] == enemy and checklist[5] == player and \
                checklist[6] == -1 and checklist[7] == -1 \
                and checklist[8] == player:
            return 300
        elif checklist[0] == player and checklist[1] == -1 and \
                checklist[2] == -1 and checklist[3] == player \
                and checklist[5] == enemy:
            return 300
        elif checklist[1] == player and checklist[2] == -1 and \
                checklist[3] == -1 and checklist[5] == player \
                and checklist[6] == enemy:
            return 300
        elif checklist[3] == enemy and checklist[5] == -1 and \
                checklist[6] == -1 and checklist[7] == player \
                and checklist[8] == player:
            return 300
        elif checklist[0] == -1 and checklist[1] == player and \
                checklist[2] == player and checklist[3] == -1 \
                and checklist[5] == enemy:
            return 30
        elif checklist[2] == -1 and checklist[3] == player and \
                checklist[5] == -1 and checklist[6] == player \
                and checklist[7] == enemy:
            return 300
        elif checklist[3] == -1 and checklist[5] == player and \
                checklist[6] == -1 and checklist[7] == player \
                and checklist[8] == enemy:
            return 300
        elif checklist[0] == -1 and checklist[1] == player and \
                checklist[2] == -1 and checklist[3] == player \
                and checklist[5] == enemy:
            return 300
        elif checklist[1] == -1 and checklist[2] == player and \
                checklist[3] == -1 and checklist[5] == player \
                and checklist[6] == enemy:
            return 300
        elif checklist[3] == -1 and checklist[5] == -1 and \
                checklist[6] == player and checklist[7] == player \
                and checklist[8] == enemy:
            return 300
        elif checklist[0] == player and checklist[1] == -1 and \
                checklist[2] == player and checklist[3] == -1 \
                and checklist[5] == enemy:
            return 300
        elif checklist[1] == enemy and checklist[2] == player and \
                checklist[3] == -1 and checklist[5] == -1 \
                and checklist[6] == player:
            return 300
        elif checklist[2] == player and checklist[3] == -1 and \
                checklist[5]== -1 and checklist[6] == player \
                and checklist[7] == enemy:
            return 300
        elif checklist[3] == enemy and checklist[5] == -1 and \
                checklist[6] == player and checklist[7] == -1 \
                and checklist[8] == player:
            return 300
        else:
            return 0

    def willbealive2(self, player, enemy, checklist):
        """下在这个点会形成活二"""
        if checklist[1] == -1 and checklist[2] == -1 and \
                checklist[3] == player and checklist[5] == -1 \
                and checklist[6] == -1:
            return 99
        elif checklist[2] == -1 and checklist[3] == -1 and \
                checklist[5] == player and checklist[6] == -1 \
                and checklist[7] == -1:
            return 99
        elif checklist[0] == -1 and checklist[1] == -1 and \
                checklist[2] == -1 and checklist[3] == player \
                and checklist[5] == -1 and checklist[6] == enemy:
            return 99
        elif checklist[1] == -1 and checklist[2] == -1 and \
                checklist[3] == -1 and checklist[5] == player \
                and checklist[6] == -1 and checklist[7] == enemy:
            return 99
        elif checklist[1] == enemy and checklist[2] == -1 and \
                checklist[3] == player and checklist[5] == -1 \
                and checklist[6] == -1 and checklist[7] == -1:
            return 99
        elif checklist[2] == enemy and checklist[3] == -1 and \
                checklist[5] == player and checklist[6] == -1 \
                and checklist[7] == -1 and checklist[8] == -1:
            return 99
        else:
            return 0

    def willbesleep2(self, player, enemy, checklist):
        """下在这个点会形成眠二"""
        if checklist[2] == enemy and checklist[3] == player and \
                checklist[5] == -1 and checklist[6] == -1 \
                and checklist[7] == -1:
            return 5
        elif checklist[3] == enemy and checklist[5] == player and \
                checklist[6] == -1 and checklist[7] == -1 \
                and checklist[8] == -1:
            return 5
        elif checklist[0] == -1 and checklist[1] == -1 and \
                checklist[2] == -1 and checklist[3] == player \
                and checklist[5] == enemy:
            return 5
        elif checklist[1] == -1 and checklist[2] == -1 and \
                checklist[3] == -1 and checklist[5] == player \
                and checklist[6] == enemy:
            return 5
        elif checklist[1] == enemy and checklist[2] == -1 and \
                checklist[3] == player and checklist[5] == -1 \
                and checklist[6] == -1 and checklist[7] == enemy:
            return 5
        elif checklist[2] == enemy and checklist[3] == -1 and \
                checklist[5] == player and checklist[6] == -1 \
                and checklist[7] == -1 and checklist[8] == enemy:
            return 5
        elif checklist[0] == enemy and checklist[1] == -1 and \
                checklist[2] == player and checklist[3] == -1 \
                and checklist[5] == -1 and checklist[6] == enemy:
            return 5
        elif checklist[2] == enemy and checklist[3] == -1 and \
                checklist[5] == -1 and checklist[6] == player \
                and checklist[7] == -1 and checklist[8] == enemy:
            return 5
        elif checklist[0] == enemy and checklist[1] == -1 and \
                checklist[2] == -1 and checklist[3] == player \
                and checklist[5] == -1 and checklist[6] == enemy:
            return 5
        elif checklist[1] == enemy and checklist[2] == -1 and \
                checklist[3] == -1 and checklist[5] == player \
                and checklist[6] == -1 and checklist[7] == enemy:
            return 5
        elif checklist[0] == -1 and checklist[1] == player and \
                checklist[2] == -1 and checklist[3] == -1 \
                and checklist[5] == enemy:
            return 5
        elif checklist[3] == -1 and checklist[5] == -1 and \
                checklist[6] == -1 and checklist[7] == player \
                and checklist[8] == enemy:
            return 5
        elif checklist[0] == -1 and checklist[1] == -1 and \
                checklist[2] == player and checklist[3] == -1 \
                and checklist[5] == enemy:
            return 5
        elif checklist[2] == -1 and checklist[3] == -1 and \
                checklist[5] == -1 and checklist[6] == player \
                and checklist[7] == enemy:
            return 5
        elif checklist[1] == enemy and checklist[2] == player and \
                checklist[3] == -1 and checklist[5] == -1 \
                and checklist[6] == -1:
            return 5
        elif checklist[3] == enemy and checklist[5] == -1 and \
                checklist[6] == player and checklist[7] == -1 \
                and checklist[8] == -1:
            return 5
        elif checklist[0] == enemy and checklist[1] == player and \
                checklist[2] == -1 and checklist[3] == -1 \
                and checklist[5] == -1:
            return 5
        elif checklist[3] == enemy and checklist[5] == -1 and \
                checklist[6] == -1 and checklist[7] == player \
                and checklist[8] == -1:
            return 5
        else:
            return 0
