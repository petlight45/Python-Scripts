import subprocess
from subprocess import PIPE
import re
import datetime
from dateutil.parser import parse


obj = subprocess.Popen("net stats workstation",stdout=PIPE)
output = str(obj.communicate())
time_string = re.search(r"Statistics since ([\d/:\s]+(PM|AM)*)",output).group(1)
print(time_string)
print(datetime.datetime.today() - parse(time_string))