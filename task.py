class Task:
    def __init__(self, task_id, purpose, duration, max_retries = 2):
        self.task_id = task_id
        self.purpose = purpose
        self.duration = duration
        self.remaining_time = duration
        self.state = 'PENDING'
        self.max_retries = max_retries
        self.retry_count = 0

    def __str__(self):
        return f"Task {self.task_id} | {self.purpose} | {self.state}"
    
    def reset(self):
        self.state = "PENDING"
        self.retry_count = 0
        self.remaining_time = self.duration