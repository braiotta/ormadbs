class DataSource:
    source_dir = './sources'

    def __init__(self):
        self.rows = []

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

    @staticmethod
    def pad_zip(zip):
        return zip.rjust(5, '0')