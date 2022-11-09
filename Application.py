import pandas as pd
import joblib
import Form_DF as form_df
from flask import Flask, render_template, request


model = joblib.load(open('Rf_Model.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    store=eval(request.form['Store'])
    date=request.form['Date']
    weekly_sales=eval(request.form['Weekly_Sales'])
    temp=eval(request.form['Temperature'])
    fuel_price=eval(request.form['Fuel_Price'])
    cpi=eval(request.form['CPI'])
    unemployment=eval(request.form['Unemployment'])
    isholiday=bool(request.form['IsHoliday'])
    type=request.form['Type']
    size=eval(request.form['Size'])

    dic={'Store':[store],'Date':[date],'Weekly_Sales':[weekly_sales],'Temperature':[temp],'Fuel_Price':[fuel_price],'CPI':[cpi],'Unemployment':[unemployment],'IsHoliday':[isholiday],'Type':[type],'Size':[size]}
    sample_df=pd.DataFrame(dic)

    def Predict(data):
        fun_df=form_df.Frame_Converter(data)
        x=fun_df.drop(['Weekly_Sales','Date','Year'],axis=1)

        Rf_model=model
        result=Rf_model.predict(x)
        return result
    pred = Predict(sample_df)
    return  f"Final output is {pred}" #render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True) #host='0.0.0.0', port=8080,
    
