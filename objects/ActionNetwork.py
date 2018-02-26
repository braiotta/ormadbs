from objects.DataSource import DataSource


class ActionNetwork(DataSource):
    file_name = 'or-actionnetwork.csv'

    col_map = {
        "first_name": "first_name",
        "last_name": "last_name",
        "zip": "zip_code",
        "email": "email",
        'ward_precinct': 'Ward/PrecinctName',
        'vanid': "VoterVANID"
    }

    def __init__(self):
        super().__init__()