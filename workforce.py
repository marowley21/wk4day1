class User:  # User class
    def __init__(self, first_name, last_name, email, created_on, id): # Constructor
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_on = created_on
        self.id = id

    def __repr__(self): 
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}', '{self.created_on}', '{self.id}')"

    def __str__(self): 
        return f"{self.first_name} {self.last_name} {self.email} {self.created_on} {self.id}"

    def __eq__(self, other): 
        return self.email == other.email

    def __hash__(self): 
        return hash(self.email)

    def change_first_name(self, new_first_name): 
        self.first_name = new_first_name 

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name


class Employee(User):
    def __init__(self, first_name, last_name, email, created_on, home_address, security_level, department, id):
        super().__init__(first_name, last_name, email, created_on, id)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department

    def change_department(self, new_department): 
        self.department = new_department


class Customer(User): 
    def __init__(self, first_name, last_name, email, created_on, shipping_address, billing_address, purchase_history, id):
        super().__init__(first_name, last_name, email, created_on, id)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history

    def change_billing_address(self, new_billing_address): 
        self.billing_address = new_billing_address

    def change_shipping_address(self, new_shipping_address): 
        self.shipping_address = new_shipping_address


if __name__ == '__main__':
    employees = [ Employee('John', 'Doe', 'johndoe@mail.com', '2020-01-01', '123 Main St', 1, 'IT', 'JohnDoeIT'),
                  Employee('Jack','Denial', 'jackdenial@mail.com', '2020-01-02', '456 Main St', 2, 'HR', 'JackDenialHR'),
                  Employee('Jane', 'Doe', 'janedoe@mail.com', '2020-01-03', '789 Main St', 3, 'Sales', 'JaneDoeSales') ]

    customers = [ Customer('John', 'Smith', 'johnsmith@mail.com', '2020-01-01', '123 Main St', '123 Main St', [], 'jonhsmith12' ),
                    Customer('Jack', 'Smith', 'jacksmith@mail.com', '2020-01-02', '456 Main St', '456 Main St', [], 'jacksmith12' ),
                    Customer('Jane', 'Smith', 'janesmith@mail.com', '2020-01-03', '789 Main St', '789 Main St', [], 'janesmith12' ) ]
    
    users = employees + customers
    users.sort(key=lambda user: user.created_on, reverse=True)
    print(*users,sep='\n')
