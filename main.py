import click
from datetime import datetime, timedelta
import csv

@click.group()
def main():
    """
    ***********************************************************************\n
    -   This is a CLI tool to add and retrieve the small bits of notes.   -\n
    ***********************************************************************
    """
    pass


def is_within_this_week(date_str) -> bool:
    date = datetime.fromisoformat(date_str)
    now = datetime.now()
    start_of_week = now - timedelta(days=now.isoweekday() - 1)  # Monday
    end_of_week = start_of_week + timedelta(days=6)  # Sunday
    return start_of_week <= date <= end_of_week

def is_within_this_month(date_str) -> bool:
    date = datetime.fromisoformat(date_str)
    now = datetime.now()
    return date.year == now.year and date.month == now.month

def is_within_today(date_str) -> bool:
    date = datetime.fromisoformat(date_str)
    now = datetime.now()
    return date.year == now.year and date.month == now.month and date.day == now.day

@main.command()
@click.option("-t", "--today", is_flag=True, help="Filter notes written today")
@click.option("-w", "--week", is_flag=True, help="Filter notes written this week")
@click.option("-m", "--month", is_flag=True, help="Filter notes written this month")
def listnotes(today:bool, week:bool, month:bool) -> None:
    """Display list of all notes, can be filtered using options"""
    what_to_show = []
    try: # error handling
        with open("storage.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row)==2] # filtering blank lines

        if today:
            what_to_show = [(index,message[1]) for index,message in enumerate(rows) if is_within_today(message[0])]
        if week:
            what_to_show = [(index,message[1]) for index,message in enumerate(rows) if is_within_this_week(message[0])]
        if month:
            what_to_show = [(index,message[1]) for index,message in enumerate(rows) if is_within_this_month(message[0])]
        else:
            what_to_show = [(index,message[1]) for index,message in enumerate(rows)]
    except FileNotFoundError:
        click.echo(click.style("Storage.csv not found.", fg="red"))

    for data in what_to_show:
        click.echo(data)


@main.command()
@click.option("-c", "--count", type=int, default=1, help="Returns last -c latest notes")
def latest(count:int) -> None:
    """Returns the latest note made"""
    try: # error handling
        with open("storage.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row)==2] # filtering blank lines
    except FileNotFoundError:
        click.echo(click.style("Storage.csv not found.", fg="red"))

    for _,message in rows[-count:]:
        click.echo(message)


@main.command()
@click.option("-n", "--linenumbers", help="Comma seperated line/s which needs to be deleted")
@click.option("--recent", is_flag=True, help="Delete last added note")
def delete(linenumbers:str, recent:str) -> None:
    """Deletes notes"""
    try: # error handling
        with open("storage.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row)==2] # filtering blank lines

        if not rows:
            click.echo(click.style("No notes found to delete.", fg="yellow"))
            return
        
    except FileNotFoundError:
        click.echo(click.style("Storage.csv not found.", fg="red"))
        return
    
    changed = rows
    if linenumbers:
        lines = [int(i) for i in linenumbers.split(',')]
        if any(line < 0 or line > len(rows) for line in lines):
            click.echo(click.echo("Error: some lines are out of range", fg="red"))
            return
        changed = [data for index,data in enumerate(rows) if index not in lines]

    if recent:
        if len(changed):
            changed = changed[:-1]
        else:
            click.echo(click.style("No note is left to be deleted", fg="yellow"))
            return

    try: # error handling
        with open("storage.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(changed)
        click.echo(click.style("Note Deleted Successfully", fg="green"))
    except FileNotFoundError:
        click.echo(click.style("Storage.csv not found. Cannot write changed into file", fg="red"))

    

@main.command()
@click.option("-m", "--message", prompt=True, help="Enter the message that needs to be saved")
def addnote(message:str) -> None:
    """Enter the message that needs to be saved"""
    with open("storage.csv", "a", newline="") as file:
        date = datetime.now().isoformat()
        writer = csv.writer(file)
        writer.writerow([date, message])
    click.echo(click.style("Message added successfully", fg='green'))

if __name__ == "__main__":
    main()