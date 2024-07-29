from prefect import task

@task(name="mi primera tarea")
def task_primera_tarea():
    print("esta es mi primera tarea con prefect...")