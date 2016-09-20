import sublime, sublime_plugin, string
from random import sample, choice, randrange

class PasswordCommand(sublime_plugin.TextCommand):
    secure = False
    chars = string.ascii_letters + string.digits
    secure_chars = chars + "!@#$%^&*_-+=|/?:;<>~"
    length = randrange(6, 31)
    
    def run(self, edit):
        population = self.secure_chars if self.secure else self.chars
        p = ''.join(sample(population, self.length))
        for region in self.view.sel():
            self.view.replace(edit, region, p)

class GenerateShortPasswordCommand(PasswordCommand):
    length = 10

class GenerateMediumPasswordCommand(PasswordCommand):
    length = 15

class GenerateLongPasswordCommand(PasswordCommand):
    length = 20

class GenerateShortSecurePasswordCommand(GenerateShortPasswordCommand):
    secure = True

class GenerateMediumSecurePasswordCommand(GenerateMediumPasswordCommand):
    secure = True
    
class GenerateLongSecurePasswordCommand(GenerateLongPasswordCommand):
    secure = True

class GenerateCustomPasswordCommand(sublime_plugin.TextCommand):
    patter = "Cvcvcv99"
    result = ''
    def run(self, edit):
        self.edit = edit
        self.view.window().show_input_panel("Input Pattern", self.patter, self.generate_string, None, None)
        for region in self.view.sel():
            self.view.replace(edit, region, self.result)

    def generate_string(self, user_input):
        self.patter = user_input
        chars = "!@#$%^&*_-+=|/?:;<>~"
        letter_upper = "BCDFGHJKLMNPQRSTVWXYZ"
        letter_lower = "bcdfghjklmnpqrstvwxyz"
        vowels_upper = "AEIOU"
        vowels_lower = "aeiou"
        digits = "0123456789"
        result =""
        for char in user_input:
            if char == "/#":
                flag = randrange(0, len(chars))
                result += chars[flag]
            elif char == "c":
                flag = randrange(0, len(letter_lower))
                result += letter_lower[flag]
            elif char == "C":
                flag = randrange(0, len(letter_upper))
                result += letter_upper[flag]
            elif char == "v":
                flag = randrange(0, len(vowels_lower))
                result += vowels_lower[flag]
            elif char == "V":
                flag = randrange(0, len(vowels_upper))
                result += vowels_upper[flag]
            elif char == "9":
                flag = randrange(0, len(digits))
                result += digits[flag]
            else:
                result += char
        self.result = result