import click
import os
import json

TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('task')
def add(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)
    click.echo(f'Task "{task}" added.')

@cli.command()
def list():
    """List all tasks."""
    tasks = load_tasks()
    if tasks:
        click.echo('Tasks:')
        for i, task in enumerate(tasks, start=1):
            status = '[x]' if task['done'] else '[ ]'
            click.echo(f"{i}. {status} {task['task']}")
    else:
        click.echo('No tasks.')

@cli.command()
@click.argument('task_number', type=int)
def complete(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        click.echo(f'Task {task_number} marked as completed.')
    else:
        click.echo('Invalid task number.')

if __name__ == '__main__':
    cli()
