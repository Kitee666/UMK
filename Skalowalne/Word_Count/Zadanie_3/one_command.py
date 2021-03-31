#!/usr/bin/env python3
import os
import sys

os.system("cat " + sys.argv[1] + " | python3 map.py | sort | python3 reduce.py")
