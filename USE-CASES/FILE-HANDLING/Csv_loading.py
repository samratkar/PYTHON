import pandas as pd
companies = pd.read_csv("../DATA-FILES/companies.txt", sep="\t", encoding = 'ISO-8859-1')
companies["permalink"] = companies["permalink"].str.upper()
