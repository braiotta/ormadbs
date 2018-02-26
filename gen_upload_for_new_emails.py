"""
takes National data and Action Network data, figures out which rows in National data have an email address not present
in existing Action Network data, and creates a CSV upload
"""

from objects.National import National
from objects.ActionNetwork import ActionNetwork

# load our two data sources
a = ActionNetwork()
a.load()

n = National()
n.load()

# minus email matches
national_minus_email_matches = n.minus_email_matches(old_data=a.rows)

# create a csv upload for action network based removing those with matching email
a_upload = ActionNetwork()
a_upload.feed(rows=national_minus_email_matches)
print(a_upload.to_csv())