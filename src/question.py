import importlib


class Question:
    def __init__(self, item):
        self.question = item['question']
        self.answers = item['answer']
        self.correct = ''
        self.cost = item['cost']
        self.index = 0

    def execute(self,function_string,param):
        mod_name, func_name = function_string.rsplit('.',1)
        mod = importlib.import_module(mod_name)
        func = getattr(mod, func_name)
        result = func(*param.split(';'))
        self.correct = result
        self.question = self.question.format(*param.split(';'))

    def shuffle(self):
        import random
        indices = list(range(len(self.answers)))
        z_list = list(zip(indices, self.answers))
        random.shuffle(z_list)
        indices, self.answers = zip(*z_list)
        self.correct = chr(ord('A') + indices.index(0))
