Pandas Virtual Column - Python

A function that extends a pandas DataFrame by dynamically creating a virtual column based on a simple mathematical expression.


TASK DESCRIPTION:

  You have a pandas DataFrame with existing data and want to create a new DataFrame that includes the original data along with an additional column calculated based on specified operations. To achieve this, implement the add_virtual_column function.
  
  Inputs:
  
    df: Any pandas DataFrame.
    role: A mathematical expression defining how to compute the values for the virtual column. For example, 'first_column - second_column'.
    new_column: The name of the new virtual column to be added.
  
  Validations:
  
    Column labels must consist only of letters and underscores (_).
    The function must support basic operations: addition (+), subtraction (-), and multiplication (*).
    If the role or any column label is incorrect, the function should return an empty DataFrame.


