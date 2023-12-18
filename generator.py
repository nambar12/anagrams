from generator.anagrams_generator import AnagramsGenerator


def anagrams():
    generator = AnagramsGenerator()
    list = generator.generate_full(5, 1000000, 25)
    for item in list:
        print(item)


if __name__ == '__main__':
    anagrams()


