# ---views.py---
# ---importing all necessary and essential pakages and libraries... ---
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserSigninForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib
import base64
from statsmodels.tsa.arima.model import ARIMA

# --- views... ----

# ---a view for showing the main html page ----
class Main(View):
    def get(self, request):
        return render(request, 'account/main.html')

# ---to show the raw singin form , then check and enter the values if the information is correct ---
class UserSigninView(View):
    form_class = UserSigninForm
    template_name = 'account/signin.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                messages.success(request, 'added', 'success')
                login(request, user)
            return redirect('main')
        else:
            return render(request, self.template_name, {'form': form})

# --- to show the raw form of login , getting the data , then log in... ---
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                messages.success(request, 'added', 'success')
                login(request, user)
                return redirect('main')

        return render(request, self.template_name, {'form': form})


# ---to loggin out the user---
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')

# --- main view of the project
# --- to show the exist data as a diagram and calculate and show the predicted values
class Page(View):

    # def setup, To connect to the database once and not make the code slow ("lazy")
    # each data and title, calling with one number. then Depending on the ID of the page, it will change to the main data
    # and title...
    def setup(self, request, *args, **kwargs):
        self.data1 = pd.read_csv('C:/Users/amin/PycharmProjects/djangoProject1/home/files/EURUSD.csv').sort_index(
            axis=0,
            ascending=False)
        self.title1 = "euro to united states dollar"
        self.data2 = pd.read_csv('C:/Users/amin/PycharmProjects/djangoProject1/home/files/EURCAD.csv').sort_index(
            axis=0,
            ascending=False)
        self.title2 = 'euro to canada dollar'
        self.data3 = pd.read_csv('C:/Users/amin/PycharmProjects/djangoProject1/home/files/EURAUD.csv').sort_index(
            axis=0,
            ascending=False)
        self.title3 = 'euro to australia dollar'
        self.data4 = pd.read_csv('C:/Users/amin/PycharmProjects/djangoProject1/home/files/EURSGD.csv').sort_index(
            axis=0,
            ascending=False)
        self.title4 = 'euro to singapore dollar'
        self.data5 = pd.read_csv('C:/Users/amin/PycharmProjects/djangoProject1/home/files/EURRUB.csv').sort_index(
            axis=0,
            ascending=False)
        self.title5 = 'euro to russia ruble'
        self.data6 = pd.read_csv('C:/Users/amin/PycharmProjects/djangoProject1/home/files/EURKWD.csv').sort_index(
            axis=0,
            ascending=False)
        self.title6 = 'euro to kuwait dinar'

        return super().setup(request, *args, **kwargs)

    # get part, to show the load the page
    def get(self, request, page_id, ):

        global data, title
        # the ID of the page ,assign what the data and title will be
        if page_id == 1:
            data = self.data1
            title = self.title1
        elif page_id == 2:
            data = self.data2
            title = self.title2
        elif page_id == 3:
            data = self.data3
            title = self.title3
        elif page_id == 4:
            data = self.data4
            title = self.title4
        elif page_id == 5:
            data = self.data5
            title = self.title5
        elif page_id == 6:
            data = self.data6
            title = self.title6

        # ARIMA model, is one of the m_learning algorithms to predict non_linear data here i spend much time to find
        # the most parameters to each argument the model required, with drop the model in three "for_loop" to reach
        # to the most suitable set of the parameters for predicting next days. in the case"eurrub" (euro to ruble) it
        # worked incredibly awsome! *** IT COULD PREDICT NEXT 5 DAYS PRICES FLUCTUATIONS COMPLETELY!***  in other
        # cases it could predict near days with acceptable values and finally in one case it stuck in one price


        # here is the 3 most suitable set of the parameters for arguments...

        # model = ARIMA(data['Close'], order=(5, 2, 0))
        model = ARIMA(data['Close'], order=(4, 1, 2))
        # model = ARIMA(data['Close'], order=(5, 0, 0))

        model_fit = model.fit()

        y1 = np.array(data['Close']).reshape(-1, 1)
        # defining the price values(from the Close column in the external file.)
        start = len(y1)
        stop = start + 7
        # defining the length of the price value set(in some cases was 20 data, other was 21 and etc. it will worl
        #         # for all of them...
        y2 = np.array(model_fit.predict(start, stop)).reshape(-1, 1)
        y3 = np.concatenate((y1, y2), axis=0)
        # merging the pre_existing data with the model out_put values for the next days, to show in "one" diagram...
        x = np.arange(len(y3))
        # defining the x dimensions according to y dimensions length.

        # draw blue diagram , dot for marker and two hyphen to plot...
        plt.plot(x, y3, '.--b')
        plt.grid()
        # show a red vertical bar to locate "today"...
        plt.scatter(start, y1[-1], s=1000, marker="|", c="r")

        # define 6 variable to prices to show on the template...
        ep0 = np.array(model_fit.predict(start+0))
        ep1 = np.array(model_fit.predict(start+1))
        ep2 = np.array(model_fit.predict(start+2))
        ep3 = np.array(model_fit.predict(start+3))
        ep4 = np.array(model_fit.predict(start+4))
        ep5 = np.array(model_fit.predict(start+5))

        # Specifications of the diagram
        plt.title(title)
        plt.xlabel("days")
        plt.ylabel('fluctuations')

        # essential codes to converting the diagram to the picture to show in the template...
        plt.grid()
        plt.grid()
        plt.switch_backend('agg')
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        plt.clf()
        plt.close()
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)

        return render(request, 'account/page.html', {'data': uri, 'ep0': ep0, 'ep1': ep1, 'ep2': ep2, 'ep3': ep3,
                                                     'ep4': ep4, 'ep5': ep5,})
