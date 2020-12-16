import getData
import plot

questioninput = str(input("Do you want to input data or to see plots? Answer with 'data' or 'plot': "))

if questioninput == "data":
    getData.input_data()

elif questioninput == "plot":
    plot.plot()