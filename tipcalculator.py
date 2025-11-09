def get_bill_amount():
    return float(input("Whats the Ammount of the bill? : "))
    
def get_number_of_people():
    return int(input("How many people had dinner Together? : ")) 

def tip_calculate():
    tip_float = float(input("How Much Tip Do you want to give? [No Need For % Sign] : "))
    tip = bill * (tip_float / 100)
    return tip


def final_count(tip):
    each_person = (tip + bill) / Number_of_people

    print(f"Bill = ${bill}")
    print(f"Total Bill = ${round(bill + tip)}")
    print(f"Tip = ${round(tip)}")
    print(f"For Each Person = ${round(each_person)}")

bill =  get_bill_amount()
tip = tip_calculate()
Number_of_people = get_number_of_people()
final = final_count(tip)
