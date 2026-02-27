from flask import Flask, render_template, request, redirect
from db_config import get_connection

app = Flask(__name__, template_folder="../frontend")

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT FIR.fir_id, Complainant.name, Crime_Category.category_name, FIR.status
        FROM FIR
        JOIN Complainant ON FIR.complainant_id = Complainant.complainant_id
        JOIN Crime_Category ON FIR.category_id = Crime_Category.category_id
    """)
    records = cursor.fetchall()
    conn.close()
    return render_template("index.html", records=records)

@app.route("/add", methods=["GET", "POST"])
def add_fir():
    if request.method == "POST":
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Complainant (name, phone, address) VALUES (%s,%s,%s)",
                       (request.form["name"], request.form["phone"], request.form["address"]))
        conn.commit()

        complainant_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO FIR (complainant_id, officer_id, category_id, description, date_filed)
            VALUES (%s, 1, 1, %s, CURDATE())
        """, (complainant_id, request.form["description"]))

        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("add_fir.html")

if __name__ == "__main__":
    app.run(debug=True)
