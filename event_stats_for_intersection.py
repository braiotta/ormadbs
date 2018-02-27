"""
generates count of records for each "Event" type in overlaps between National and ActionNetwork
"""

from objects.ActionNetwork import ActionNetwork
from objects.National import National
from collections import OrderedDict
import operator

a = ActionNetwork()
a.load()

n = National()
n.load()

overlaps = a.only_email_matches(other_data=n.rows)

events = {}
for row in overlaps:
    event = str(row['event']).strip()
    if event not in events:
        events[event] = 0
    events[event] += 1

events = OrderedDict(sorted(events.items(), key=operator.itemgetter(1), reverse=True))
[print(row, ':', count) for row, count in events.items()]