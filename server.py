from flask import Flask, render_template, request, abort
import pyautogui

app = Flask(__name__)

GPS_POS = (2532, 228)
CONTROLS_POS = (1532, 228)

@app.route('/student')
def student():
    hidden = True
    return render_template('clicker.html',hidden=hidden)

@app.route('/instructor_l33t')
def instructor():
    hidden = False
    return render_template('clicker.html',hidden=hidden)


@app.route('/click')
def click():
    pos = request.args.get('pos')
    # Perform different actions based on the role
    if pos == 'gps':
        pyautogui.click(GPS_POS)
    elif pos == 'controls':
        pyautogui.click(CONTROLS_POS)
    else:
        abort(400, description="Invalid 'pos' parameter")
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)