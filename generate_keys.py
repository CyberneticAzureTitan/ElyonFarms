import pickle
from pathlib import Path
import streamlit_authenticator as stauth

passwords = ["password123", "password456"]

hasher = stauth.Hasher()
hashed_passwords = [hasher.hash(pw) for pw in passwords]

file_path = Path(__file__).parent / "hashed_passwords.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

print("Hashed passwords saved successfully!")
