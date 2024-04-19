# purchase.py
from locust import task, TaskSet

class PurchaseTasks(TaskSet):
    @task(3)
    def visit_purchase_page(self):
        self.client.get("/purchase.php")
    
    @task(1)
    def make_purchase(self):
        data = {
            "inputName": "John Doe",
            "address": "123 Elm St",
            "city": "Anytown",
            "state": "CA",
            "zipCode": "90210",
            "cardType": "Visa",
            "creditCardNumber": "4111111111111111",
            "creditCardMonth": "11",
            "creditCardYear": "2024",
            "nameOnCard": "John Doe"
        }
        self.client.post("/confirmation.php", data)
