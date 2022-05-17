
from faker import Faker

faker = Faker()



def data_generator(n):    
    customers = []

    for i in range(0,n):
        customer = faker.simple_profile()
        del customer['birthdate']
        customers.append(customer)

    return customers

    

