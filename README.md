# CPU Scheduler Simulation

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-learning%20project-orange)

A Python simulation of classic **Operating System CPU scheduling algorithms**, including **FCFS, SJF, SRTF, and Round Robin**, with task lifecycle management and CPU execution timeline visualization.

---

## Overview

Operating systems must decide **which process gets CPU time** when multiple processes are ready to run.

This project simulates several common CPU scheduling strategies and demonstrates how they behave with tasks of different execution times.

Implemented algorithms:

- **FCFS — First Come First Serve**
- **SJF — Shortest Job First**
- **SRTF — Shortest Remaining Time First**
- **Round Robin — Time-sliced scheduling**

---

## Features

- Multiple CPU scheduling algorithms (FCFS, SJF, SRTF, Round Robin)
- CLI-based execution with algorithm selection
- Task lifecycle simulation with retry handling
- Gantt chart visualization of CPU execution timeline
- Performance metrics (Average Waiting Time, Turnaround Time)
---

## Project Structure

```
cpu_scheduler/
├── task.py          # Task model and state management
├── scheduler.py     # Scheduling algorithm implementations
├── utils.py         # Helper utilities and result printing
├── main.py          # Program entry point
└── README.md
```

---

## Scheduling Algorithms

| Algorithm | Type | Description |
|----------|----------|----------|
| **FCFS** | Non-preemptive | Tasks execute in arrival order |
| **SJF** | Non-preemptive | Shortest job executes first |
| **SRTF** | Preemptive | Task with shortest remaining time executes |
| **Round Robin** | Preemptive | Tasks receive fixed time slices |

---

## Example Output

```
--- SRTF Scheduler ---
Task 1 | Basic | PENDING
Task 2 | Intermediate | PENDING
Task 3 | Advanced | PENDING
Task 2 | Intermediate | RUNNING
Task 2 | Intermediate | COMPLETED
Task 3 | Advanced | RUNNING
Task 3 | Advanced | RUNNING
Task 3 | Advanced | COMPLETED
Task 1 | Basic | RUNNING
Task 1 | Basic | RUNNING
Task 1 | Basic | RUNNING
Task 1 | Basic | COMPLETED

Completed Tasks:
Task 2 | Intermediate | COMPLETED
Task 3 | Advanced | COMPLETED
Task 1 | Basic | COMPLETED
All tasks completed successfully.

CPU Timeline (Gantt Chart):
| T2 | T3 | T3 | T1 | T1 | T1 |
0    1    2    3    4    5    6


Performance Metrics
-------------------
Task 1 -> WT: 3, TAT: 6
Task 2 -> WT: 0, TAT: 1
Task 3 -> WT: 1, TAT: 3
Average Waiting Time: 1.33
Average Turnaround Time: 3.33
```

The **CPU timeline** shows which task was executed at each time unit.

---
## Scheduling Algorithms Comparison

| Algorithm      | Average Waiting Time | Average Turnaround Time | Key Observation                          |
|----------------|--------------------|------------------------|-----------------------------------------|
| FCFS           | 4.33               | 6.33                   | Simple, but suffers from Belady's anomaly  |
| SJF            | 1.33               | 3.33                   | Minimizes average waiting time          |
| SRTF           | 1.33               | 3.33                   | Preemptive, best responsiveness         |
| Round Robin    | 2.67               | 4.67                   | Fair time-slicing, slightly higher TAT |

#### Belady's anomaly :  increasing the number of page frames in memory leads to an increase in the number of page faults

#### Note: Values are based on default example tasks; your simulation may produce slightly different metrics depending on task durations and retries.

## Requirements

- Python 3.8+
- No external dependencies

---

## How To Run

### 1. Clone the repository

```
git clone https://github.com/deoraja/cpu_scheduling.git
cd cpu_scheduling
```

### 2. Run the simulation

The simulator can be run using command-line arguments to select scheduling algorithms and input tasks.

### Run all algorithms (default)
```
python main.py
```

### Run a specific algorithm
```
python main.py --algo srtf
python main.py --algo fcfs
python main.py --algo sjf
python main.py --algo rr
```

---

## Example Tasks

### Task Structure

Each task contains the following attributes:

- `task_id` — unique identifier for the task
- `purpose` — description or type of task
- `duration` — total CPU time required
- `remaining_time` — remaining execution time (used in preemptive scheduling)
- `state` — current task state (`PENDING`, `RUNNING`, `COMPLETED`, `FAILED`)
- `max_retries` — maximum retry attempts if execution fails
- `retry_count` — number of retries attempted

### Task States

Tasks transition through several states:

```
PENDING → RUNNING → COMPLETED → FAILED
```
---
### Example Task

```python
task = Task(
    task_id=1,
    purpose="Basic computation",
    duration=3
)
```

---

## Concepts Demonstrated

This project demonstrates several **operating system concepts**:

- CPU scheduling algorithms
- Preemptive vs non-preemptive scheduling
- Task lifecycle management
- Execution timeline simulation
- Modular Python project structure

---

## License

This project is licensed under the **MIT License**.

---

## Author

Created as a learning project to explore **Operating System scheduling algorithms and Python system design**.
