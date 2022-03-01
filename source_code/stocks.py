#!/usr/bin/python
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime 



START_DATE = '2005-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
print(END_DATE)