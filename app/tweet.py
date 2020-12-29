# coding: utf-8

import logging

class Tweet:
    def __init__(self, content={}):
            formatted_content = '''\
{word}({category}): {mean}
{supplement}
#SoftwareEnglish
\
'''.format(word=content.word, category=content.category, mean=content.mean, supplement=content.supplement)
            self.content = {"status": formatted_content}
