import  datetime,time

def compressOld_str(string):
    count = 0
    result = ''
    current = string[0]

    for ch in string[1:]:
        if ch == current:
            count += 1
        else:
            result += current + str(count)
            current = ch
            count = 1

    result += current + str(count)

    if len(result)> len(string):
            return string

    return result

def compressNew_str(string):
    result = []
    count = 1
    current = string[0]

    for ch in string[1:]:
        if ch == current:
            count += 1
        else:
            result.append(current)
            result.append(str(count))
            count = 1
            current = ch

    result.append(current)
    result.append(str(count))
    if len(result) >= len(string):
        return string
    return ''.join(result)

start = time.clock()
print(compressOld_str('abbbaaabbbccccc'))
end = time.clock()
print('Time of old compress method is '+str(end-start))

start = time.clock()
print(compressNew_str('abbbaaabbbccccc'))
end = time.clock()
print('Time of new compress method is '+str(end-start))

