"""
A very simple implementation of the wordcount example with a map-reduce.
"""
import time
from pyactor.context import set_context, create_host, serve_forever
from functools import reduce
from collections import Counter
import json


class Executor(object):
    """ Simulates a facade that implements a map and a reduce. So the
        implementations can be easyly redifined.
    """
    _ask = []
    _tell = ['mapper']
    _ref = ['mapper']

    def mapper(self, map_fun, reduce_fun, file, sender):
        res = map_fun(file)
        self.reducer = self.host.lookup_url(sender.get_name(), 'Reducer', 'Server')
        self.reducer.set_dict(res, reduce_fun)


class Reducer(object):
    _tell = ['set_dict', 'set_params']
    _ask = ['get_name', 'get_proxy']
    _ref = ['get_proxy']

    llista = list()
    n_workers = 0
    start = 0

    def set_dict(self, result, reduce_fun):
        self.llista.append(result)
        if(len(self.llista) >= self.n_workers):
            result = reduce(reduce_fun, self.llista)
            with open('nouDiccF4.txt', 'w') as f:
                f.write(json.dumps(result))
            print("--- %s seconds ---" % (time.time() - self.start))

    def get_name(self):
        return "http://127.0.0.1:1679/reducer1"

    def get_proxy(self):
        return self.proxy

    def set_params(self, workers, time):
        self.n_workers = workers
        self.start = time


def merge(dict1, dict2):
    return Counter(dict1) + Counter(dict2)


def reduce_count(count1, count2):
    return count1 + count2


def mapper2(line):
    """ Map function definition. Splits the lines and generates key-value for
        each word.
    """
    counts = {}
    line = line.lower()
    line = line.replace('.', '').replace(',', '').replace(':', '').replace(
        '"', '').replace('#', '')
    words = line.split()
    for word in words:
        global aval
        aval = aval + 1
        counts[word] = counts.get(word, 0) + 1
    return counts


def mapper3(file):
    with open(file) as f:
        lines = f.readlines()
    countWord = 0
    for line in lines:
        line = line.lower()
        line = line.replace('.', '').replace(',', '').replace(':', '').replace(
            '"', '').replace('#', '')
        words = line.split()
        for word in words:
            countWord = countWord + 1
    return countWord


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')
    local_host = host.spawn('reducer1', 'Server/Reducer')
    print(local_host)
    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry',
                               'Registry')

    remote_host = registry.lookup('host1')
    remote_host2 = registry.lookup('host2')
    remote_host3 = registry.lookup('host3')
    remote_host4 = registry.lookup('host4')
    remote_host5 = registry.lookup('host5')
    print(remote_host)
    print(remote_host2)
    print(remote_host3)
    print(remote_host4)
    print(remote_host5)
    n_workers = 5
    path_fitxer = "/projects/SD/Prac1/Proves/big2.txt"
    start_time = time.time()
    local_host.set_params(n_workers, start_time)
    server = remote_host.spawn('server', 'Server/Executor')
    server.mapper(mapper2, merge, path_fitxer, local_host.get_proxy())

    server2 = remote_host2.spawn('server2', 'Server/Executor')
    server2.mapper(mapper2, merge, path_fitxer, local_host.get_proxy())

    server3 = remote_host3.spawn('server3', 'Server/Executor')
    server3.mapper(mapper2, merge, path_fitxer, local_host.get_proxy())

    server4 = remote_host4.spawn('server4', 'Server/Executor')
    server4.mapper(mapper2, merge, path_fitxer, local_host.get_proxy())

    server5 = remote_host5.spawn('server5', 'Server/Executor')
    server5.mapper(mapper2, merge, path_fitxer, local_host.get_proxy())

    serve_forever()
