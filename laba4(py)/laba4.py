class String:

    def Set(self, phrase = input()):
        print('Исходная строка: {}'.format(phrase))
        self.presentPhrase = phrase

        if len(phrase) % 2 == 0:
            self.L = phrase[2:(len(phrase) - 2)]
            print('Строка после преобразований:', self.L)
            return self.L

        else:
            self.L = phrase
            print('Строка после преобразований:', self.L, '(ничего не изменилось)')
            return self.L

    def print(self):
        return self.presentPhrase


line = String()
line.Set()
line.print()

file_input = open('input_textLab4.txt', 'w')
file_input.write(line.print())
file_input.close()


file_output = open('output_textLab4.txt', 'w')
file_output.write(line.Set())
file_output.close()
