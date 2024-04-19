# home_page.py
from locust import task, between, TaskSet

class HomePageTasks(TaskSet):
    @task(1)
    def load_home_page(self):
        self.client.get("/")
