from example import get_dups
import os
import string
import random
import json


class Metavault:

    def __init__(self, database, file):
        self.database = database
        self.file = file

    def connnection(self) -> str:
        try:
            os.mkdir(self.database)
            self.file = self.database + '/' + self.file
            if not self.file.endswith('.json'):
                self.file = self.file + ".json"
                # If the file is not a json file but a text file this would be
                # immediatly changed to a json
            else:
                pass
            f = open(self.file, 'xt')
            f.write('{}')
            # This would create an empty object
            f.close()
            return True
        except FileExistsError or FileNotFoundError:
            pass

    def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def find_files(filename, search_path=os.path.dirname(
            os.path.abspath("top_level_file.txt")
        )
    ):
        result = []
        for root, dir, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))

            # This would find the file path for the filename
            # This would then be used for the self arguement which hold
            # the database and filename

        result = str(result)
        unwanted = '[]'
        for x in unwanted:
            result = result.replace(x, '')
        result = result.strip("''")

        # This removes any extra quotations
        return result

    def get_dups(a, values=None):
        if values is None: values = []
        if (a in values): return True
        values.append(a)
        if type(a) == dict:
            for i, y in a.items():
                if (get_dups(y, values=values)):
                    del a[i]
                    return i
        return False

    def insert_object(self, args):
        try:
            path = Metavault.find_files(self.file)
            with open(path, 'rt') as f:
                value = f.read()
                value = eval(value)
                f.close()

                # I would have thought that it should be a number that would
                # keep track of the nested objects
                # Its just gonna have to be random, as it's easier

            with open(path, 'wt') as f:
                key = Metavault.id_generator(12)
                value.update({key: args})
                value = json.dumps(value)
                get_dups(value)
                f.write(value)
            print(value)
        except FileNotFoundError:
            pass


