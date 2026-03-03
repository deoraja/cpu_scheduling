from collections import deque
import time
import random

class Task:
    def __init__(self,task_id, purpose, duration,max_retries=2):
        self.task_id = task_id
        self.purpose = purpose
        self.duration = duration
        self.state = 'PENDING'
        self.max_retries = max_retries
        self.retry_count = 0

    def __str__(self):
        return f"Task {self.task_id} | {self.purpose} | {self.state}"


class FIFOScheduler:
    
    def __init__(self):
        self.queue = deque()
        self.completed_tasks = []
    
    def submit_task(self,task):
        self.queue.append(task)
        print(task)
    
    def run(self):
        failure_probability = 0.4
        while self.queue:
            current_task = self.queue.popleft()
            current_task.state = 'RUNNING'
            print(f"{current_task}")
            try:
              time.sleep(current_task.duration)

              # Simulate random failure
              if random.random() < failure_probability:
                raise Exception("Random failure occurred")
              
              current_task.state = 'COMPLETED'
              self.completed_tasks.append(current_task)
              print(f"{current_task}")

            except Exception:
                current_task.retry_count +=1

                if current_task.retry_count <= current_task.max_retries:
                    current_task.state = 'RETRYING'
                    print(f"{current_task} | Retrying ({current_task.retry_count})")
                    self.queue.append(current_task)
                else:
                  current_task.state = 'FAILED'
                  print(f"{current_task} permanently failed")
            
    
    def __str__(self):
        return f"Task queue is {self.queue}"


scheduler1 = FIFOScheduler()

task1 = Task(1,'Basic',2)
task2 = Task(2,'Intermediate',2)
task3 = Task(3,'Advanced',2)

scheduler1.submit_task(task1)
scheduler1.submit_task(task2)
scheduler1.submit_task(task3)
scheduler1.run()
print(len(scheduler1.queue) )           
print(len(scheduler1.completed_tasks))