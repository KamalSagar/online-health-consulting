from flask import Flask, render_template, request, flash, url_for, redirect,session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wcnfouooggefbh:9a21b61748763e7903b50940b5e1fa845527ef99f80dc3822267260b678fc269@ec2-18-214-140-149.compute-1.amazonaws.com:5432/d9vfg6lm5ku6nj'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

@app.route('/')
def index():
   return render_template('welcome_page.html')
@app.route('/login')
def log():
   return render_template('login.html')  
@app.route('/register')
def reg():
   return render_template('patient_registration.html')	
@app.route('/dregister')
def dreg():
   return render_template('doc_registration.html')						

@app.route('/ad')
def add_disease():
   return render_template('admin/add_disease.html')
@app.route('/vdoc')
def vdoc():
   return render_template('admin/view_doc.html',doc_register=doc_register.query.all())
@app.route('/vd')
def vd():
   return render_template('admin/view_disease.html',add_disease=add_disease.query.all())
@app.route('/vp')
def view_patient():
   return render_template('admin/view_patient.html',patient_register=patient_register.query.all())
@app.route('/vpf')
def vpf():
   return render_template('admin/view_patient_feed.html',patient_feedback=patient_feedback.query.all())
@app.route('/vpc')
def vdc():
   return render_template('admin/view_patient_contact.html',patient_contact=patient_contact.query.all())
@app.route('/vf')
def vf():
   return render_template('admin/view_doc_feed.html',doc_feedback=doc_feedback.query.all())
@app.route('/vc')
def vc():
   return render_template('admin/view_doc_contact.html',doc_contact=doc_contact.query.all())

@app.route('/home')
def home():
   return render_template('user/patient_home.html')
@app.route('/details/<name>')
def patient_details(name):
   return render_template('user/patient_details.html',patient_register=patient_register.query.filter_by(username='%s'%name))
@app.route('/search')
def search():
   return render_template('user/doc_search.html')
@app.route('/search_details/<name>/<district>')
def search_details(name,district):
   return render_template('user/doc_search_view.html',doc_register=doc_register.query.filter_by(name='%s'%name,district='%s'%district))
@app.route('/m_app/<name>')
def m_app(name):
   return render_template('user/make_appoinment.html',doc_register=doc_register.query.filter_by(username='%s'%name))
@app.route('/prediction')
def prediction():
   return render_template('user/disease_prediction.html')
@app.route('/prediction_details/<name>')
def prediction_details(name):
   return render_template('user/disease_prediction_view.html',add_disease=add_disease.query.filter_by(diseases_name='%s'%name),doc_register=doc_register.query.filter_by(specialised='%s'%name))
@app.route('/rdoc')
def rdoc():
   return render_template('user/related_doc_view.html')
@app.route('/dm_app/<name>')
def dm_app(name):
   return render_template('user/dmake_appoinment.html',doc_register=doc_register.query.filter_by(username='%s'%name))
@app.route('/feedback')
def patient_feedback():
   return render_template('user/patient_feedback.html')
@app.route('/contact')
def patient_contact():
   return render_template('user/patient_contact.html')
@app.route('/f_app/<namme>')
def fix_app1(namme):
   return render_template('user/appointment.html',fix_appoinment=fix_appoinment.query.filter_by(patient_name='%s'%namme))
@app.route('/map')
def map():
   return render_template('user/map.html')
   
@app.route('/dh')
def home1():
   return render_template('doctor/doc_home.html')
@app.route('/dd/<namme>')
def doc_details(namme):
   return render_template('doctor/doc_details.html',doc_register=doc_register.query.filter_by(username='%s'%namme))
@app.route('/dr/<namme>')
def record(namme):
   return render_template('doctor/patient_rcrd.html',make_appointment=make_appointment.query.filter_by(dname='%s'%namme))
@app.route('/df')
def doc_feedback():
   return render_template('doctor/doc_feedback.html')
@app.route('/dc')
def doc_contact():
   return render_template('doctor/doc_contact.html')
@app.route('/fa')
def fix_app():
   return render_template('doctor/fix_appointment.html')
@app.route('/appp/<name>')
def appp(name):
   return render_template('doctor/patient.html',patient_register=patient_register.query.filter_by(username='%s'%name))
class patient_register(db.Model):
	id = db.Column('reg_id', db.Integer, primary_key = True)
	name = db.Column(db.String(200))
	email = db.Column(db.String(200))
	username = db.Column(db.String(200)) 
	password = db.Column(db.String(10))
	r_password = db.Column(db.String(10))
	dob1 = db.Column(db.String(100))
	dob2 = db.Column(db.String(100))
	dob3 = db.Column(db.String(100))
	gender = db.Column(db.String(10))
	phn = db.Column(db.String(100))
	def __init__(self, name, email, username, password, r_password, dob1, dob2, dob3, gender, phn):
		self.name = name
		self.email = email
		self.username = username
		self.password = password
		self.r_password = r_password
		self.dob1 = dob1
		self.dob2 = dob2
		self.dob3 = dob3
		self.gender = gender
		self.phn = phn
	@app.route('/register', methods = ['GET', 'POST'])
	def new():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['username'] or not request.form['password'] or not request.form['r_password'] or not request.form['dob1'] or not request.form['dob2'] or not request.form['dob3'] or not request.form['gender'] or not request.form['phn']:
				flash('Please enter all the fields', 'error')
			else:
				reg = patient_register(request.form['name'], request.form['email'], request.form['username'], request.form['password'], request.form['r_password'], request.form['dob1'], request.form['dob2'], request.form['dob3'], request.form['gender'], request.form['phn'])			 
				db.session.add(reg)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('log'))
		return render_template('patient_registration.html')

class doc_register(db.Model):
	id = db.Column('dreg_id', db.Integer, primary_key = True)
	name = db.Column(db.String(200))
	email = db.Column(db.String(200))
	degree = db.Column(db.String(200))
	specialised = db.Column(db.String(200))
	address = db.Column(db.String(2000))
	district = db.Column(db.String(200))
	username = db.Column(db.String(200)) 
	password = db.Column(db.String(10))
	r_password = db.Column(db.String(10))
	gender = db.Column(db.String(10))
	phn = db.Column(db.String(100))
	def __init__(self, name, email, degree, specialised, address, district, username, password, r_password, gender, phn):
		self.name = name
		self.email = email
		self.degree = degree
		self.specialised = specialised
		self.address = address
		self.district = district
		self.username = username
		self.password = password
		self.r_password = r_password
		self.gender = gender
		self.phn = phn
	@app.route('/dregister', methods = ['GET', 'POST'])
	def new5():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['degree'] or not request.form['specialised'] or not request.form['address'] or not request.form['district'] or not request.form['username'] or not request.form['password'] or not request.form['r_password'] or not request.form['gender'] or not request.form['phn']:
				flash('Please enter all the fields', 'error')
			else:
				dreg = doc_register(request.form['name'], request.form['email'], request.form['degree'], request.form['specialised'], request.form['address'], request.form['district'], request.form['username'], request.form['password'], request.form['r_password'], request.form['gender'], request.form['phn'])			 
				db.session.add(dreg)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('log'))
		return render_template('doc_registration.html')

@app.route('/login', methods=['POST','GET'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	username = request.form['username']
	password = request.form['password']
	session['username']=username
	reg=patient_register.query.filter_by(username=username,password=password).first()
	dreg=doc_register.query.filter_by(username=username,password=password).first()
	if request.form['password'] == '1' and request.form['username'] == 'admin':
		return render_template("admin/add_disease.html")
	if reg is not None:
		return redirect(url_for('patient_details',name=username))
	elif dreg is not None:
		return redirect(url_for('doc_details',namme=username))
	else:
		return render_template("login.html")
		
@app.route('/status/<int:id>' , methods=['POST', 'GET'])
def status(id):
	reg=patient_register.query.filter_by(id=id).delete()
	db.session.commit()
	return redirect(url_for('view_patient'))	
 
@app.route('/status/<int:id>' , methods=['POST', 'GET'])
def status1(id):
	dreg=doc_register.query.filter_by(id=id).delete()
	db.session.commit()
	return redirect(url_for('vdoc'))	

@app.route('/doc_search_view', methods=['POST','GET'])
def search_view():
	if request.method=='GET':
		return render_template('user/doc_search.html')
	search = request.form['search']
	district = request.form['district']
	return redirect(url_for('search_details',name=search,district=district))

@app.route('/disease_prediction_view', methods=['POST','GET'])
def prediction_view():
	if request.method=='GET':
		return render_template('user/disease_prediction.html')
	prediction = request.form['prediction']
	return redirect(url_for('prediction_details',name=prediction))	

class add_doc(db.Model):
	id = db.Column('demo_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	degree = db.Column(db.String(100))
	specialised = db.Column(db.String(100))
	phn = db.Column(db.String(100))
	def __init__(self, name, email, degree, specialised, phn):
		self.name = name
		self.email = email
		self.degree = degree
		self.specialised = specialised
		self.phn = phn
	@app.route('/add_doc', methods = ['GET', 'POST'])
	def new1():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['degree'] or not request.form['specialised'] or not request.form['phn']:
				flash('Please enter all the fields', 'error')
			else:
				demo = add_doc(request.form['name'], request.form['email'], request.form['degree'], request.form['specialised'], request.form['phn'])			 
				db.session.add(demo)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('add_doc'))
		return render_template('admin/add_doc.html')

class add_disease(db.Model):
	id = db.Column('adis_id', db.Integer, primary_key = True)
	diseases_name = db.Column(db.String(100))
	symptoms = db.Column(db.String(100))
	def __init__(self,diseases_name, symptoms):
		self.diseases_name = diseases_name
		self.symptoms = symptoms
	@app.route('/add_disease', methods = ['GET', 'POST'])
	def new2():
		if request.method == 'POST':
			if not request.form['diseases_name'] or not request.form['symptoms']:
				flash('Please enter all the fields', 'error')
			else:
				adis = add_disease(request.form['diseases_name'], request.form['symptoms'])			 
				db.session.add(adis)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('add_disease'))
		return render_template('admin/add_disease.html')

class patient_feedback(db.Model):
	id = db.Column('feed_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	feedback = db.Column(db.String(100))
	def __init__(self,name,email,feedback):
		self.name = name
		self.email = email
		self.feedback = feedback
	@app.route('/patient_feedback', methods = ['GET', 'POST'])
	def new3():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['feedback']:
				flash('Please enter all the fields', 'error')
			else:
				feed = patient_feedback(request.form['name'], request.form['email'] , request.form['feedback'])			 
				db.session.add(feed)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('patient_feedback'))
		return render_template('user/patient_feedback.html')

class patient_contact(db.Model):
	id = db.Column('contact1_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100)) 
	email = db.Column(db.String(100))
	subject = db.Column(db.String(100))
	message = db.Column(db.String(100))
	def __init__(self,name,email,subject,message):
		self.name = name
		self.email = email
		self.subject = subject
		self.message = message
	@app.route('/patient_contact', methods = ['GET', 'POST'])
	def new4():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['subject'] or not request.form['message']:
				flash('Please enter all the fields', 'error')
			else:
				contact1 = patient_contact(request.form['name'], request.form['email'], request.form['subject'], request.form['message'])			 
				db.session.add(contact1)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('patient_contact'))
		return render_template('user/patient_contact.html')

class doc_feedback(db.Model):
	id = db.Column('feed_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	feedback = db.Column(db.String(100))
	def __init__(self,name,email,feedback):
		self.name = name
		self.email = email
		self.feedback = feedback
	@app.route('/doc_feedback', methods = ['GET', 'POST'])
	def new6():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['feedback']:
				flash('Please enter all the fields', 'error')
			else:
				feed = doc_feedback(request.form['name'], request.form['email'] , request.form['feedback'])			 
				db.session.add(feed)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('doc_feedback'))
		return render_template('user/doc_feedback.html')

class doc_contact(db.Model):
	id = db.Column('contact1_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	subject = db.Column(db.String(100))
	message = db.Column(db.String(100))
	def __init__(self,name,email,subject,message):
		self.name = name
		self.email = email
		self.subject = subject
		self.message = message
	@app.route('/doc_contact', methods = ['GET', 'POST'])
	def new7():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['subject'] or not request.form['message']:
				flash('Please enter all the fields', 'error')
			else:
				contact1 = doc_contact(request.form['name'], request.form['email'], request.form['subject'], request.form['message'])			 
				db.session.add(contact1)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('doc_contact'))
		return render_template('doctor/doc_contact.html')
		
class make_appointment(db.Model):
	id = db.Column('m_app_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	dname = db.Column(db.String(100))
	subject = db.Column(db.String(100))
	message = db.Column(db.String(10000))
	def __init__(self,name,email,dname,subject,message):
		self.name = name
		self.email = email
		self.dname= dname
		self.subject = subject
		self.message = message
	@app.route('/m_app', methods = ['GET', 'POST'])
	def new8():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['dname'] or not request.form['subject'] or not request.form['message']:
				flash('Please enter all the fields', 'error')
			else:
				m_app = make_appointment(request.form['name'], request.form['email'], request.form['dname'], request.form['subject'], request.form['message'])			 
				db.session.add(m_app)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('home'))
		return render_template('user/make_appointment.html')
class make_appointment2(db.Model):
	id = db.Column('m_app2_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	dname = db.Column(db.String(100))
	subject = db.Column(db.String(100))
	message = db.Column(db.String(10000))
	def __init__(self,name,email,dname,subject,message):
		self.name = name
		self.email = email
		self.dname = dname
		self.subject = subject
		self.message = message
	@app.route('/dm_app', methods = ['GET', 'POST'])
	def new10():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['dname'] or not request.form['subject'] or not request.form['message']:
				flash('Please enter all the fields', 'error')
			else:
				m_app2 = make_appointment2(request.form['name'], request.form['email'], request.form['dname'], request.form['subject'], request.form['message'])			 
				db.session.add(m_app2)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('home'))
		return render_template('user/dmake_appointment.html')
class fix_appoinment(db.Model):
	id = db.Column('fix_app_id', db.Integer, primary_key = True)
	doc_name = db.Column(db.String(100))
	patient_name = db.Column(db.String(100))
	address = db.Column(db.String(100))
	dob1 = db.Column(db.String(100))
	dob2 = db.Column(db.String(100))
	dob3 = db.Column(db.String(100))
	def __init__(self,doc_name,patient_name,address,dob1,dob2,dob3):
		self.doc_name = doc_name
		self.patient_name = patient_name
		self.address = address
		self.dob1 = dob1
		self.dob2 = dob2
		self.dob3 = dob3
	@app.route('/fix_app', methods = ['GET', 'POST'])
	def new9():
		if request.method == 'POST':
			if not request.form['doc_name'] or not request.form['patient_name'] or not request.form['address'] or not request.form['dob1'] or not request.form['dob2'] or not request.form['dob3']:
				flash('Please enter all the fields', 'error')
			else:
				fix_app = fix_appoinment(request.form['doc_name'] ,request.form['patient_name'] ,request.form['address'] ,request.form['dob1'], request.form['dob2'], request.form['dob3'])			 
				db.session.add(fix_app)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('home1'))
		return render_template('doctor/fix_appointment.html')

if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)
