"""
Coordonator aplicatie.
Autor: Arsene Robert
"""

from ui.console import Console

# Functie principala care ruleaza aplicatia
def run_app():
    """
    Ruleaza aplicatia.
    Input: -.
    Output: -.
    """
    ui = Console()
    ui.showUi()

if __name__ == "__main__":
    run_app()