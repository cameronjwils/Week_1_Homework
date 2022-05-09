# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, cash):
    cc_pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, x):
    cc_pet_shop["admin"]["pets_sold"] += x

def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []

    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
     if get_customer_cash(customer) >= pet["price"]:
        return True
     else:
        return False

# def sell_pet_to_customer(pet_shop, pet, customer):
#     add_pet_to_customer(customer, pet)
#     get_pets_sold(pet_shop)
#     get_customer_cash(customer)
#     get_total_cash(pet_shop)










    









