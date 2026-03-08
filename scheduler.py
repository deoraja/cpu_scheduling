from collections import deque
import time
import random

#  Base Scheduler 
class BaseScheduler:
    def __init__(self, failure_probability = 0.3):
        self.tasks = []
        self.completed_tasks = []
        self.failed_tasks = []
        self.failure_probability = failure_probability
        self.timeline = []

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

            self.timeline.append(f"T{current_task.task_id}")

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
        super().__init__(failure_probability = 0.4)
        self.tasks = deque() 

    def submit_task(self, task):
        self.tasks.append(task)
        print(task)

    def pick_task(self):
        return self.tasks.popleft()

#  SJF Scheduler 
class SJF_Scheduler(BaseScheduler):
    def __init__(self):
        super().__init__(failure_probability = 0.3)

    def pick_task(self):
        self.tasks.sort(key=lambda t: t.duration)
        return self.tasks.pop(0)

    def resort_tasks(self):
        self.tasks.sort(key=lambda t: t.duration)

#  ROUND ROBIN Scheduler
class RoundRobin_Scheduler(BaseScheduler):
    def __init__(self, time_quantum = 2): 
        super().__init__(failure_probability = 0.3)
        self.tasks = deque()
        self.time_quantum = time_quantum
    
    def submit_task(self, task):
        self.tasks.append(task)
        print(task)

    def pick_task(self):
        return self.tasks.popleft()
    
    def run(self):
        while self.tasks:
            
            current_task = self.tasks.popleft()
            current_task.state = 'RUNNING'

            print(current_task)

            execution_time = min(self.time_quantum,current_task.remaining_time)
            
            for _ in range(execution_time):
                self.timeline.append(f"T{current_task.task_id}")

            time.sleep(execution_time)

            current_task.remaining_time -= execution_time

            if current_task.remaining_time > 0:
                current_task.state = 'PENDING'
                self.tasks.append(current_task)
            else:
                current_task.state = 'COMPLETED'
                self.completed_tasks.append(current_task)
                print(current_task)

#  SRTF Scheduler
class SRTF_Scheduler(BaseScheduler):
    def __init__(self):
        super().__init__(failure_probability = 0.2)
    
    def pick_task(self):
        self.tasks.sort(key=lambda t: t.remaining_time)
        return self.tasks.pop(0)
    
    def run(self):
        while self.tasks:
            current_task = self.pick_task()

            current_task.state = 'RUNNING' 

            print(current_task)
            
            self.timeline.append(f"T{current_task.task_id}")
            
            time.sleep(1)

            current_task.remaining_time -= 1

            if current_task.remaining_time > 0:
                current_task.state = 'PENDING'
                self.tasks.append(current_task)
            else:
                current_task.state = 'COMPLETED'
                self.completed_tasks.append(current_task)
                print(current_task)
