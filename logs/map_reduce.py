
def map(record):
    split_record = record.split(" ")
    virtual_machine = " ".join(split_record[0:3])
    date = " ".join(split_record[4:7])
    request = split_record[7]
    module = " ".join(split_record[8:10])
    status = split_record[10]

    if status == '200':
        yield module, 1


def reduce(module, value):
    yield module, sum(value)

