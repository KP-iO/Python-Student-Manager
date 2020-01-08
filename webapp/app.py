from flask import Flask, render_template, redirect, url_for, request

from student import Student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_name = request.form.get("student-name", "")
        new_student_age = request.form.get("age", "")
        new_student_town = request.form.get("town", "")

        new_student = Student(name=new_student_name, age=new_student_age, town=new_student_town)
        students.append(new_student)

        return redirect(url_for(students_page))
    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
