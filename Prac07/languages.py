from Prac07.programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

language_list = [ruby, python, vb]

print("The dynamically typed languages are: ")
for language in language_list:
    if ProgrammingLanguage.is_dynamic(language) is True:
        print(language.name)
