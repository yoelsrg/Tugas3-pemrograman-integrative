class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be greater than zero.")
        self._weight = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be greater than zero.")
        self._height = value
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

# Contoh penggunaan kelas BMI
if __name__ == "__main__":
    # Membuat dua objek BMI
    person1 = BMI(65, 1.55)
    person2 = BMI(77, 1.60)

    # Menghitung nilai BMI untuk setiap objek
    bmi1 = person1.BMI_Value()
    bmi2 = person2.BMI_Value()

    # Mencetak nilai BMI untuk setiap objek
    print("BMI for person 1:", bmi1)
    print("BMI for person 2:", bmi2)

    # Membandingkan dua objek BMI
    if person1 == person2:
        print("Person 1 and Person 2 have the same weight and height.")
    else:
        print("Person 1 and Person 2 have different weight or height.")
