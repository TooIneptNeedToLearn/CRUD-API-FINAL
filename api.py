import pymysql
from app import app
from config import mysql
from flask import jsonify, request, render_template, url_for, redirect

#Authentication via login method in home route
username = "admin"
password = "admin"
logged_in = False

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    global logged_in
    name = request.form['Username']
    pwd = request.form['Password']
    if name == username and pwd == password:
        logged_in = True
        return redirect(url_for('read_index'))
    else:
        return render_template('login.html', info = "Invalid Username and Password")

@app.route('/login/logout')
def logout():
    global logged_in
    logged_in = False
    return redirect(url_for('home'))

#READ
#index that shows the basics of this program
@app.route('/login/intro')
def read_index():
    if logged_in:
        return render_template("intro.html")
    else:
        return render_template("authentication_required.html")

#route that shows all the table
@app.route('/login/tables')
def read_tables():
    if logged_in:
        conn = None
        cursor = None
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlquery = "SELECT * FROM customers"
            cursor.execute(sqlquery)
            all_row = cursor.fetchall()
            response = jsonify(all_row)
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return render_template("authentication_required.html")

    

#route that shows a specific row in the table
@app.route('/login/tables/<int:customers_id>')
def read_selected_row(customers_id):
    if logged_in:
        conn = None
        cursor = None
        try: 
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlquery = "select customers_id,f_name,l_name from customers where customers_id = %s"
            cursor.execute(sqlquery, customers_id)
            customer_row = cursor.fetchone()
            response = jsonify(customer_row)
            return response
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return render_template("authentication_required.html")


#POST
@app.route('/login/create', methods = ['POST'])
def create_add_input():
    if logged_in:
        conn = None
        cursor = None
        try:
            _json = request.json
            customers_id = _json['customers_id']
            f_name = _json['f_name']
            l_name = _json['l_name']
            if customers_id and f_name and l_name and request.method == 'POST':
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                sqlquery = "insert into customers(customers_id, f_name, l_name) values (%s ,%s, %s)"
                bind_var = (customers_id, f_name, l_name)
                cursor.execute(sqlquery, bind_var)
                conn.commit()
                response = jsonify("Added to table successfully")
                response.status_code = 200
                return response
            else:
                return errormess()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return render_template("authentication_required.html")

#PUT
@app.route('/login/update', methods = ['PUT'])
def update_row():
    if logged_in:
        conn = None
        cursor = None
        try:
            _json = request.json
            customers_id = _json['customers_id']
            f_name = _json['f_name']
            l_name = _json['l_name']
            if customers_id and f_name and l_name and request.method == 'PUT':
                sqlquerry = "update customers set f_name = %s, l_name = %s where customers_id = %s"
                bind_var = (f_name, l_name, customers_id)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sqlquerry,bind_var)
                conn.commit()
                response = jsonify(f"row {customers_id} values updated successfully")
                response.status_code = 200
                return response
            else:
                errormess()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return render_template("authentication_required.html")


#DELETE
@app.route('/login/delete/<int:customers_id>', methods=['DELETE'])
def delete_row(customers_id):
    if logged_in:
        conn = None
        cursor = None
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            sqlquery = "delete from customers where customers_id = %s"
            cursor.execute(sqlquery,(customers_id,))
            conn.commit()
            respone = jsonify(f'row {customers_id} deleted successfully!')
            respone.status_code = 200
            return respone
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    else:
        return render_template("authentication_required.html")

#error handler that will print a message if you got 404
@app.errorhandler(404)
def errormess(error=None):
    message = {
        'Status': 404,
        'Message': "Record not found" + request.url
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True)