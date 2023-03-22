class khush:
    company = "Microsoft"
    
    def __init__(self, name, email, product):
        self.name = name
        self.email = email
        self.product = product
        
    def getDetails(self):
        print(f"{self.name} is working in {self.company} whose email is {self.email} and their product is {self.product}")

prog1 = khush("KHUSH", "khushnadpara@gmail.com", "OneNote")
prog2 = khush("Gautam", "gautambariya@gmail.com", "Outlook")

prog1.getDetails()
prog2.getDetails()
