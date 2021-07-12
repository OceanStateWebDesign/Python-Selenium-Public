import sys
import os

from twocaptcha import TwoCaptcha

solver = TwoCaptcha('09fd33978408d2c34d665d037e79e20a')
result = solver.normal('./CapTest.png')
goodresult = result.str.split(',')

print(goodresult);
