import pandas as pd


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    
    for letter in new_column:
        if not letter.isalpha() and letter != "_":
            return pd.DataFrame([])
        
    new_df = df.copy()    

    try:
        new_df[new_column] = new_df.eval(role)
    except:
        return pd.DataFrame([])

    return new_df


if __name__ == "__main__":

    data = {"name": ["banana", "apple", "orange", "strawberry"], "quantity": [10, 3, 5, 8], "price": [10, 1, 2, 15]}
    df = pd.DataFrame(data)

    x = add_virtual_column(df, "      quantity    *     price    * 10 ", "te_st")
    print(x)


