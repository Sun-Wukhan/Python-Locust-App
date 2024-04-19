# main_locustfile.py
import os
import signal
from locust import HttpUser, between
from locustfiles.tasks.home_page import HomePageTasks
from locustfiles.tasks.find_flights import FindFlightsTasks
from locustfiles.tasks.purchase import PurchaseTasks

def shutdown_handler(signum, frame):
    print("Shutdown signal received. Shutting down Locust.")
    events.quitting.fire(reverse=True)

# Register the shutdown handler
signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [HomePageTasks, FindFlightsTasks, PurchaseTasks]
