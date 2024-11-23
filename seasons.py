from datetime import  datetime,date
import inflect
inflector = inflect.engine()
import sys

def main():
    dob = input("Date of birth: ")
    try:
        y,m,d=dob.split("-")
    except ValueError:
        print("Invalid Date")
        sys.exit(1)
    else:
        y, m, d = map(int, (y, m, d))
        mins=to_mins(date(y,m,d))
        key=to_mins(date.today())
        print(f"{to_words(mins-key)} minutes")

def to_mins(dob):
    today = date.today()
    time_to_birthday = abs(dob - today)
    return 24*60*time_to_birthday.days

def to_words(j):
    final= inflector.number_to_words(j)
    if "and" in final:
        final=final.replace("and ","")
    final=final.replace(final[0],final[0].upper(),1)
    return final



if __name__ == "__main__":
    main()