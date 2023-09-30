import sqlite3
import os 

if not os.path.exists('data'):
    os.makedirs('data')

def initialize_database():
    # Connect to SQLite database. If the database doesn't exist, it will be created.
    conn = sqlite3.connect('data/flashcards.db')
    
    # Create a table named 'Flashcards'
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS Flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            category TEXT
        );
        ''')
    print("Database initialized and Flashcards table created.")

# Function to add a new flashcard to the Flashcards table
def add_flashcard(question, answer, category):
    conn = sqlite3.connect('data/flashcards.db')
    with conn:
        conn.execute("INSERT INTO Flashcards (question, answer, category) VALUES (?, ?, ?)", (question, answer, category))
    print(f"Flashcard added: {question}")

# Function to retrieve all flashcards from the Flashcards table
def get_all_flashcards():
    conn = sqlite3.connect('data/flashcards.db')
    cursor = conn.execute("SELECT * FROM Flashcards")
    flashcards = [{"id": row[0], "question": row[1], "answer": row[2], "category": row[3]} for row in cursor.fetchall()]
    return flashcards

# Function to retrieve flashcards by category from the Flashcards table
def get_flashcards_by_category(category):
    conn = sqlite3.connect('data/flashcards.db')
    cursor = conn.execute("SELECT * FROM Flashcards WHERE category = ?", (category,))
    flashcards = [{"id": row[0], "question": row[1], "answer": row[2], "category": row[3]} for row in cursor.fetchall()]
    return flashcards


# Initialize the database and table
initialize_database()

# Test the add_flashcard function
add_flashcard("What is the capital of France?", "Paris", "Geography")
add_flashcard("What is 2 + 2?", "4", "Math")

# Test the get_all_flashcards function
print("All Flashcards:")
print(get_all_flashcards())

# Test the get_flashcards_by_category function
print("Math Flashcards:")
print(get_flashcards_by_category("Math"))
