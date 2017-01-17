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

    def separate_item(self, items):
        item = items.split("\n")
        if len(item) == 1:
            item = item[0].split(",")
        item = [ x.strip() for x in item ]
        item = [ x.lower() for x in item ]
        return item

    def stats_two(self):
        """for fall 15 csv files"""
        """where id, title, technology*, user interface language, backend
        environment, dataset, github url, dataset url"""

        m = 0
        c = Counter()
        for i in self.raw_data:
            item = self.separate_item(i['Technology*'])
            lang = self.separate_item(i['User Interface Language'])
            env = self.separate_item(i['Backend Environment**'])
            tech = item + lang + env
            m = self.mean([m, len(tech)])
            c2 = Counter(tech)
            c += c2

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
    #res = stat.create_domain_json('fall15')
    #stat.save_json('fall15.json', res)
    res = stat.stats_two()
    pprint (res)
