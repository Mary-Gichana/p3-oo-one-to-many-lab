class Owner:
    def __init__(self, name):
        
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        self._pets = [] 

    def pets(self):
    
        return self._pets

    def add_pet(self, pet):
        
        if not isinstance(pet, Pet):
            raise Exception("Only instances of the Pet class can be added.")
        pet.owner = self  
        self._pets.append(pet)  

    def get_sorted_pets(self):
    
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = [] 

    def __init__(self, name, pet_type, owner=None):
        
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types: {', '.join(self.PET_TYPES)}.")
        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if owner:
            owner.add_pet(self) 
        Pet.all.append(self)  
