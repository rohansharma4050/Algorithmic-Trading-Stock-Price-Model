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
* 

### Need for this Model
Stock market price prediction is a difficult undertaking that generally requires a lot of human-computer interaction. Traditional batch processing methods cannot be used effectively for stock market analysis due to the linked nature of stock prices. We present an online learning technique that employs a recurrent neural network of some sort (RNN) called Long Short Term Memory (LSTM), which uses stochastic gradient descent to update the weights for individual data points. When compared to existing stock price prediction systems, this will yield more accurate results. With varying sizes of data, the network is trained and evaluated for accuracy, and the results are tallied. A comparison with respect to accuracy is then performed against an Artificial Neural Network


### Sample Demo on Local Host

This is the interface of the website deployed on Streamlit platform. User can select any stock of his choice from the list of options. After selection of the stock it takes a couple of seconds to capture the latest price with the help of yfinance library.


![Screenshot (1009)](https://user-images.githubusercontent.com/69635604/125208680-9f062180-e2b1-11eb-903c-3b4cd2bf4f32.png)


After capturing the price of that stock it runs the LSTM Model in the backend and make prediction based on batch size and epochs that we have considered in our code. Prediction usually takes upto 2-3 mins. Prediction are made for the next 10 days only (considering the high volatility of Stock Market)


![Screenshot (1008)](https://user-images.githubusercontent.com/69635604/125208681-a2011200-e2b1-11eb-9585-be4936915e5c.png)


### Future Work
Stock markets  are  hard  to  monitor  and  require  plenty  of context when trying to interpret the movement and predict prices.  In  ANN,  each  hidden  node  is  simply  a  node  with  a single  activation  function,  while  in  LSTM,  each  node  is  a memory cell that can store contextual information. As such, LSTMs perform better as they are able to keep track of the context-specific   temporal   dependencies   between   stock prices for   a   longer   period   of   time   while   performing predictions. 

An  analysis  of  the  results  also  indicates  that model gives better accuracy when the size of the dataset increases. With  more  data,  more  patterns  can  be  fleshed  out  by  the model, and the weights of the layers can be better adjusted. At its  core,  the  stock  market  is  a  reflection  of  human emotions.  Pure number crunching and analysis  have  their limitations; a possible extension of this stock prediction system would be to augment it with a news feed analysis from social media platforms such as Twitter,where emotions are gauged from the articles. This sentiment analysis can be linked with the LSTM to better train weights and further improve accuracy. 




