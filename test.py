import pymysql

# Connect to the MySQL server.
conn = pymysql.connect(host='10.2.1.88', port='3306', user='admin', password='admin')

# Create a cursor object to execute queries.
cur = conn.cursor()

# Prompt the user to choose between logging in or registering.
choice = input('Enter 1 to login or 2 to register: ')

if choice == '1':
  # If the user chose to login, prompt them to enter their username and password.
  username = input('Enter your username: ')
  password = input('Enter your password: ')

  # Execute a query to retrieve the user with the entered username and password.
  query = 'SELECT * FROM users WHERE username = %s AND password = %s'
  cur.execute(query, (username, password))

  # Check if the query returned a result.
  if cur.rowcount > 0:
    # If the query returned a result, print a success message.
    print('Successfully logged in!')
  else:
    # If the query did not return a result, print an error message.
    print('Invalid username or password.')
else:
  # If the user chose to register, prompt them to enter their desired username and password.
  username = input('Enter your desired username: ')
  password = input('Enter your desired password: ')

  # Execute a query to insert the new user into the database.
  query = 'INSERT INTO users (username, password) VALUES (%s, %s)'
  cur.execute(query, (username, password))

  # Commit the transaction to save the new user to the database.
  conn.commit()

  # Print a success message.
  print('Successfully registered!')

# Close the cursor and connection to the database.
cur.close()
conn.close()
