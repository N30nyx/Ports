from ports import APP, static_APP,Core, localStorage
from ports import tools
import ports

app = APP()
app.db["todo"] = {}
app.db["todo"]["1"] = "Add debug mode"
app.db["todo"]["2"] = "Add markdown support"
app.db["todo"]["[☑️]3"] = "fix whatever is wrong with args"
app.db["todo"]["4"] = "idea: add time to print(request.method)"

@app.route("/")
def index():
  return tools.render_template("index.html",{"ip":tools.get_addr()})

@app.route("/hi/bye/")
def hibye():
  return "hi bye!"

@app.route("/todo/")
def todo():
  tr = ""
  for item in app.db["todo"]:
    val = app.db["todo"][item]
    tr += f"\n<p>{item}. {val}</p>\n"
  return tr



@app.route("/favicon.ico")
def favicon():
  return tools.send_file("www/indra.jpg")






ls = localStorage("webserve.ehnryu.repl.co")








app.run()
