import math
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
from datetime import date
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go

st.title('DALAL STREET- STOCK ANALYZER')
stocks = ("TECHM.NS","TCS.NS","WIPRO.NS","INFY.NS","LT.NS","GODREJIND.NS","RELIANCE.NS", "KOTAKBANK.NS", "ICICIBANK.NS", "HDFCBANK.NS","AXISBANK.NS")
selected_stock = st.selectbox("Select any Stock for Analysis", stocks)

def load_data(ticker):
    data = yf.download(ticker)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text('Collecting Live Data...It may take some time!')
df = load_data(selected_stock)
data_load_state.text('Collecting Live Data...It may take some time!, Hurray Live Data is Ready!')

st.subheader('Past 5 Days Analysis')
st.write(df.tail())

def plot_raw_data():
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.Date, y=df['Close'], name="stock_close", line_color='deepskyblue'))
    fig.layout.update(
        title_text='Time Series Analysis', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    return fig


plot_raw_data()

data_load_state = st.text('Predicting and Analyzing your Stock... Kindly Wait!')

data = df.filter(['Close'])
current_data = np.array(data).reshape(-1, 1).tolist()

df = np.array(data).reshape(-1, 1)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_df = scaler.fit_transform(np.array(df).reshape(-1, 1))
train_data = scaled_df[0:, :]

x_train = []
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error',metrics =['accuracy'])
model.fit(x_train, y_train, batch_size=40, epochs=20)

test_data = scaled_df[-60:, :].tolist()
x_test = []
y_test = []
for i in range(60, 70):
    x_test = (test_data[i-60:i])
    x_test = np.asarray(x_test)
    pred_data = model.predict(x_test.reshape(1, x_test.shape[0], 1).tolist())

    y_test.append(pred_data[0][0])
    test_data.append(pred_data)



pred_next_10 = scaler.inverse_transform(np.asarray(y_test).reshape(-1, 1))

data_load_state.text('Hurrayy,Stock successfully Analyzed!')
st.subheader("Next 10 Days Analysis")
st.write(pred_next_10)
