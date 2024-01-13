from datetime import datetime;

class User:
    def __init__(self):
        self.serialNumber: str = self.GenerateSerialNumber();
        self.firstName: str = self.GenerateFirstName(self.serialNumber);
        self.lastName: str = self.GenerateLastName(self.serialNumber);
        self.username: str = self.GenerateUsername(self.serialNumber);
        self.password: str = self.GeneratePassword(self.serialNumber);
    
    def GenerateFirstName(self, serial: str) -> str:
        firstNameOptions = ["John", "Joe", "James", "Jason", "Jorden"];
        index = int(serial) % len(firstNameOptions);
        return firstNameOptions[index];
    
    def GenerateLastName(self, serial: str) -> str:
        lastNameOptions = ["Smith", "Store", "Booke", "Rane", "Koors"];
        index = int(serial) % len(lastNameOptions);
        return lastNameOptions[index];
    
    def GenerateUsername(self, serial: str) -> str:
        return "PT" + serial;
    
    def GeneratePassword(self, serial: str) -> str:
        return "Pwd!" + serial;
    
    def GenerateSerialNumber(self) -> str:
        return datetime.now().strftime("%d%m%Y%H%M%S");
    
    def  RegisterUserViaApi(self) -> bool:
        pass;