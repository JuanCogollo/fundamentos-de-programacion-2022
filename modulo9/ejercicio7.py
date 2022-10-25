def to_camel_case(str_):
    name = str_.split('_')
    camel_case = ''
    for word in name:
        capitalized = ''
        for i in range(len(word)):
            if i == 0:
                capitalized += word[i].capitalize()
            else:
                capitalized += word[i]
        camel_case += capitalized
    return camel_case


def main():
    n = int(input())
    for i in range(n):
        name = input()
        print(to_camel_case(name))


main()
