from cli.commands import main as cli_main
from gui.main import main as gui_main
import sys

def main() -> None:
    if len(sys.argv) > 1 and (sys.argv[1] == "gui" or sys.argv[1] == "GUI" or sys.argv[1] == 'interactive'):
        gui_main()
    else:
        cli_main()

if __name__ == "__main__":
    main()