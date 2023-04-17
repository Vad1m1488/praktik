def common_chars(с):
    common = set(с[0])
    for i in с[1:]:
        common &= set(i)
    result = list(common)
    result.sort(key = lambda x: [i.count(x) for i in с])
    return result

с = ["cool", "lock", "cook"]
result = common_chars(с)
print(result)