class DataSource:
    source_dir = './sources'

    def __init__(self):
        self.rows = []

    def feed(self, rows):
        self.rows = rows

    def load(self):
        [self.rows.append(self.map_row(row)) for row in self.load_file()]

    def load_file(self):
        import csv
        rows = csv.DictReader(open(self.source_dir + '/' + self.file_name))
        return rows

    def map_row(self, row):
        new_row = {}

        for key, csv_name in self.col_map.items():
            val = row[csv_name]
            new_row[key] = val

        try:
            new_row['address'] = self.derive_address(row)
        except AttributeError:
            pass

        new_row['zip'] = DataSource.pad_zip(zip=new_row['zip'])

        return new_row

    def minus_email_matches(self, old_data):
        # compile a dict of all emails in old data
        old_emails = {thedict['email']:1 for thedict in [row for row in old_data]}

        # for every row in new data, pass it on if the email doesn't exist in dict of old_email data
        combed_data = [row for row in self.rows if row['email'] not in old_emails]

        return combed_data

    def to_csv(self):
        import csv
        import io
        output = io.StringIO()

        csv_data = []

        # update all keys to reflect output key names
        for row in self.rows:
            new_row = {}
            for k, v in row.items():
                new_k = self.col_map[k]
                new_row[new_k] = v
            csv_data.append(new_row)

        # return output
        str_output = ""
        with output:
            writer = csv.DictWriter(output, fieldnames=self.csv_order)
            writer.writeheader()
            for row in csv_data:
                writer.writerow(row)

            str_output = output.getvalue()

        return str_output

    @staticmethod
    def pad_zip(zip):
        return zip.rjust(5, '0')