

from flask import Flask, render_template, request

import nb_author_id_deployment as nb



app =Flask(__name__)



@app.route("/", methods= ['GET','POST'])
def hello():
    if request.method == "POST":
        usernam = request.form["username"]
        author = nb.author_prediction(usernam)
        
        
        result = author
        
    return render_template("index.html", book_author = result)
    
'''
@app.route("/sub", methods = ['POST'])
def submit() :
    # HTML -> .py
    if request.method == "POST":
        name = request.form["username"]
    # .py -> HTML   
    return render_template("sub.html", n = name)
    '''

if __name__ == "__main__":
    app.run(debug=True)
    
 