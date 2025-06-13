from datetime import datetime

def age_calculator(dob):

    now = datetime.now()
    given_date = datetime.strptime(dob, "%d-%m-%Y")

    age_years = now.year - given_date.year

    if now.month - given_date.month < 0 or (now.month == given_date.month and now.day - given_date.day < 0):
        age_years -= 1

    return print(age_years)

age_calculator("11-06-2002")



    

