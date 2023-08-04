import pandas as pd
import matplotlib.pyplot as npt
ages=[25,30,28,32,22,31,35,29,49,26,30,49,57,34,55,26,37,47,42,45,47,45,52,65,37,27,52,50,
        36,29,62,67,66,67,60,35,22,21,42,23,27,29,31,30,32,35,23,39,40,56,65,60,70]
npt.hist(ages,bins=30,edgecolor='red',color='yellow')
npt.xlabel('Age')
npt.ylabel('Frequency')
npt.title('Distibution Of Ages')
npt.show()
