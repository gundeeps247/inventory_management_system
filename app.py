from flask import *
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import cv2
import numpy as np
import mysql.connector
import bcrypt
#import pytesseract


app = Flask(__name__, template_folder='templates')
app.secret_key="sndjsndnsjndnmlksml"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/loginpage")
def loginpage():
    return render_template("loginpage.html")
    
@app.route("/signuppage")
def signuppage():
    return render_template("signuppage.html")

@app.route("/add")
def adde():
    return render_template("add.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get the submitted form data
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Store the new user in the users list
        cnx=mysql.connector.connect(user='root',password='1234',host='localhost',database='ims_users')
        cursor=cnx.cursor()
        cursor.execute("select * from user;")
        data=cursor.fetchall()
        for row in data:
            if username==row[0]:
                #message alert
                return render_template('signuppage.html', errors="Error:Username already in use!")
        cnx.commit()
        add_user=("insert into user(userid,password) VALUES (%s, %s)")
        cursor.execute(add_user, (username,hashed_password)) 
        cnx.commit()
        cursor.close()
        cnx.close()

        #create table
        cnx=mysql.connector.connect(user='root',password='1234',host='localhost',database='ims')
        cursor=cnx.cursor()
        cursor.execute("create table product"+username+"(Serial_No varchar(100),Product_Name varchar(100), Price float);")
        cnx.commit()
        cursor.close()
        cnx.close()

        # Redirect to the login page   
        return redirect(url_for("loginpage"))

    return render_template("signuppage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get the submitted form data
        username = request.form.get("username")
        password = request.form.get("password")

        cnx=mysql.connector.connect(user='root',password='1234',host='localhost',database='ims_users')
        cursor=cnx.cursor()
        cursor.execute("select * from user;")
        data=cursor.fetchall()
        for row in data:
            if username==row[0] and bcrypt.checkpw(password.encode("utf-8"), row[1].encode("utf-8")) :
                session['user']=username
                return redirect("/inventory")

        # Login failed
        return render_template("loginpage.html",errors="Error:Invaild Credentials!")

    return render_template("loginpages].html")

@app.route('/add_product', methods=['POST'])
def add_product():
    # Get the data from the form
    image = request.files.get('image')
    serial = request.form.get('serial')
    pdt_name = request.form.get('product_name')
    price = request.form.get('price')
    
    if image:
        image.save('./test.jpg')
        img = cv2.imread("test.jpg")
        barcodes = decode(img)

        if barcodes:
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

                barcode_data = barcode.data.decode("utf-8")
                #barcode_type = barcode.type
                #text = f"{barcode_data} ({barcode_type})"
                # cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                serial=barcode_data
    cnx=mysql.connector.connect(user='root',password='1234',host='localhost',database='ims')
    cursor=cnx.cursor()
    add_prd=("insert into product"+session['user']+"(Serial_No, Product_Name, price) VALUES (%s, %s, %s)")
    cursor.execute(add_prd, (serial,pdt_name, price))
    cnx.commit()
    cursor.close()
    cnx.close
    return render_template("add.html")
        
    
@app.route('/inventory')
def show_inventory():
    # Get the data from the form
    cnx=mysql.connector.connect(user='root',password='1234',host='localhost',database='ims')
    cursor=cnx.cursor()
    cursor.execute("select Product_Name,Price,count(serial_no) from product"+session['user']+" group by Product_Name,price;")
    data=cursor.fetchall()
    return render_template("inventory.html",prd_data=data)

@app.route('/inventory/<name>')
def individual(name=None):
    cnx=mysql.connector.connect(user='root',password='1234',host='localhost',database='ims')
    cursor=cnx.cursor()
    cursor.execute("select * from product"+session['user']+" where Product_Name='"+name+"';")
    data=cursor.fetchall()

    return render_template('inventorylist.html', iprd_data=data)

if __name__ == '__main__':
    app.run(debug=True)
