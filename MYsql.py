# import mysql.connector

# # Step 1: Establish a connection to the MySQL database
# def connect_to_db():
#     return mysql.connector.connect(
#         host="localhost", 
#         user="root",       
#         password="ashish", 
#         database="users"  
#     )

# # Step 2: Create a table (if it doesn't already exist)
# def create_table(cursor):
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(255) NOT NULL,
#             age INT NOT NULL,
#             email VARCHAR(255) UNIQUE NOT NULL
#         )
#     ''')

# # Step 3: Insert data into the table
# def insert_user(cursor, name, age, email):
#     cursor.execute('''
#         INSERT INTO users (name, age, email) VALUES (%s, %s, %s)
#     ''', (name, age, email))

# # Step 4: Retrieve and display all users
# def get_users(cursor):
#     cursor.execute("SELECT * FROM users")
#     return cursor.fetchall()

# # Step 5: Update a user
# def update_user(cursor, user_id, name=None, age=None, email=None):
#     fields = []
#     values = []
#     if name:
#         fields.append("name = %s")
#         values.append(name)
#     if age:
#         fields.append("age = %s")
#         values.append(age)
#     if email:
#         fields.append("email = %s")
#         values.append(email)
#     values.append(user_id)

#     query = f"UPDATE users SET {', '.join(fields)} WHERE id = %s"
#     cursor.execute(query, values)

# # Step 6: Delete a user
# def delete_user(cursor, user_id):
#     cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))

# # Main function to demonstrate functionality
# if __name__ == "__main__":
#     # Connect to the database
#     conn = connect_to_db()
#     cursor = conn.cursor()

#     # Create table
#     create_table(cursor)

#     # Insert users
#     insert_user(cursor, 'Ashish ', 19, 'ashis@gmail.com')
#     insert_user(cursor, 'mehra', 15, 'Ashii@gmail.com')
#     insert_user(cursor, 'priyanshu', 12, 'Aryan9@gmail.com')


#     # Commit changes to the database
#     conn.commit()

#     # Retrieve and display all users
#     users = get_users(cursor)
#     print("Users:", users)

#     # Update user with ID 1
#     update_user(cursor, 2, name='Guddu Ellis', age=18)
    
#     # Delete user with ID 2
#     delete_user(cursor, 2)

#     # Retrieve users after update and delete
#     conn.commit()
#     users = get_users(cursor)
#     print("Updated Users:", users)

#     # Close the connection
#     cursor.close()
#     conn.close()



import mysql.connector

# Step 1: Establish a connection to the MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost", 
        user="root",       
        password="ashish", 
        database="users"  
    )

# Step 2: Drop the table (if it exists) and create a new table
def recreate_table(cursor):
    cursor.execute('DROP TABLE IF EXISTS users')  # Drop table if it exists
    cursor.execute('''
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL
        )
    ''')

# Step 3: Insert data into the table
def insert_user(cursor, name, age, email):
    cursor.execute('''
        INSERT INTO users (name, age, email) VALUES (%s, %s, %s)
    ''', (name, age, email))

# Step 4: Retrieve and display all users
def get_users(cursor):
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Step 5: Update a user
def update_user(cursor, user_id, name=None, age=None, email=None):
    fields = []
    values = []
    if name:
        fields.append("name = %s")
        values.append(name)
    if age:
        fields.append("age = %s")
        values.append(age)
    if email:
        fields.append("email = %s")
        values.append(email)
    values.append(user_id)

    query = f"UPDATE users SET {', '.join(fields)} WHERE id = %s"
    cursor.execute(query, values)

# Step 6: Delete a user
def delete_user(cursor, user_id):
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Connect to the database
    conn = connect_to_db()
    cursor = conn.cursor()

    # Drop and recreate the table
    recreate_table(cursor)

    # Insert users
    insert_user(cursor, 'Ashish ', 19, 'ashis@gmail.com')
    insert_user(cursor, 'mehra', 15, 'Ashii@gmail.com')
    insert_user(cursor, 'priyanshu', 12, 'Aryan9@gmail.com')

    # Commit changes to the database
    conn.commit()

    # Retrieve and display all users
    users = get_users(cursor)
    print("Users:", users)

    # Update user with ID 2
    update_user(cursor, 2, name='Guddu Ellis', age=18)

    # Delete user with ID 2
    delete_user(cursor, 2)

    # Commit changes after update and delete
    conn.commit()

    # Retrieve users after update and delete
    users = get_users(cursor)
    print("Updated Users:", users)

    # Close the connection
    cursor.close()
    conn.close()
