class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        
        self.owner = owner
        if owner is not None:
            owner.add_pet(self) 
        
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  

    def pets(self):
        """Return the full list of owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner's list, and set the owner of the pet."""
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of the Pet class.")
        
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of owner's pets based on their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


owner = Owner("Ben")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)

print([pet.name for pet in owner.pets()])  
