from flask import Flask, render_template, request, escape
from RadCalcv_json_test import data_calculation, report



app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = { 'host' : '127.0.0.1',
                'user': 'radtool',
                'password': 'Radt00lpasswd?',
                'database': 'radcalcDB',}
    import mysql.connector
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
                (Reach, Stack, Spacers, Stem, Head_Tube_Angle, Handlebar_Rise, BackSweep, UpSweep, Handlebar_Length, bikename, ip, browswer_strong, Results)
                values
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"""
    cursor.execute(_SQL, (req.form['reach'],
                    req.form['stack'],
                    req.form['spacer'],
                    req.form['stem'],
                    req.form['htangle'],
                    req.form['htrise'],
                    req.form['backsweep'],
                    req.form['upsweep'],
                    req.form['handlebarlength'],
                    req.form['bikename'],
                    req.remote_addr,
                    req.user_agent.browser,
                    res, ))
    conn.commit()
    cursor.close()
    conn.close()

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
        rreach = results['Reach'],
        sstack = results['Stack'],
        sspacer = results['Spacers'],
        sstem = results['Stem'],
        hhtangle = results['Head Tube Angle'],
        hhtrise = results['Handlebar Rise'],
        bbacksweep = results['Back Sweep'],
        uupsweep = results['Up Sweep'],
        hhandlebarlength = results['Handlebar Length'],
        bbikename = results['bikename'],
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