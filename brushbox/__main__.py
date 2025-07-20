import sys
import brushbox
from .TokenExcecpion import TokenException
args=sys.argv[1:]
try:
    for i in range(int(args[3])):
        brushbox.send_message(args[0],args[1],args[2])
except TokenException:
    print("[Error] Token过期")
except:
    print("使用方式:python -m brushbox [token] [内容] [群id] [次数]")