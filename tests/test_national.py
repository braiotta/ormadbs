import unittest.mock
from objects.National import National
from objects.DataSource import DataSource


def return_national_load(*args, **kwargs):
    rows = [
        {"City": 'Boston', 'Employer': '', 'Zip': '2134', 'Occupation': '', 'Prefix': '', 'Address 2': 'Apt 123',
         'Email': 'LIBsnowflake@gmail.com', 'Work Phone': '6175551212', 'Last Name': 'Snowflake',
         'First Name': 'Libby', 'Unique Constituent ID': '12345', 'Congressional District': 'MA1',
         'Status': 'Non-Donor', 'Subsource': '', 'Mobile Phone Opt-In': '', 'Join Date': '2018-02-03 23:52:05 EST',
         'Source': 'main-nav-join', 'Address 1': '123 Fake St', '\ufeffState': 'MA', 'Suffix': '',
         'Mobile Phone': '6175552222', 'Fax': '', 'County': 'Middlesex', 'Home Phone': '6175553333', 'Gender': '',
         'State House District': 'MA2', 'Country': 'US', 'Membership Card': 'No', 'State Senate District': 'MA3',
         'Middle Name': 'Gorn'},
        {"City": 'Cambridge', 'Employer': '', 'Zip': '2345', 'Occupation': '', 'Prefix': '', 'Address 2': 'Apt 345',
         'Email': 'agentprovocateur@gmail.com', 'Work Phone': '6175559876', 'Last Name': 'Provocateur',
         'First Name': 'Agent', 'Unique Constituent ID': '9876', 'Congressional District': 'MA9',
         'Status': 'Non-Donor', 'Subsource': '', 'Mobile Phone Opt-In': '', 'Join Date': '2018-02-03 23:52:05 EST',
         'Source': 'main-nav-join', 'Address 1': '987 Fake St', '\ufeffState': 'MA', 'Suffix': '',
         'Mobile Phone': '6175558765', 'Fax': '', 'County': 'Middlesex', 'Home Phone': '6175557654', 'Gender': '',
         'State House District': 'MA8', 'Country': 'US', 'Membership Card': 'No', 'State Senate District': 'MA7',
         'Middle Name': ''}
    ]

    return rows


class NationalTestCase(unittest.TestCase):
    def test_derive_address(self):
        raw_row = {"City": 'Boston', 'Employer': '', 'Zip': '2134', 'Occupation': '', 'Prefix': '',
                   'Address 2': 'Apt 123',
                   'Email': 'libsnowflake@gmail.com', 'Work Phone': '6175551212', 'Last Name': 'Snowflake',
                   'First Name': 'Libby', 'Unique Constituent ID': '12345', 'Congressional District': 'MA1',
                   'Status': 'Non-Donor', 'Subsource': '', 'Mobile Phone Opt-In': '',
                   'Join Date': '2018-02-03 23:52:05 EST',
                   'Source': 'main-nav-join', 'Address 1': '123 Fake St', '\ufeffState': 'MA', 'Suffix': '',
                   'Mobile Phone': '6175552222', 'Fax': '', 'County': 'Middlesex', 'Home Phone': '6175553333',
                   'Gender': '',
                   'State House District': 'MA2', 'Country': 'US', 'Membership Card': 'No',
                   'State Senate District': 'MA3',
                   'Middle Name': 'Gorn'}
        addr = National.derive_address(row=raw_row)
        self.assertEqual("123 Fake St\nApt 123", addr)

    def test_map_row(self):
        raw_row = {"City": 'Boston', 'Employer': '', 'Zip': '2134', 'Occupation': '', 'Prefix': '', 'Address 2': 'Apt 123',
               'Email': 'libsnowflake@gmail.com', 'Work Phone': '6175551212', 'Last Name': 'Snowflake',
               'First Name': 'Libby', 'Unique Constituent ID': '12345', 'Congressional District': 'MA1',
               'Status': 'Non-Donor', 'Subsource': '', 'Mobile Phone Opt-In': '', 'Join Date': '2018-02-03 23:52:05 EST',
               'Source': 'main-nav-join', 'Address 1': '123 Fake St', '\ufeffState': 'MA', 'Suffix': '',
               'Mobile Phone': '6175552222', 'Fax': '', 'County': 'Middlesex', 'Home Phone': '6175553333', 'Gender': '',
               'State House District': 'MA2', 'Country': 'US', 'Membership Card': 'No', 'State Senate District': 'MA3',
               'Middle Name': 'Gorn'}

        n = National()
        row = n.map_row(row=raw_row)
        self.assertEqual(
            {'last_name': 'Snowflake', 'congressional_district': 'MA1', 'email': 'libsnowflake@gmail.com',
             'first_name': 'Libby', 'mobile_phone': '6175552222', 'state_senate_district': 'MA3', 'zip': '02134',
             'address': '123 Fake St\nApt 123', 'county': 'Middlesex', 'home_phone': '6175553333',
             'state_house_district': 'MA2', 'city': 'Boston', 'work_phone': '6175551212'},
            row
        )

    def test_map_row_lowercases_email(self):
        raw_row = {"City": 'Boston', 'Employer': '', 'Zip': '2134', 'Occupation': '', 'Prefix': '',
                   'Address 2': 'Apt 123',
                   'Email': 'LIBsnowflake@gmail.com', 'Work Phone': '6175551212', 'Last Name': 'Snowflake',
                   'First Name': 'Libby', 'Unique Constituent ID': '12345', 'Congressional District': 'MA1',
                   'Status': 'Non-Donor', 'Subsource': '', 'Mobile Phone Opt-In': '',
                   'Join Date': '2018-02-03 23:52:05 EST',
                   'Source': 'main-nav-join', 'Address 1': '123 Fake St', '\ufeffState': 'MA', 'Suffix': '',
                   'Mobile Phone': '6175552222', 'Fax': '', 'County': 'Middlesex', 'Home Phone': '6175553333',
                   'Gender': '',
                   'State House District': 'MA2', 'Country': 'US', 'Membership Card': 'No',
                   'State Senate District': 'MA3',
                   'Middle Name': 'Gorn'}
        n = National()
        row = n.map_row(row=raw_row)
        self.assertEqual(raw_row['Email'].lower(), row['email'])

    def test_map_row_zeropads_zip(self):
        raw_row = {"City": 'Boston', 'Employer': '', 'Zip': '2134', 'Occupation': '', 'Prefix': '',
                   'Address 2': 'Apt 123',
                   'Email': 'LIBsnowflake@gmail.com', 'Work Phone': '6175551212', 'Last Name': 'Snowflake',
                   'First Name': 'Libby', 'Unique Constituent ID': '12345', 'Congressional District': 'MA1',
                   'Status': 'Non-Donor', 'Subsource': '', 'Mobile Phone Opt-In': '',
                   'Join Date': '2018-02-03 23:52:05 EST',
                   'Source': 'main-nav-join', 'Address 1': '123 Fake St', '\ufeffState': 'MA', 'Suffix': '',
                   'Mobile Phone': '6175552222', 'Fax': '', 'County': 'Middlesex', 'Home Phone': '6175553333',
                   'Gender': '',
                   'State House District': 'MA2', 'Country': 'US', 'Membership Card': 'No',
                   'State Senate District': 'MA3',
                   'Middle Name': 'Gorn'}
        n = National()
        row = n.map_row(row=raw_row)
        self.assertEqual('0' + raw_row['Zip'], row['zip'])

    @unittest.mock.patch.object(DataSource, 'load_file', side_effect=return_national_load)
    def test_load(self, load_file):
        n = National()
        n.load()
        self.assertEqual(
            [{'zip': '02134', 'address': '123 Fake St\nApt 123', 'congressional_district': 'MA1', 'first_name': 'Libby',
              'city': 'Boston', 'mobile_phone': '6175552222', 'state_house_district': 'MA2',
              'email': 'libsnowflake@gmail.com', 'last_name': 'Snowflake', 'state_senate_district': 'MA3',
              'county': 'Middlesex', 'home_phone': '6175553333', 'work_phone': '6175551212'},
             {'zip': '02345', 'address': '987 Fake St\nApt 345', 'congressional_district': 'MA9', 'first_name': 'Agent',
              'city': 'Cambridge', 'mobile_phone': '6175558765', 'state_house_district': 'MA8',
              'email': 'agentprovocateur@gmail.com', 'last_name': 'Provocateur', 'state_senate_district': 'MA7',
              'county': 'Middlesex', 'home_phone': '6175557654', 'work_phone': '6175559876'}],
            n.rows
        )