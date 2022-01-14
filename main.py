#!/usr/bin/env python3
#
# MIT License
#
# Copyright (c) 2022 Kovács József Miklós <kovacsjozsef7u@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import re
import os
import sys
import json
import urllib.request
import urllib.parse

def fix_text(text):
    text = text.replace(r'\n', '')
    text = text.replace(r'\N', '')
    # remove { foobar foobar }
    text = re.sub('{.*?}', '', text)
    return text

def read_deepL_API_key():
    if not os.path.exists('deepL.txt'):
        print('deepL.txt not exist')
        sys.exit(1)
    with open('deepL.txt', 'r') as f:
        # TODO: check?
        return f.readline().strip()

def translate_deepL(text, deepL_API_key, target_lang):
    headers = {
        'User-Agent': 'TrashSub',
        'Host': 'api-free.deepl.com'
    }
    data = {
        'auth_key': deepL_API_key,
        'text': text,
        'target_lang': target_lang
    }
    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request('https://api-free.deepl.com/v2/translate?auth_key=' + deepL_API_key, headers=headers, data=data)
    resp = urllib.request.urlopen(req).read()
    resp = json.loads(resp)

    return resp['translations'][0]['text']

def main():
    deepL_API_key = read_deepL_API_key()
    target_lang = 'HU'

    dialogues = []

    # TODO: better solution?
    filename = 'input.ass'
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Dialogue: '):
                line = line.split(',')
                line = ''.join(line[9:])
                dialogues.append(line)

    for index, dialogue in enumerate(dialogues):
        d = fix_text(dialogue)

        print(f'Line {index+1}')
        print(d)
        print(translate_deepL(d, deepL_API_key, target_lang))

        # empty line
        print()

if __name__ == '__main__':
    main()
