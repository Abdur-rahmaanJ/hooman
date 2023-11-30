import os

first_element_printed = 0
print("Please choose from:")
for file in os.listdir('.'):
    if not file.startswith("__"):
        if file.endswith(".py"):
            first_element_printed
            print("•", "python -m hooman.demos."+file[:-3])