from flask import Flask, render_template, request, escape
from RadCalcv_json_test import data_calculation, json_report



app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('RADReq.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/datainput', methods=['POST'])
def calculation() -> 'html':
    global bikedata
    bikedata = {
        'Reach' : request.form['reach'],
        'Stack' : request.form['stack'],
        'Spacers' : request.form['spacer'],
        'Stem' : request.form['stem'],
        'Head Tube Angle' : request.form['htangle'],
        'Handlebar Rise' : request.form['htrise'],
        'Back Sweep' : request.form['backsweep'],
        'Up Sweep' : request.form['upsweep'],
        'Handlebar Length' : request.form['handlebarlength'],
        'bikename' : request.form['bikename']}
    title = 'Here are your results!'
    results = data_calculation(bikedata)
    log_request(request, results)
    return render_template('radresults.html',
        rreach = bikedata['Reach'],
        sstack = bikedata['Stack'],
        sspacer = bikedata['Spacers'],
        sstem = bikedata['Stem'],
        hhtangle = bikedata['Head Tube Angle'],
        hhtrise = bikedata['Handlebar Rise'],
        bbacksweep = bikedata['Back Sweep'],
        uupsweep = bikedata['Up Sweep'],
        hhandlebarlength = bikedata['Handlebar Length'],
        bbikename = bikedata['bikename'],
        the_title = title,
        radmm_results = results['RAD'],
        radin_results = results['RAD in inches'],
        radangle_results = results['RAAD'])
 
@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('RADReq.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                            the_title = 'View Log',
                            the_row_titles = titles,
                            the_data = contents)


@app.route('/')    
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('radentry.html',
        the_title='Welcome to the RAD CALCULATOR Web App')

if __name__ == '__main__':
    app.run(debug=True)