from app.core import password_analyzer
from app.utils import validate_input, feedback, strength_score
from rich.console import Console

console = Console()

def run():
    analyzer = password_analyzer()
    while True:
        pwd = input("\nEnter password (or type 'exit' to quit): ")
        if pwd.lower() == 'exit':
            console.print("Exiting program. Stay secure!")
            break
        if not (validate_input(pwd)):
            console.print("Invalid input. Try again.")
            continue
        passed, failed = analyzer(pwd)
        console.print('Passed rules: ', passed)
        console.print('Failed rules: ', failed)
        feedback(passed, failed)
        strength_score(len(passed), len(passed) + len(failed))

if __name__ == "__main__":
    run()