import os
import subprocess

def run_phishing_script():
    print("Starting phishing script...")
    subprocess.run(["python3", "phishingscript.py", "--host", "127.0.0.1", "--port", "5000"])

def start_web_server():
    print("Starting local web server...")
    subprocess.run(["python3", "-m", "http.server", "80"])

def start_flask_server():
    print("Starting Flask server...")
    subprocess.run(["python3", "app.py"])

if __name__ == "__main__":
    print("White Rose Setup Script")
    print("1. Run Phishing Script")
    print("2. Start Web Server")
    print("3. Start Flask Server")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        run_phishing_script()
    elif choice == "2":
        start_web_server()
    elif choice == "3":
        start_flask_server()
    else:
        print("Invalid choice.")

