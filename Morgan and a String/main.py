def solution(a,b):
    result = ''
    a += 'z'
    b += 'z'
    for i in range(len(a) + len(b) -2):
        if(a < b):
            yield a[0]
            a = a[1:]
        else:
            yield b[0]
            b = b[1:]

def morganAndString(a,b):
    return "".join(solution(a,b))

if __name__ == "__main__":
    a = 'BAB'
    b = 'BAC'
    # a = 'JACK'
    # b = 'DANIEL'
    # a = 'ABACABA'
    # b = 'ABACABA'
    print(morganAndString(a, b))
    		