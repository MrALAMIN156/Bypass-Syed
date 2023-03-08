import os, sys

try:

    __import__("Syed").main()

except Exception as e:

    exit(str(e))
