import textwrap

def wrap(string, max_width):
    my_wrap = textwrap.TextWrapper(width = max_width)
    return my_wrap.fill(text=string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)