import subprocess
from PIL import Image
import os
import re

# name="20211218 ワールドワイドワンダー MORE MORE JUMP！ × KAITO "
# os.rename(f"yt-dlp/out.mp3", f"yt-dlp/{name} .mp3")

class Shuzokuchi():
    def __init__(self,s):
        self.sum=s

    def __gt__(self,other):
        return self.sum>other.sum

s1=Shuzokuchi(120)
s2=Shuzokuchi(100)

print(s1>s2)
print(s1.__gt__(s2)) #s1>s2と同じ意味
print(Shuzokuchi.__gt__(s1,s2))  #s1>s2と同じ意味
