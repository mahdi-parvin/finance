# Project Overview
This project, titled “Forecasting and Checking Currency Price Fluctuations,” displays the price of several currencies against the euro in a chart. Additionally, it can predict price fluctuations for the next five days and present these predictions in both a chart and a table.

## Methodology
The ARIMA (Autoregressive Integrated Moving Average) machine learning algorithm is utilized in this project.

## About the ARIMA Model
The Autoregressive Integrated Moving Average (ARIMA) model predicts the next step in a sequence as a linear function of the differenced observations and residual errors at prior time steps.

This method integrates the principles of Autoregression (AR) and Moving Average (MA) models, as well as a differencing pre-processing step of the sequence to make the sequence stationary, known as integration (I).

The model is denoted as ARIMA(p, d, q), where ‘p’, ‘d’, and ‘q’ represent the order for the AR, I, and MA models respectively. The ARIMA model can also be used to develop AR, MA, and ARMA models.

The ARIMA approach is optimal for single-variable time series that exhibit a trend.

Parameter Selection
Due to the difficulty of finding optimal values for the parameters, considerable time was spent identifying the most efficient values for each argument required by the model. The model was tested in three separate loops to identify the most suitable set of parameters for predicting future days. The ‘p’ parameter was tested in the first loop, ‘d’ in the second, and ‘q’ in the last.

## Prediction Accuracy
The project has demonstrated varying levels of success across different examples.

For instance, in the Euro to Ruble example, the algorithm showed remarkable success. It was able to accurately predict the price for all the next five days, correctly charting the price fluctuations in accordance with the actual prices of the following days.
In later examples, the algorithm was able to predict the price accurately for two to three days, or obtain a correct estimate of the amount and direction of the fluctuation movement.

However, in one example, the algorithm predicted a constant price.



# Deployment
Sure, I can guide you on how to Dockerize a Django project for hosting on Kubernetes. Here are the general steps:

1. **Build the Docker image**: Run the following command in the same directory as your Dockerfile:

```bash
docker build -t my-django-app .
```

2. **Test your Docker image**: You can run your application with the following command:

```bash
docker run -it -p 8000:8000 my-django-app
```

3. **Push your Docker image to a registry**: Before you can deploy your application to Kubernetes, you need to push your Docker image to a registry that Kubernetes can access.

```bash
docker tag my-django-app registry.example.com/my-django-app
docker push registry.example.com/my-django-app
```

4. **Deploy your application to Kubernetes**: Now you can deploy your application using `kubectl`:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Please replace the example values with the ones that match your project and infrastructure. Also, remember to include a `requirements.txt` file in your project with all the necessary packages. You might need to tweak these instructions based on the specifics of your project. For example, if your application requires a database, you might need to add additional Kubernetes resources such as PersistentVolumes, PersistentVolumeClaims, and Secrets. 
