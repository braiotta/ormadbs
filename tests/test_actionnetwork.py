import unittest.mock
from objects.ActionNetwork import ActionNetwork
from objects.DataSource import DataSource


def return_national_load(*args, **kwargs):
    rows = [
        {'last_name': 'Snowflake', 'zip_code': '1234', 'first_name': 'Libby', 'Ward/PrecinctName': 'MA1',
         'email': 'libsnowflake@gmail.com', 'VoterVANID': '999'},
        {'last_name': 'Provocateur', 'zip_code': '2345', 'first_name': 'Agent', 'Ward/PrecinctName': 'MA2',
         'email': 'agentprovocateur@gmail.com', 'VoterVANID': '888'}
    ]

    return rows

class ActionNetworkTestCase(unittest.TestCase):
    def test_map_row(self):
        raw_row = {'last_name': 'Snowflake', 'zip_code': '1234', 'first_name': 'Libby', 'Ward/PrecinctName': 'MA1',
         'email': 'libsnowflake@gmail.com', 'VoterVANID': '999'}

        n = ActionNetwork()
        row = n.map_row(row=raw_row)

        print(row)

        self.assertEqual(
            {'zip': '01234', 'last_name': 'Snowflake', 'first_name': 'Libby', 'email': 'libsnowflake@gmail.com',
             'ward_precinct': 'MA1', 'vanid': '999'},
            row
        )

    @unittest.mock.patch.object(DataSource, 'load_file', side_effect=return_national_load)
    def test_load(self, load_file):
        n = ActionNetwork()
        n.load()

        self.assertEqual(
            [{'zip': '01234', 'ward_precinct': 'MA1', 'email': 'libsnowflake@gmail.com', 'first_name': 'Libby',
              'last_name': 'Snowflake', 'vanid': '999'},
             {'zip': '02345', 'ward_precinct': 'MA2', 'email': 'agentprovocateur@gmail.com', 'first_name': 'Agent',
              'last_name': 'Provocateur', 'vanid': '888'}],
            n.rows
        )

    @unittest.mock.patch.object(DataSource, 'load_file', side_effect=return_national_load)
    def test_to_csv(self, load_file):
        n = ActionNetwork()
        n.load()
        csv = n.to_csv()
        self.assertEqual(
            "first_name,last_name,email,zip_code,ORMA Supporter,VoterVANID,Ward/PrecinctName,Zip\r\nLibby,Snowflake,libsnowflake@gmail.com,01234,,999,MA1,\r\nAgent,Provocateur,agentprovocateur@gmail.com,02345,,888,MA2,\r\n",
            csv
        )

    @unittest.mock.patch.object(DataSource, 'load_file', side_effect=return_national_load)
    def test_minus_old_emails(self, load_file):
        n = ActionNetwork()
        n.load()

        old_data = [
            {'first_name': 'Henry', 'last_name': 'Kissinger', 'email': 'hk@clinton.org'},
            {'zip': '01234', 'ward_precinct': 'MA1', 'email': 'libsnowflake@gmail.com', 'first_name': 'Libby',
             'last_name': 'Snowflake', 'vanid': '999'}
        ]

        # Libby Snowflake exists in the old data and the new. Expect to see her gone.
        combed = n.minus_email_matches(old_data=old_data)
        self.assertEqual(
            [{'last_name': 'Provocateur', 'first_name': 'Agent', 'email': 'agentprovocateur@gmail.com', 'vanid': '888',
              'zip': '02345', 'ward_precinct': 'MA2'}],
            combed
        )