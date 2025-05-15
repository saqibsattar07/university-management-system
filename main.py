from services.auth import login
from services.menu import run_menu

if __name__ == "__main__":
    if login():
        run_menu()
