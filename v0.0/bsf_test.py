import ast

code = """
import os, sys
from collections import deque
import numpy as np
"""

tree = ast.parse(code)

print(tree)
