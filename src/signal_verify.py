# -*- coding:utf-8 -*-
# ------------------------
# File: signal_verify
# Author: changqingai
# Date: 2019.01.09
# ------------------------

import signal


def sig_tstp():

    def handler(signum, frame):
        print('I received: ', signum)

    signal.signal(signal.SIGTSTP, handler)
    signal.pause()
    print('end of signal demo')


if __name__ == "__main__":
    sig_tstp()
