## SAS User Global Forum 2020: Presentation:  - Using Python to Maximize Limited SAS® Viya® Resources 

### **Introduction:**

### **Getting Started:**
##### This assumes you're comfortable with setting up python and connecting to CAS via swat. If you're a little unsure, I'd recommend looking at [Official SWAT Documenation](https://sassoftware.github.io/python-swat/)
##### I'm also assuming that you're connecting to a SQL Server DB.  You may have to create your own connection class tha generates the needed connection object. 

1. Clone Repo

    `git clone https://github.com/willhaley-bne/SASUGF-2020-Python-Viya-Limited-Resources`
    
2. Set Up Python Environment (developed on 3.7)

    `cd SASUGF-2020-Python-Viya-Limited-Resources`  
    `python -m venv venv`  
    `source venv\bin\activate`  
    `pip install -r requiremnets.txt` 
    
3. Update Code with your connection information

    ###### Connections/ViyaConnection.py  
    `  url = None`  
    `  user_name = None`  
    `  password = None`  
    `  port = None`
    ###### Connections/Warehouse.py  
    `server = None`  
    `username = None`  
    `password = None`  
    `driver = '/opt/microsoft/msodbcsql/lib64/libmsodbcsql-13.1.so.9.2'`  

4. Update Example Report with your own information
    ###### Reports/ExampleReport.py  
    `source_sql = ''`    
    `cas_table_name = ''`  
    `caslib = ''` 

5. Make sure your have the CAS_CLIENT_SSL_CA_LIST environment variable set 

### **Examples:**


