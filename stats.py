import json
import csv
import sys
from collections import Counter
from pprint import pprint

class bdStatsClasses(object):

    def load_csv(self, filepath):
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            self.raw_data = list(reader)

    def mean(self, numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

    def stats(self):
        m = 0
        c = Counter()
        for i in self.raw_data:
            items = i['Technologies']
            item = items.split("\n")
            item = [ x.lower() for x in item ]
            m = self.mean([m, len(item)])
            c2 = Counter(item)
            c += c2

        res = { 
                "techonologies": c,
                'total_count': len(self.raw_data),
                'average_roles': m
                }
        self.result = res
        return res

    def create_domain_json(self, dname):
        tmp = {}
        for i in self.raw_data:
            name = i['Dataset']
            url = i['Dataset URL']
            tmp[name] = url

        res = {
                dname: {
                    'categories': {
                        'bigdataclass': tmp
                        }
                    }
                }

        return res

    def save_json(self, filename, data):
        with open(filename, 'w') as f:
            json.dump(data, f)
        f.close()

    def stats_two(self):
        """for fall 15 csv files"""
        """where id, title, technology*, user interface language, backend
        environment, dataset, github url, dataset url"""

        m = 0
        c = Counter()
        for i in self.raw_data:
            items = i['Technology*']
            item = items.split("\n")
            item = [ x.lower() for x in item ]
            m = self.mean([m, len(item)])
            c2 = Counter(item)
            c += c2

            lang = i['User Interface Language']
            env = i['Backend Environment**']
            data = i['Dataset URL']

        res = { 
                "techonologies": c,
                'total_count': len(self.raw_data),
                'average_roles': m
                }
        self.result = res
        return res


if __name__ == "__main__":

    stat = bdStatsClasses()
    stat.load_csv(sys.argv[1])
    #res = stat.stats()
    #pprint (res)
    res = stat.create_domain_json('fall15')
    stat.save_json('fall15.json', res)
