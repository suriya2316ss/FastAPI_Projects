### **Requirements**
	-pip install sqlalchemy
	-pip install fastapi
	-pip install uvicorn
	-pip install pyschopg2-binary
	-pip install python-dotenv




#### **ORM-OBJECT RELATIONAL MAPPING**

Defeniton:

&nbsp;     ORM is a technique that allows you to interact with a database using Python classes and objects instead of writing raw SQL queries.



In python,

-class consider as a table in db.

-objects consider as a row.

-Attribute consider as a column.

-Method consider as an SQL querry.





simple words:

&nbsp;     -python code instead of sql code.



------------------------------------------------------------------------------------------------------------------------------------------------------



#### **SQLALCHEMY**



Defenition:Sqlalchemy is a Python library used to work with  relational databases using both raw SQL and ORM features.It is also called as database toolkit.

-It makes  database operations easier,safer,and more pythonic.

-connect databses

-create table using python classes

-perform CRUD operations

-Suport Many databases(SQLite,MySQL,PosgreSQL)



#### 

#### **create\_engine**

&nbsp;	-create\_engine() is a function in SQLAlchemy that creates a connection object to the database.

&nbsp;	-Engine handles database communication

&nbsp;	-All queries go through the engine

#### **Session / sessionmaker**

&nbsp;	-Database operations require a session, like a temporary workspace.

&nbsp;		-Opening a transaction

&nbsp;		-Writing and reading data

&nbsp;		-Committing or rolling back changes

#### 

#### **Declarative Base**

&nbsp;	-declarative\_base() is used to create a base class for ORM models.

&nbsp;	-Any class that represents a database table must inherit from this base.

#### **dotenv**

&nbsp;-dotenv is a Python library that loads environment variables from a .env file.

&nbsp;-Storing the sensitive data

&nbsp;	-Database passwords

&nbsp;	-API keys

&nbsp;	-Secret keys

#### &nbsp;**load\_dotenv**

	-Function from dotenv that loads the .env file into Python environment variables.

&nbsp;	-Secure credential handling.

&nbsp;	-No plain passwords in code.


#### **Pydantic**
	-Pydantic is a Python library used mainly for data validation and settings management using Python type hints. It is commonly used in FastAPI and other modern Python projects.
			-Ensures that the data you work with is valid and matches expected types.
			-Automatically parses and validates data (from JSON, dicts, etc.).
			-Makes your code safer and cleaner.


### **Run the program**
 -uvicorn main:app --host 0.0.0.0 --port 8000 --reload