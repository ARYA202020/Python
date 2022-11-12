import argparse
import pandas as pd



class AryaFinance():
    def __init__(self, date, amount, tran_type, comments):
        self.date = date
        self.amount = amount
        self.tran_type = tran_type
        self.comments = comments

    def print_msg(self):
        dict = {'Date': [self.date], 'Amount': [self.amount], 'Tran_Type': [self.tran_type], 'Comments': [comments]}
        input_df = pd.DataFrame.from_dict(dict)
        source_df = pd.read_excel(r'C:\Finance\finance.xlsx')
        df = pd.concat([source_df, input_df])
        df.to_excel(r'C:\Finance\finance.xlsx', index=False)
        print(df)





if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("Date", help="Please pass the date of transaction")
    ap.add_argument("Amount", help="Please pass the Amount")
    ap.add_argument("Transaction_type", help="Please pass the transaction of type (cr / dr)")
    ap.add_argument("Comments", help="Please pass the Comments")
    args = ap.parse_args()
    date = args.Date
    amount = args.Amount
    comments = args.Comments
    tran_type = args.Transaction_type
    AryaFinance(date, amount, tran_type, comments).print_msg()
