from flask import Flask,render_template,request
from main import generate_certificates
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('index.html')

@app.route('/certificate',methods = ['POST', 'GET'])
def certificate():
   name=''
   if(request.method=='POST'):
      p= str(request.form.get('fname'))
      p1=str(request.form.get('lname'))
      name=str(p+' '+p1)
      print(name)
      generate_certificates(name)
      
      return render_template('certificateview.html',name=name)
   else:
      return render_template('certificateview.html',name=name)

if __name__ == '__main__':
   app.run(debug=True)