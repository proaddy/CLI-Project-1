import csv
import click
from datetime import datetime

def read_notes(file_path="storage/storage.csv") -> None:
    """Read all notes from the storage file."""
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            return [row for row in reader if len(row)==2] # filtering blank lines
    except FileNotFoundError: # if file doesn't exist
        click.echo(click.style("Storage.csv not found.", fg="red"))
        return []
    except Exception as e:
        click.echo(click.style(f"Some unexpected error occured. {e}", fg="red"))
        return []

def add_note(message:str, file_path="storage/storage.csv") -> None:
    """Add a new note with current timestamp"""
    try:
        date = datetime.now().isoformat()
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, message])
    except FileNotFoundError: # if file doesn't exist
        click.echo(click.style("Storage.csv not found.", fg="red"))

def write_notes(new_notes:list, file_path="storage/storage.csv") -> None:
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_notes)
    except FileNotFoundError: # if file doesn't exist
        click.echo(click.style("Storage.csv not found. Cannot write changed into file", fg="red"))

def delete_notes(indices:list, file_path="storage/storage.csv") -> int:
    """Delete the number of indices"""
    notes = read_notes(file_path)
    try: # error handling
        if not notes:
            click.echo(click.style("No note is left to be deleted", fg="yellow"))
            return 0
        changed = [data for index,data in enumerate(notes) if index not in indices]
        write_notes(changed, file_path)
        return len(notes) - len(changed)
    except FileNotFoundError:
        click.echo(click.style("Storage.csv not found.", fg="red"))
        return 0

def get_latest_notes(count, file_path="storage/storage.csv") -> list:
    """Gets the latest `count` notes."""
    try: # error handling
        with open(file_path, "r") as file:
            notes = list(csv.reader(file))
        return notes[-count:]
    except FileNotFoundError:
        click.echo(click.style("Storage.csv not found.", fg="red"))
        return []