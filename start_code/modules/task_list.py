

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted = []
    for x in list:
        if x["completed"] == False:
            uncompleted.append(x)
    return uncompleted


## Get a list of completed tasks
def get_completed_tasks(list):
    return get_tasks_by_status(list, True)

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    return get_tasks_by_status(False)

## Find a task with a given description
def get_task_with_description(list, description):
    for x in list:
        if x["description"] == description:
            return x

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    status_collect = []
    for x in list:
        if x["completed"] == status:
            status_collect.append(x)
    return status_collect


def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)
