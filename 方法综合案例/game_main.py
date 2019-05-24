#! /home/panda/miniconda3/envs/tensor/bin/python


class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息: 让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("当前历史最高分为: %.2f" % cls.top_score)

    def start_name(self):
        print("%s 开始游戏啦..." % self.player_name)


if __name__ == "__main__":
    Game.show_help()
    Game.show_top_score()
    game = Game("小明")
    game.start_name()