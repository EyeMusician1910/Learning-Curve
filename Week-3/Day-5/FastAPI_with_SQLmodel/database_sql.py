import sqlite3
from pathlib import Path
from typing import Any
from .api.schemas.shipment import ShipmentCreate, ShipmentUpdate
from contextlib import contextmanager


DATABASE_PATH = Path(__file__).resolve().parent / "sqlite2.db"


class Database:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect_to_db(self):
        #make the connection    
        self.conn=sqlite3.connect(DATABASE_PATH,check_same_thread=False)#Both connections cannot run on the same thread

        self.cur=self.conn.cursor()
        print("connection established")

    #Creating a table this doesn't work as you can't use plcaholders in the CREATE TABLE queries
    # def crate_table(self):
    #     self.cur.execute("""CREATE TABLE IF NOT EXISTS ? 
    #            (id INTEGER PRIMARY KEY,
    #            contenr TEXT,
    #            weight REAL,
    #            status TEXT)
    #            """,(name,))
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS shipment 
               (id INTEGER PRIMARY KEY,
               content TEXT,
               weight REAL,
               status TEXT)
               """)

    def create(self,shipment:ShipmentCreate)-> int:
        self.cur.execute("""SELECT MAX(id) FROM shipment""")
        result=self.cur.fetchone()
        new_id=(result[0] or 0) + 1
        #Inserting values into the table
        self.cur.execute("""
               INSERT INTO shipment
               VALUES(:id,:content,:weight,:status)
               """,
               {
                   "id":new_id,
                   **shipment.model_dump(),
                   "status": "placed",
               }
               )
        self.conn.commit()
        return new_id
         
    #Read a row
    def get(self,id : int)-> dict[str,Any] | None:
        self.cur.execute("""
            SELECT * FROM shipment
            WHERE id=?
            """,(id,))
        row=self.cur.fetchone()
        if row is None:
            return None
        return{
            "id":row[0],
            "content":row[1],
            "weight":row[2],
            "status":row[3],
        }
    #Update a Row    
    def update(self,id:int,shipment: ShipmentUpdate)-> dict[str,Any]:
        self.cur.execute("""
               UPDATE shipment
               SET status=:status
               WHERE id=:id
               """,
               {
                   "id":id,
                   **shipment.model_dump()
               })
        self.conn.commit()
        
        return self.get(id)

    def delete(self,id:int):
        self.cur.execute("""
                DELETE FROM shipment
                WHERE id=?
                """,(id,))
        self.conn.commit()
    def close(self):
        if self.conn is not None:
            print("Connection closed")
            self.conn.close()
            self.conn = None
            self.cur = None
    # def __enter__(self):
    #     print("enter the context")
    #     self.connect_to_db()
    #     self.create_table()
    #     return self
    # def __exit__(self,*args):
    #     print("exit the context")
    #     self.close()
#If we try to run this on any module or package we're importing,we can't use this
#that's why we need to create a method to instatiate the db
#Use contextmanager to make this usable as we can't define the enter and exit functions for this
@contextmanager
def managed_db():
    db=Database()
    print("enter the context")
    db.connect_to_db()
    db.create_table()
    yield db
    print("exit the context")
    db.close()



# with managed_db() as db:
#     shipment = db.get(2204)
#     print(shipment)
#     input("Press Enter to close...")
        
        
        
        
        
        
# connection=sqlite3.connect("sqlite.db")
# cursor=connection.cursor()      

# # cursor.execute("""ALTER TABLE shipment
# # RENAME COLUMN content TO content;""")
# # connection.commit()
# cursor.execute("""CREATE TABLE IF NOT EXISTS shipment 
#                (id INTEGER PRIMARY KEY,
#                content TEXT,
#                weight REAL,
#                status TEXT)
#                """)
# cursor.execute("""
#                INSERT INTO shipment
#                VALUES(:id,:content,:weight,:status)
#                """,
#                {
#                    "id":2204,
#                    "content":"glassware",
#                    "weight":6,
#                    "status": "placed",
#                }
#                )
# connection.commit()

 

# cursor.execute("""DROP TABLE shipment""")
# connection.commit()


#commenting out as nothing needs to be inserted right now
#2. Insert Rows


# #3. Reading the shipment by id


#4. Update Operation 
#can also use the Query Parameters
#id=2201
#status="in_transit"
# cursor.execute(f"""
#                UPDATE shipment
#                SET status={status}
#                WHERE id={id}
#                """)
# connection.commit()
#Not reccomended as it can change the datatypes as there's no type validation

# cursor.execute("""
#                UPDATE shipment
#                SET status='in_transit'
#                WHERE id=2201
#                """)
# connection.commit()


#5. Delete Operation
# cursor.execute("""
#                DELETE FROM shipment
#                WHERE id=2201
#                """)
# connection.commit()



#close the connection when we're
# connection.close()
