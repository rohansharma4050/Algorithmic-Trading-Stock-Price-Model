# Algorithmic-Trading-Stock-Price-Model

### Problem Statement
To predict the volatility of intraday stock market considering various parameters.

### Existing System
Traditional approaches to stock market analysis and stock price prediction include fundamental analysis, which looks at a stock's past performance and the general credibility of the company itself, and statistical analysis, which is solely concerned with number crunching and identifying patterns in stock price variation. The latter is commonly achieved with the help of Genetic Algorithms (GA) or Artificial Neural Networks (ANN's), but these fail to capture correlation between stock prices in the form of long-term temporal dependencies. Another major issue with using simple ANNs for stock predictions the phenomenon of exploding / vanishing gradient, where the weights of a large network either become too large or too small (respectively), drastically slowing their convergence to the optimal value. 

### Approach to the problem
* Live Data Collection using yfinance Library
* Pre processing the data for drawing insights in terms of stability of the company
* Visualizing the stock price of the company right from the date of listing till present graphically
* Developing a Model using LSTM( Type of Recurrent Neural Network)
* Developing a Deployment file (app.py) using Streamlit
* Deploying our model on Website 

### Need for this Model
Stock market price prediction is a difficult undertaking that generally requires a lot of human-computer interaction. Traditional batch processing methods cannot be used effectively for stock market analysis due to the linked nature of stock prices. We present an online learning technique that employs a recurrent neural network of some sort (RNN) called Long Short Term Memory (LSTM), which uses stochastic gradient descent to update the weights for individual data points. When compared to existing stock price prediction systems, this will yield more accurate results. With varying sizes of data, the network is trained and evaluated for accuracy, and the results are tallied. A comparison with respect to accuracy is then performed against an Artificial Neural Network

### Sample Demo on Local Host
![Screenshot (1009)](https://user-images.githubusercontent.com/69635604/125208680-9f062180-e2b1-11eb-903c-3b4cd2bf4f32.png)
![Screenshot (1008)](https://user-images.githubusercontent.com/69635604/125208681-a2011200-e2b1-11eb-9585-be4936915e5c.png)
![Screenshot (1007)](https://user-images.githubusercontent.com/69635604/125208682-a299a880-e2b1-11eb-9ca6-c77843367a23.png)
