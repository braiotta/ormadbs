from objects.National import National
from objects.ActionNetwork import ActionNetwork

# load our two data sources
a = ActionNetwork()
a.load()

n = National()
n.load()

# minus email matches
national_minus_email_matches = n.minus_email_matches(old_data=a)
print(national_minus_email_matches)
# create a csv upload for action network
a_upload = ActionNetwork()
a_upload.feed(rows=national_minus_email_matches)
print(a_upload.to_csv())

# minus lname matches, fname1 in fname2 or vice versa
# minus lname matches, fname1 and fname2 have same first initial