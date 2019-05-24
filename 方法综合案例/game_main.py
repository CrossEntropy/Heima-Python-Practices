#! /home/panda/miniconda3/envs/tensor/bin/python


class Game(object):

    top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        pass

    @classmethod
    def show_top_score(cls):
        print("当前历史最高分为: %.2f" % cls.top_score)

    def start_name(self):
        pass