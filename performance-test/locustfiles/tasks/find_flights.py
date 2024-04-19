from locust import task, TaskSet
# Use relative imports for modules within your package
from ..common.logging_helpers import setup_logging, log_message

class FindFlightsTasks(TaskSet):
    @task(2)
    def find_flights(self):
        with self.client.get("/reserve.php", catch_response=True) as response:
            if "Flights from" in response.text:
                response.success()

    @task(1)
    def post_flights(self):
        # This mimics selecting a flight based on data that would typically be part of the page
        data = {
            "fromPort": "Philadelphia",
            "toPort": "London"
        }
        response = self.client.post("/purchase.php", data)

        if response.ok:
            log_message("Flight reservation successful")
        else:
            log_message(f"Failed to make reservation: {response.status_code}")
