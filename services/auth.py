def login():
    users = {
        "admin": "admin123",
        "staff": "staff123"
    }
    print("🔐 Login Required")
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print("✅ Login successful")
        return True
    else:
        print("❌ Invalid credentials")
        return False
