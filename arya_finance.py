import argparse
import numpy as np
import pandas as pd



class AryaFinance():
    def __init__(self, date, amount, tran_type, comments):
        self.date = date
        self.amount = float(amount)
        self.tran_type = tran_type.upper()
        self.comments = str(comments)
        self.df = pd.DataFrame()

    def load_transaction(self):
        dict = {'Date': [self.date], 'Amount': [self.amount], 'Tran_Type': [self.tran_type], 'Comments': [comments]}
        input_df = pd.DataFrame.from_dict(dict)
        source_df = pd.read_excel(r'C:\Finance\finance.xlsx')
        self.df = pd.concat([source_df, input_df])
        self.df = self.df.reset_index(drop=True)
        self.calculate_balance()
        self.df.to_excel(r'C:\Finance\finance.xlsx', index=False)

    def calculate_balance(self):
        balance = 0
        self.df['Balance'] = np.NAN
        for index, row in self.df.iterrows():
            if row['Tran_Type'] == 'CR':
                balance = balance + row['Amount']
            if row['Tran_Type'] == 'DR':
                balance = balance - row['Amount']
            self.df.at[index, 'Balance'] = balance
        print(self.df)




# if __name__ == '__main__':
#     ap = argparse.ArgumentParser()
#     ap.add_argument("Date", help="Please pass the date of transaction")
#     ap.add_argument("Amount", help="Please pass the Amount")
#     ap.add_argument("Transaction_type", help="Please pass the transaction of type (cr / dr)")
#     ap.add_argument("Comments", help="Please pass the Comments")
#     args = ap.parse_args()
#     date = args.Date
#     amount = args.Amount
#     comments = args.Comments
#     tran_type = args.Transaction_type
#     AryaFinance(date, amount, tran_type, comments).load_transaction()

if __name__ == '__main__':
    date = input("Please Enter the Date of transaction ")
    amount = input("Please Enter the Amount")
    tran_type = input("Please Enter the Type of transaction(CR or DR) ")
    comments = input("Please Enter Where You Got Or Spent The Money ")
    AryaFinance(date, amount, tran_type, comments).load_transaction()
