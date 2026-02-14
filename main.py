import pandas as pd


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    new_df = df.copy()

    for letter in new_column:
        if not letter.isalpha() and letter != "_":
            return pd.DataFrame([])
        
    role = role.replace(" ", "")
    operator_index = -1

    for operator in ["*", "+", "-"]:
        if operator in role:
            operator_index = role.find(operator)
            break
    
    if operator_index == -1:
        return pd.DataFrame([])
      
    role_info = [role[:operator_index], role[operator_index], role[operator_index+1:]]  
 
    if role_info[0] not in new_df.columns or role_info[2] not in new_df.columns:
        return pd.DataFrame([])

    try:
        match role_info[1]:
            case "*":
                new_df[new_column] = new_df[role_info[0]] * new_df[role_info[2]]
            case "+":
                new_df[new_column] = new_df[role_info[0]] + new_df[role_info[2]]
            case "-":
                new_df[new_column] = new_df[role_info[0]] - new_df[role_info[2]]
    except:
        return pd.DataFrame([])
    
    return new_df


if __name__ == "__main__":

    data = {"name": ["banana", "apple", "orange", "strawberry"], "quantity": [10, 3, 5, 8], "price": [10, 1, 2, 15]}
    df = pd.DataFrame(data)

    x = add_virtual_column(df, "quantity   +   price      ", "te_st")
    print(x)




