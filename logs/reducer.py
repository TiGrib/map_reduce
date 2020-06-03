import sys


def do_reduce(module, values):
    return module, sum(values)


prev_key = None
values = []


for line in sys.stdin:
    key, value = line.split("\t")
    if key != prev_key and prev_key is not None:
        result_key, result_value = do_reduce(prev_key, values)
        print(f'{result_key}    {str(result_value)}')
        values = []

    prev_key = key
    values.append(int(value))

if prev_key is not None:
    result_key, result_value = do_reduce(prev_key, values)
    print(f'{result_key}   {str(result_value)}')
