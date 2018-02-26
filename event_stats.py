"""
generates count of records for each "Event" type
"""

from objects.ActionNetwork import ActionNetwork
from collections import OrderedDict
import operator

a = ActionNetwork()
a.load()

events = {}
for row in a.rows:
    event = str(row['event']).strip()
    if event not in events:
        events[event] = 0
    events[event] += 1

events = OrderedDict(sorted(events.items(), key=operator.itemgetter(1), reverse=True))
[print(row, ':', count) for row, count in events.items()]