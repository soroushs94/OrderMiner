import pandas as pd
from .Taxonomy import dics


class WO_Categorizer():
    def __init__(self, df, cleaned_column):
        # df = pd.read_csv('./2yrWO_cleaned_2_buildings.csv')
        self.df = df #assuming the df is in correct format
        self.column = cleaned_column
        self.dics = dics
        self.keys = dict(zip([y for x in self.dics for y in x], [set(x[y]) for x in self.dics for y in x]))

        self.add_columns()
        self.update_df()

    def add_columns(self):
        for key in self.keys.keys():
            self.df[key] = 0

    def contains_word(self,text, word_list):
        return any(word in text for word in word_list)

    def update_df(self):
        for index, row in self.df.iterrows():
            text = row[self.column]
            for key, values in self.keys.items():
                if self.contains_word(text, values):
                    self.df.at[index, key] = 1

    def get_categorized_df(self):
        return self.df

if __name__ == '__main__':
    df = pd.read_csv('./2yrWO_cleaned_2_buildings.csv')
    categorizer = WO_Categorizer(df,'clean_desc')
    print(categorizer.get_categorized_df().head())
