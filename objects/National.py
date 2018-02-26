from objects.DataSource import DataSource


class National(DataSource):
    file_name = 'or-national.csv'

    col_map = {
        "first_name": "First Name",
        "last_name": "Last Name",
        "city": "City",
        "zip": "Zip",
        "county": "County",
        "congressional_district": "Congressional District",
        "state_house_district": "State House District",
        "state_senate_district": "State Senate District",
        "email": "Email",
        "home_phone": "Home Phone",
        "work_phone": "Work Phone",
        "mobile_phone": "Mobile Phone"
    }

    def __init__(self):
        super().__init__()

    @staticmethod
    def derive_address(row):
        addr = []
        addr_cols = ['Address 1', 'Address 2']
        for addr_col in addr_cols:
            if addr_col in row and len(row[addr_col]) > 0:
                addr.append(row[addr_col])

        return "\n".join(addr)