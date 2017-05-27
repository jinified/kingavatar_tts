#!/usr/bin/env python
import time
import sys
import codecs
import os
import multiprocessing as mp
from gtts import gTTS

BASE = '/home/parapa/Desktop/speakchinese/out/'

def tts(idx):
    idx = idx.rstrip('\n')
    rawtext = '{}{}.txt'.format(BASE, idx)
    mp3 = '{}{}.mp3'.format(BASE, idx)
    print(rawtext)
    with codecs.open(rawtext, encoding='utf8') as f:
        # Read content of file as unicodes
        content = f.read()
        speech = gTTS(content, idx, lang='zh-cn')
        speech.save(mp3)
    return idx



def parallel_extract(content):
    pool = mp.Pool()
    results = pool.map(tts, content)
    pool.close()
    pool.join()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], 'r') as f:
                content = f.readlines()
                parallel_extract(content)
        else:
            tts(sys.argv[1])
    else:
        parallel_extract(map(str, range(1753, 1758)))
