from pyactor.context import set_context, create_host, serve_forever
from collections import Counter


def mapper2(file):
    """ Map function definition. Splits the lines and generates key-value for
        each word.
    """
    with open(file) as f:
        lines = f.readlines()
    counts = {}
    for line in lines:
        line = line.lower()
        line = line.replace('.', '').replace(',', '').replace(':', '').replace(
            '"', '').replace('#', '')
        words = line.split()
        for word in words:
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


def merge(dict1, dict2):
    return Counter(dict1) + Counter(dict2)


def reduce_count(count1, count2):
    return count1 + count2


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1284/')

    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry',
                               'Registry')

    registry.bind('host4', host)

    print('host listening at port 1284')

    serve_forever()
