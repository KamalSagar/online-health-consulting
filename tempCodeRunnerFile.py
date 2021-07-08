ute('/patient_feedback', methods = ['GET', 'POST'])
	# def new3():
	# 	if request.method == 'POST':
	# 		if not request.form['name'] or not request.form['email'] or not request.form['feedback']:
	# 			flash('Please enter all the fields', 'error')
	# 		else:
	# 			feed = patient_feedback(request.form['name'], request.form['email'] , request.form['feedback'])			 
	# 			db.session.add(feed)
	# 			db.session.commit()
 	# 			flash('Record was successfully added')
	# 			return redirect(url_for('patient_feedback'))
	# 	return render_