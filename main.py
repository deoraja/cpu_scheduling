from task import Task
from scheduler import(FCFS_Scheduler, SJF_Scheduler, RoundRobin_Scheduler, SRTF_Scheduler)
from utils import run_scheduler

if __name__ == "__main__":
  tasks = [
    Task(1, "Basic", 3),
    Task(2, "Intermediate", 1),
    Task(3, "Advanced", 2)
    ]
  run_scheduler("FCFS", FCFS_Scheduler(), tasks)
  run_scheduler("SJF", SJF_Scheduler(), tasks)
  run_scheduler("ROUND ROBIN", RoundRobin_Scheduler(), tasks)
  run_scheduler("SRTF", SRTF_Scheduler(), tasks)
   
              