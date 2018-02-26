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
#print(len(a_upload.rows))

# minus lname matches, fname1 in fname2 or vice versa
# minus lname matches, fname1 and fname2 have same first initial