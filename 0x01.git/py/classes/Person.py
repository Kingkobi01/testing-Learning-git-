class Person:
    def __init__(self, first_name, last_name, email_address) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    
    def fullname(self):
        return f'{self.first_name, self.last_name}'
    
    def __repr__(self) -> str:

        description = f"""
Fullname: {self.fullname()}
Email: {self.email_address}
"""
        return description




Dangote = Person("Samuel", "Owusu", "sammy@dangote.com")

assert "Sam" == Dangote.first_name[0:3]

    
