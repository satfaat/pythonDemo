import psutil
import schedule
import time
import logging


class Monitoring:
    # Function to log messages
    def log_message(self, message):
        # Configure logging
        logging.basicConfig(filename='.report/system_monitor.log', level=logging.INFO,
                            format='%(asctime)s - %(message)s')
        logging.info(message)

    # Function to print alerts to the console
    def print_alert(self, message):
        print(f"ALERT: {message}")

    # Health check functions
    def check_cpu_usage(self, threshold=50):
        cpu_usage = psutil.cpu_percent(interval=1)

        if cpu_usage > threshold:
            message = f"High CPU usage detected: {cpu_usage}%"
            self.log_message(message)
            self.print_alert(message)

    def check_memory_usage(self, threshold=80):
        memory_usage = psutil.virtual_memory().percent

        if memory_usage > threshold:
            message = f"High memory usage detected: {memory_usage}%"
            self.log_message(message)
            self.print_alert(message)

    def check_disk_space(self, path='/', threshold=75):
        disk_usage = psutil.disk_usage(path).percent

        if disk_usage > threshold:
            message = f"Low disk space detected: {disk_usage}%"
            self.log_message(message)
            self.print_alert(message)

    def check_network_traffic(self, threshold=100 * 1024 * 1024):
        network_traffic = psutil.net_io_counters().bytes_recv +\
            psutil.net_io_counters().bytes_sent

        if network_traffic > threshold:
            message = f"High network traffic detected: {
                network_traffic: .2f} MB"
            self.log_message(message)
            self.print_alert(message)

    # Function to run health checks
    def run_health_checks(self):
        print("Monitoring the system...")
        self.log_message("Running system health checks...")

        self.check_cpu_usage()
        self.check_memory_usage()
        self.check_disk_space()
        self.check_network_traffic()

        self.log_message("Health checks completed.")
