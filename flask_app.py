from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cardealershipdb'

def get_db_connection():
    conn = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    return conn

def get_table_data(table):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {table}')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/designers', methods=['GET', 'POST'])
def designers():
    if request.method == 'POST':
        designername = request.form['designername']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO designer (designername) VALUES (%s)', (designername,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('designers'))

    show_data = request.args.get('show_data') == 'true'
    designers = get_table_data('designer') if show_data else []
    return render_template('designers.html', designers=designers, show_data=show_data)

@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    if request.method == 'POST':
        suppliername = request.form['suppliername']
        address = request.form['address']
        supplierrating = request.form['supplierrating']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO supplier (suppliername, address, supplierrating) VALUES (%s, %s, %s)',
                       (suppliername, address, supplierrating))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('suppliers'))

    show_data = request.args.get('show_data') == 'true'
    suppliers = get_table_data('supplier') if show_data else []
    return render_template('suppliers.html', suppliers=suppliers, show_data=show_data)

@app.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'POST':
        employeename = request.form['employeename']
        position = request.form['position']
        department = request.form['department']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO employee (employeename, position, department) VALUES (%s, %s, %s)',
                       (employeename, position, department))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('employees'))

    show_data = request.args.get('show_data') == 'true'
    employees = get_table_data('employee') if show_data else []
    return render_template('employees.html', employees=employees, show_data=show_data)

@app.route('/manages', methods=['GET', 'POST'])
def manages():
    if request.method == 'POST':
        manager_id = request.form['manager_id']
        employee_id = request.form['employee_id']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO manages (manager_id, employee_id) VALUES (%s, %s)', (manager_id, employee_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('manages'))

    show_data = request.args.get('show_data') == 'true'
    manages = get_table_data('manages') if show_data else []
    return render_template('manages.html', manages=manages, show_data=show_data)

@app.route('/production_lines', methods=['GET', 'POST'])
def production_lines():
    if request.method == 'POST':
        location = request.form['location']
        capacity = request.form['capacity']
        manager_id = request.form['manager_id']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO production_line (location, capacity, manager_id) VALUES (%s, %s, %s)',
                       (location, capacity, manager_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('production_lines'))

    show_data = request.args.get('show_data') == 'true'
    production_lines = get_table_data('production_line') if show_data else []
    return render_template('production_lines.html', production_lines=production_lines, show_data=show_data)


@app.route('/car_model', methods=['GET', 'POST'])
def car_model():
    if request.method == 'POST':
        model_name = request.form['model_name']
        manufacturer = request.form['manufacturer']
        price = request.form['price']
        year = request.form['year']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO car_model (model_name, manufacturer, price, year) VALUES (%s, %s, %s, %s)',
                       (model_name, manufacturer, price, year))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('car_model'))

    show_data = request.args.get('show_data') == 'true'
    car_models = get_table_data('car_model') if show_data else []

    return render_template('car_model.html', car_models=car_models, show_data=show_data)


if __name__ == '__main__':
    app.run(debug=True)
