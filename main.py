import getData
import plot

#answer the following question to run getData code or plot code
questioninput = str(input("Do you want to input data or to see plots? Answer with 'data' or 'plot': "))

if questioninput == "data":
    getData.input_data()

elif questioninput == "plot":
    plot.plot()