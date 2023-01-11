import sys
import random
from classes import Factory
from classes.readers.Reader import Reader

if (__name__ == "__main__"):
    args = sys.argv[1:]
    reader = Factory.Factory().getReader(args[0])
    reader.readFile(args[1])
    final_grades = reader.filterAttributes(['Nombre','Final'])
    approved_students = [student for student in final_grades if student["Final"]>5]
    print(f"Felicidades a {random.choice(approved_students)['Nombre']}")