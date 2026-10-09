import random

class randomOperations:
    def ran_num(self, start, end):
        randomNumber = random.randint(start, end)
        return randomNumber

    def ran_list(self, length):
        randomList = random.sample(range(1,100), length)
        return randomList

    def ran_pass(self, length):
        password = []
        special_characters = ['!', '@', '#', '$', '&', '-']
        uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        data_list = special_characters + uppercase + lowercase + numbers
        pass_list = random.sample(data_list, length)
        for i in pass_list:
            password.append(i)
        return password

    def ran_otp(self):
        otp_list = []
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        otp = random.sample(numbers, 4)
        for i in otp:
            otp_list.append(i)
        return otp