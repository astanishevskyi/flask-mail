import sys
from email import policy

PY3 = sys.version_info[0] == 3

PY34 = PY3 and sys.version_info[1] >= 4

string_types = str
text_type = str

message_policy = policy.SMTP
