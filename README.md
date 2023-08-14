
# Note Taking App with Python and MySQL database
A simple lightweight note taking app with GUI made with Python and MySQL database.
- Uses Tkinter for UI.
- Uses Pymysql for integration of MySQL database.

  ![App Screenshot](https://github.com/Cyber-Zypher/Note-Taking-App-GUI/blob/f76c7aa0b6087b5f89912dbf0d76c59c2238f252/Note%20Taking%20App.gif)

## Install the required Libraries.

Clone the project

```
pip install pymysql
```
or
```
python -m pip install pymysql
```

## Initialize the database
```
CREATE DATABASE note_taking_app;
USE note_taking_app;

CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```

## Authors

- [@sidharth_everett](https://github.com/Cyber-Zypher)

