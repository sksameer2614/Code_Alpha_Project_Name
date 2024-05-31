import sqlite3
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Step 1: Setup the Database
def setup_database():
    conn = sqlite3.connect('stock_portfolio.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS portfolio (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        stock_symbol TEXT,
                        shares INTEGER,
                        FOREIGN KEY (user_id) REFERENCES users (id))''')
    
    conn.commit()
    conn.close()

# Step 2: User Authentication
def register_user():
    conn = sqlite3.connect('stock_portfolio.db')
    cursor = conn.cursor()
    
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    try:
        cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
        conn.commit()
        print(Fore.GREEN + "Registration is successful!")
    except sqlite3.IntegrityError:
        print(Fore.RED + "Username already exists. Please try again.")
    
    conn.close()

def login_user():
    conn = sqlite3.connect('stock_portfolio.db')
    cursor = conn.cursor()
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    cursor.execute('''SELECT id FROM users WHERE username = ? AND password = ?''', (username, password))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        print(Fore.GREEN + "Login is successful!")
        return user[0]  # Return user ID
    else:
        print(Fore.RED + "Invalid username or password.")
        return None

# Step 3: Portfolio Management
def add_stock(user_id):
    conn = sqlite3.connect('stock_portfolio.db')
    cursor = conn.cursor()
    
    stock_symbol = input("Enter your stock symbol: ")
    shares = int(input("Enter the number of shares to add: "))
    
    cursor.execute('''INSERT INTO portfolio (user_id, stock_symbol, shares) VALUES (?, ?, ?)''', (user_id, stock_symbol, shares))
    conn.commit()
    
    print(Fore.GREEN + "Stock is added to portfolio!")
    conn.close()

def remove_stock(user_id):
    conn = sqlite3.connect('stock_portfolio.db')
    cursor = conn.cursor()
    
    stock_symbol = input("Enter stock symbol to remove: ")
    
    cursor.execute('''DELETE FROM portfolio WHERE user_id = ? AND stock_symbol = ?''', (user_id, stock_symbol))
    conn.commit()
    
    print(Fore.GREEN + "Stock is removed from portfolio!")
    conn.close()

def view_portfolio(user_id):
    conn = sqlite3.connect('stock_portfolio.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT stock_symbol, shares FROM portfolio WHERE user_id = ?''', (user_id,))
    portfolio = cursor.fetchall()
    
    print(Fore.CYAN + "Your Portfolio:")
    for stock in portfolio:
        print(Fore.CYAN + f"Stock: {stock[0]}, Shares: {stock[1]}")
    
    conn.close()

# Main Application
def main():
    setup_database()
    
    while True:
        print(Fore.YELLOW + "1. Register")
        print(Fore.YELLOW + "2. Login")
        print(Fore.YELLOW + "3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            user_id = login_user()
            if user_id:
                while True:
                    print(Fore.YELLOW + "\n1. Add a new Stock")
                    print(Fore.YELLOW + "2. Remove an existing Stock")
                    print(Fore.YELLOW + "3. View stock Portfolio")
                    print(Fore.YELLOW + "4. Logout")
                    user_choice = input("Enter your choice: ")
                    
                    if user_choice == '1':
                        add_stock(user_id)
                    elif user_choice == '2':
                        remove_stock(user_id)
                    elif user_choice == '3':
                        view_portfolio(user_id)
                    elif user_choice == '4':
                        print(Fore.BLUE + "Exiting the Stock Portfolio Tracker Application")
                        break
                    else:
                        print(Fore.RED + "Invalid choice. Please try again.")
        elif choice == '3':
            print(Fore.BLUE + "Exiting the stock portfolio application")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
