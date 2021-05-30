from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print("{}, {}. {}, {}".format(ruby.name, ruby.typing, ruby.reflection, ruby.year))

print(ruby.is_dynamic())
print(visual_basic.is_dynamic())

print(python)

language_list = [ruby,python,visual_basic]

print("The dynamically typed languages are:")
for language in language_list:
    if language.is_dynamic():
        print(language.name)
