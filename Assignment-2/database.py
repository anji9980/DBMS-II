import psycopg2
def unique(list1):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    list1 = unique_list

commands = (
    
     """  CREATE TABLE Author
(
  Name_ VARCHAR(500) NOT NULL,
  PRIMARY KEY (Name_)
)""",

"""CREATE TABLE Venue
(
  Name VARCHAR(500) NOT NULL,
  PRIMARY KEY (Name)
)""",

"""CREATE TABLE Research_paper
(
  Year_of_publication INT NOT NULL,
  Abstract VARCHAR(100000) NOT NULL,
  id INT NOT NULL,
  paper_title VARCHAR(100000) NOT NULL,
  Name VARCHAR(500) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (Name) REFERENCES Venue(Name)
)""",

"""CREATE TABLE List_of_Authors
(
  Order_ INT NOT NULL,
  id INT NOT NULL,
  Name_ VARCHAR(500) NOT NULL,
  PRIMARY KEY (id, Name_),
  FOREIGN KEY (id) REFERENCES Research_paper(id),
  FOREIGN KEY (Name_) REFERENCES Author(Name_)
)""",

"""CREATE TABLE Citation
(
  id_1 INT NOT NULL,
  Citationid_2 INT NOT NULL,
  PRIMARY KEY (id_1, Citationid_2),
  FOREIGN KEY (id_1) REFERENCES Research_paper(id),
  FOREIGN KEY (Citationid_2) REFERENCES Research_paper(id)
)"""
        )


conn = None
total_authors =[]
venues= []
pap_title=[]
year = 0
index =-11
abstract = []
author_name=[]
try:
    conn = psycopg2.connect(
    host="localhost",
    database="alpha",
    user="postgres",
    password="Kaushik2002@")
    cur = conn.cursor()
        # create table one by one
    #for command in commands:
     #   cur.execute(command)
        # close communication with the PostgreSQL database server
    
    
    f = open("source.txt", encoding = "utf-8")

    statements = f.readlines()
    
    
    
    for x in range(629814) :
     str = statements
     if str[0:1] == "#@":
      author_name = str[2:].split(',')
      unique(author_name)
      for i in author_name:
          if i not in total_authors:
              total_authors.append(i)
              sql = """ INSERT INTO Author VALUES(%s) """ 
              cur.execute(sql,[i])

      
     if str[0:1] == "#*":
      pap_title = str[2:]
     if str[0:1] == "#t":
         year = str[2:]
     if str[0:1] == "#c":
         venue = str[2:]
         if venue not in venues:
             sql = """ INSERT INTO venue VALUES(%s) """ 
             cur.execute(sql,[venue])
             venues.append(venue)
     if str[0:5] == "#index":
         index = str[6:]
     if str[0:1] == "#%":
         references = str[2:]
     if str[0:1] == "#c":
         abstract = str[2:]
    sql = """ INSERT INTO Research_paper VALUES (%s %s %s)"""
    cur.execute(sql,[pap_title,year,abstract ])
    for i in author_name :
         sql = """ INSERT INTO Author_and_co-Authors VALUES(%s %s %s)"""
         cur.execute(sql,[i.index(),pap_title,i])
    conn.commit()
    cur.close()       
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()


