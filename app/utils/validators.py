from rich.console import Console

console = Console()

def validate_input(password: str) -> bool:
    """Basic validation: not empty, not only spaces."""
    return bool(password and password.strip())

def feedback(passed, failed):
    console.print("\nPassword Analysis Report:")
    console.print("-" * 30)
    if passed:
        console.print("✔ Passed checks:")
        for item in passed:
            console.print(f"   - {item}")
    else:
        console.print("No conditions are met")
    if failed:
        console.print("\n✘ Failed checks:") 
        for item in failed:
            console.print(f"   - {item}")
    else:
        console.print("All conditions are met")

def strength_score(passedLength, total):
    score = passedLength / total * 100
    console.print(f"\nStrength Score: {score:.0f}%")
    if score == 100:
        console.print("Excellent! Strong paassword.")
    elif score >= 60:
        console.print("Good, but can be improved.")
    else:
        console.print("Weak password. Consider changes.")