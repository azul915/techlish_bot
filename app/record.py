# coding: utf-8

class Record:
    def __init__(self, num, word, category, mean, supplement, created_at):
        self.num = num
        self.word = word
        self.category = category
        self.mean = mean
        self.supplement = supplement
        self.created_at = created_at

    def __str__(self):
        return "num: {num} word: {word} category: {category} mean: {mean} supplement: {supplement} created_at: {created_at}".format(num=self.num, word=self.word, category=self.category, mean=self.mean, supplement=self.supplement, created_at=self.created_at)
