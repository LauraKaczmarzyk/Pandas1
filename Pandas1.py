import pandas as pd
import numpy as np


Bank_df_1 = pd.DataFrame({'First name': ['Frank', 'Alin', 'Kuba', 'Simon', 'Samuel'],
                         'Second name': ['A', 'B', 'C', 'D', 'E']},
                         index=[1, 2, 3, 4, 5])
Bank_df_2 = pd.DataFrame({'First name': ['Eve', 'Georgia', 'Vince', 'Diogo', 'Jeff'],
                          'Second name': ['A', 'D', 'A', 'K', 'L']},
                         index=[6, 7, 8, 9, 10])

Salary = pd.DataFrame({'Salary': [1, 10, 20, 4, 20, 7, 9, 15, 30, 70]},
                      index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

Bank_df = pd.concat([Bank_df_1, Bank_df_2])
Bank_df = Bank_df.join(Salary)


client_11_df = pd.DataFrame({'First name': 'Julia',
                            'Second name': 'Trawnicka',
                             'Salary': 120},
                            index=[11])

Bank_df = pd.concat([Bank_df, client_11_df])

print(Bank_df)