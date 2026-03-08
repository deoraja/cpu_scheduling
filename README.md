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

- Multiple CPU scheduling algorithms
- Modular Python project structure
- Task lifecycle simulation
- Failure simulation with retry logic
- CPU execution timeline visualization
- Easy to extend with new schedulers

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

Task 2 | Intermediate | RUNNING
Task 3 | Advanced | RUNNING
Task 3 | Advanced | COMPLETED
Task 1 | Basic | RUNNING
Task 1 | Basic | COMPLETED

CPU Timeline
------------
T2 | T3 | T3 | T1 | T1 | T1
```

The **CPU timeline** shows which task was executed at each time unit.

---

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

```
python main.py
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
PENDING → RUNNING → COMPLETED
                  → FAILED
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