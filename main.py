from collections import deque
import time
import random

class Task:
    def __init__(self, task_id, purpose, duration, max_retries=2):
        self.task_id = task_id
        self.purpose = purpose
        self.duration = duration
        self.state = 'PENDING'
        self.max_retries = max_retries
        self.retry_count = 0

    def __str__(self):
        return f"Task {self.task_id} | {self.purpose} | {self.state}"

#  Base Scheduler 
class BaseScheduler:
    def __init__(self, failure_probability=0.3):
        self.tasks = []
        self.completed_tasks = []
        self.failed_tasks = []
        self.failure_probability = failure_probability

    def submit_task(self, task):
        self.tasks.append(task)
        print(task)

    def pick_task(self):
        """Override this method in child classes for different scheduling strategies"""
        raise NotImplementedError

    def run(self):
        while self.tasks:
            current_task = self.pick_task()
            current_task.state = 'RUNNING'
            print(current_task)
            try:
                time.sleep(current_task.duration)
                if random.random() < self.failure_probability:
                    raise Exception("Random failure occurred")
                current_task.state = 'COMPLETED'
                self.completed_tasks.append(current_task)
                print(current_task)
            except Exception:
                current_task.retry_count += 1
                if current_task.retry_count <= current_task.max_retries:
                    current_task.state = 'RETRYING'
                    print(f"{current_task} | Retry_Attempt: {current_task.retry_count}")
                    self.tasks.append(current_task)
                    self.resort_tasks()
                else:
                    current_task.state = 'FAILED'
                    self.failed_tasks.append(current_task)
                    print(f"{current_task} (permanently failed)")

    def resort_tasks(self):
        """Optional: override in subclasses if tasks need to be reordered after retry"""
        pass

#  FCFS Scheduler 
class FCFS_Scheduler(BaseScheduler):
    def __init__(self):
        super().__init__(failure_probability=0.4)
        self.tasks = deque() 

    def submit_task(self, task):
        self.tasks.append(task)
        print(task)

    def pick_task(self):
        return self.tasks.popleft()

#  SJF Scheduler 
class SJF_Scheduler(BaseScheduler):
    def __init__(self):
        super().__init__(failure_probability=0.3)

    def pick_task(self):
        self.tasks.sort(key=lambda t: t.duration)
        return self.tasks.pop(0)

    def resort_tasks(self):
        self.tasks.sort(key=lambda t: t.duration)

#  Example Usage 
if __name__ == "__main__":
    # create tasks
    task1 = Task(1, 'Basic', 3)
    task2 = Task(2, 'Intermediate', 1)
    task3 = Task(3, 'Advanced', 2)

    # FCFS Example
    print("\n--- FCFS Scheduler ---")
    fcfs = FCFS_Scheduler()
    for t in [task1, task2, task3]:
        fcfs.submit_task(t)
    fcfs.run()

    print("\nCompleted Tasks:")
    for t in fcfs.completed_tasks:
        print(t)

    if fcfs.failed_tasks:
        print("Failed Tasks:")
        for t in fcfs.failed_tasks:
            print(t)
    else:
        print("All tasks completed successfully.")

    # SJF Example
    print("\n--- SJF Scheduler ---")
    # reset tasks for SJF
    for t in [task1, task2, task3]:
        t.state = 'PENDING'
        t.retry_count = 0

    sjf = SJF_Scheduler()
    for t in [task1, task2, task3]:
        sjf.submit_task(t)
    sjf.run()

    print("\nCompleted Tasks:")
    for t in sjf.completed_tasks:
        print(t)

    if sjf.failed_tasks:
        print("Failed Tasks:")
        for t in sjf.failed_tasks:
            print(t)
    else:
        print("All tasks completed successfully.")