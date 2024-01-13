from datetime import datetime;
import requests;

class User:
    def __init__(self):
        self.serialNumber: str = self.GenerateSerialNumber();
        self.firstName: str = self.GenerateFirstName(self.serialNumber);
        self.lastName: str = self.GenerateLastName(self.serialNumber);
        self.username: str = self.GenerateUsername(self.serialNumber);
        self.password: str = self.GeneratePassword(self.serialNumber);

        self.baseUrl: str = "https://demoqa.com";
        self.userEndpoint: str = "/Account/v1/User";
        self.accountAuthEndpoint: str = "/Account/v1/Authorized"
        self.UUID: str = "";
    
    def __del__(self):
        self.DeleteUserViaApi();
    
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
    
    def RegisterUserViaApi(self) -> None:
        url = self.baseUrl + self.userEndpoint;
        data = {"userName" : self.username,
                "password" : self.password};
        response = requests.post(url, json = data, timeout = 60);
        assert response.status_code == 201;
        self.UUID = response.json()["userID"];
        response.close();
    
    def DeleteUserViaApi(self) -> None:
        if (self.UUID != ""):
            url = self.baseUrl + self.userEndpoint + "/" + self.UUID;
            response = requests.delete(url, auth = (self.username, self.password), timeout = 60);
            assert response.status_code == 204;
            response.close();
    