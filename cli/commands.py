import click
from logic.filters import is_within_today, is_within_this_week, is_within_this_month
from logic.note_operations import read_notes, get_latest_notes, delete_notes, add_note

@click.group()
def main():
    """
    ********************************************************\n
    -   Notes CLI Tool: Add, retrieve, and manage notes.   -\n
    ********************************************************
    """
    pass

@main.command()
@click.option("-t", "--today", is_flag=True, help="Filter notes written today")
@click.option("-w", "--week", is_flag=True, help="Filter notes written this week")
@click.option("-m", "--month", is_flag=True, help="Filter notes written this month")
def listnotes(today:bool, week:bool, month:bool) -> None:
    """List all notes with optional flags/filters"""
    try:
        notes = read_notes()
        if today:
            what_to_show = [(index,message[1]) for index,message in enumerate(notes) if is_within_today(message[0])]
        if week:
            what_to_show = [(index,message[1]) for index,message in enumerate(notes) if is_within_this_week(message[0])]
        if month:
            what_to_show = [(index,message[1]) for index,message in enumerate(notes) if is_within_this_month(message[0])]
        else:
            what_to_show = [(index,message[1]) for index,message in enumerate(notes)]

        for index, data in enumerate(what_to_show):
            click.echo(f"{index}: {data[1]}")
    except Exception as e:
        click.echo(click.style(f"Some error occured. {e}", fg="red"))


@main.command()
@click.option("-c", "--count", type=int, default=1, help="Returns last -c latest notes")
def latest(count:int=1) -> None:
    """Display the latest notes."""
    try:
        data = get_latest_notes(count)
        for _, data in enumerate(data):
            click.echo(f"{data[1]}")
    except Exception as e:
        click.echo(click.style(f"Some error occured. {e}", fg="red"))


@main.command()
@click.option("-n", "--linenumbers", help="Comma seperated line/s which needs to be deleted")
@click.option("--recent", is_flag=True, help="Delete last added note")
def delete(linenumbers:str, recent:str) -> None:
    """Delete notes by line number or the most recent note."""
    try:
        indices = []
        if linenumbers:
            indices = [int(i) for i in linenumbers.split(",")]
        
        if recent:
            notes = read_notes()
            indices = [len(notes)-1] # getting all notes
        
        deleted_count = delete_notes(indices)
        click.echo(click.style(f"{deleted_count} note(s) deleted", fg="green"))
    except Exception as e:
        click.echo(click.style(f"Some error occured. {e}", fg="red"))

@main.command()
@click.option("-m", "--message", prompt=True, help="Enter the message that needs to be saved")
def addnote(message:str) -> None:
    """Enter the message that needs to be saved"""
    try:
        add_note(message)
        click.echo(click.style("Message added successfully", fg='green'))
    except Exception as e:
        click.echo(click.style(f"Some error occured. {e}", fg="red"))