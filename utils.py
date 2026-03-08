def reset_tasks(tasks):
    for t in tasks:
        t.reset()

def print_results(scheduler):
        
        print("\nCompleted Tasks:")
        for t in scheduler.completed_tasks:
            print(t)

        if scheduler.failed_tasks:
            print("Failed Tasks:")
            for t in scheduler.failed_tasks:
                print(t)
        else:
            print("All tasks completed successfully.")
        
        print("\nCPU Timeline:")
        print(" | ".join(scheduler.timeline))

def run_scheduler(name, scheduler, tasks):
        
        print(f"\n--- {name} Scheduler ---")

        reset_tasks(tasks)
        for t in tasks:
            scheduler.submit_task(t)

        scheduler.run()

        print_results(scheduler)