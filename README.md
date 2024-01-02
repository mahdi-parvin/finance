### Hi everyone!
## What is this project?
this project is "Forecasting and checking currency price fluctuations"
This program shows the price of several currencies against the euro in a chart.
And it can also predict price fluctuations in the next 5 days and show it in a chart and in a table.
## How it works?
In this project I used ARIMA machine learning algorithm.
## The ARIMA model...
The Autoregressive Integrated Moving Average (ARIMA) method model predicts the next step in the sequence as a linear function of the differenced observations and residual errors at prior time steps.

The method integrates the principles of Autoregression (AR) and Moving Average (MA) models as well as a differencing pre-processing step of the sequence to make the sequence stationary, called integration (I).

The notation for the model involves specifying the order for the AR(p), I(d), and MA(q) models as parameters to an ARIMA function, e.g. ARIMA(p, d, q). An ARIMA model can also be used to develop AR, MA, and ARMA models.

The ARIMA approach is optimal for single-variable time series that exhibit a trend.

## How i found the best parameters
Because of the dificulty of finding good values to the parameters,i spend much time to find the most efficient valuse to each argument the model required
I drop the model in three "for_loop" to reach to the most suitable set of the parameters for predicting next days.
the "p" was checked in the first loop. "d" in the next and "q" in the last

## How well can the project predict values?

About different examples of this project, it showed different successes.

About different examples of this project, it showed different successes.
### Regarding the euro to ruble example, the algorithm showed incredible success; And he was able to predict the price of all the next 5 days exactly in accordance with the reality and draw the ups and downs of the chart completely in accordance with the prices of the following days.
Regarding the later examples, the algorithm was able to predict the price well for two to three days, or obtain a correct estimate of the amount and direction of the fluctuation movement.
About one example, the algorithm got stuck in a fixed price.
