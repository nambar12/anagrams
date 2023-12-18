import string
import random


class AnagramsGenerator:

    def __init__(self):
        pass

    @staticmethod
    def generate_random_string(length):
        # Characters to choose from: lowercase, uppercase letters and digits
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def scramble_string(s):
        char_list = list(s)
        random.shuffle(char_list)
        return ''.join(char_list)

    def generate_one(self, length, size):
        generated_str = self.generate_random_string(length)
        return [self.scramble_string(generated_str) for _ in range(size)]

    def generate_one_range(self, length, size):
        generated_str = self.generate_random_string(random.randint(1, length))
        return [self.scramble_string(generated_str) for _ in range(random.randint(1, size))]

    def generate_full(self, amount, length, size):
        result = []
        generated_strs = [self.generate_random_string(length) for _ in range(random.randint(1, amount))]
        for generated_str in generated_strs:
            result.extend([self.scramble_string(generated_str) for _ in range(random.randint(1, size))])
        random.shuffle(result)
        return result
