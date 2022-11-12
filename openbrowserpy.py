# first import the module
import webbrowser
n = int(input("Now many times you want open the tab"));
# then make a url variable
for i in range(0,n):
    url = "https://learn.microsoft.com/training/browse/?products=azure&wt.mc_id=studentamb_209515"
    webbrowser.open(url)
