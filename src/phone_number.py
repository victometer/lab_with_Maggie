# class PhoneNumber:
#     def __init__(self, input_number):
#         self.phone_number = input_number

def phone_number_formater (number):
    string_number = str(number)
    list_of_numbers = []
    for number in string_number:
        list_of_numbers.append(number)
    first_3_nums = list_of_numbers[0] + list_of_numbers[1] + list_of_numbers[2]
    middle_3_nums = list_of_numbers[3] + list_of_numbers[4] + list_of_numbers[5]
    last_four_nums = list_of_numbers[6] + list_of_numbers[7] + list_of_numbers[8] + list_of_numbers[9]
    return "(" + first_3_nums + ") " + middle_3_nums +"-" + last_four_nums
    
    

    

        