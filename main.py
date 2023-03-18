import pymysql
from flask import Flask, render_template
from sql_commands import create_tables, insert_values
from requestsAndPlot import r1, connect
import plotly.graph_objects as go


def initDB():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='alternance',
    cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()  

    # create_tables(False, cursor)
    insert_values(cursor)

    connection.commit()
    connection.close()


app = Flask(__name__)

@app.route('/')
def home():
    command = '''SELECT s.libelle_specialite, COUNT(*) AS nombre_etudiants FROM Diplome d JOIN Specialite s ON s.id_specialite = d.id_specialite JOIN Apprenti a ON a.id_diplome = d.id_diplome GROUP BY s.libelle_specialite;'''
    cursor = connect()
    cursor.execute(command)

    rows = cursor.fetchall()




    y_data = [row['libelle_specialite'] for row in rows]  # get values of 'libelle_specialite'
    x_data = [row['nombre_etudiants'] for row in rows]  # get values of 'nombre_etudiants'

    # create the pie chart with Plotly
    fig = go.Figure(data=[go.Pie(labels=y_data, values=x_data)])

    # set the layout of the chart
    fig.update_layout(title='Nombre d\'étudiants par spécialité', width=800, height=800)


    # get the HTML of the chart
    graph_html = fig.to_html(full_html=False)

    return render_template("index.html", graph_html=graph_html)






if __name__ == "__main__":
    app.run(debug=True)




