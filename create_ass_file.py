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

# TODO: write a better script

def main() -> None:
    dialogues = []

    with open('output.txt', 'r') as f:
        count = 0
        for line in f:
            line = line.strip()
            if line == '':
                continue
            count += 1
            if count == 3:
                count = 0
                dialogues.append(line)

    with open('input.ass', 'r') as inpf:
        i = 0
        for line in inpf:
            line = line.strip()
            if line.startswith('Dialogue: '):
                line = line.split(',')
                line = ','.join(line[:9])
                print(line + ',' + dialogues[i])
                i += 1
            else:
                print(line)

if __name__ == '__main__':
    main()
