import sys
import numpy as np
import pandas as pd

def merge_home_and_away_scores(dataframe):
    values = dataframe.to_numpy()
    output_array = None
    column_name = []
    columns = dataframe.columns
    for column in columns:
        column_values = values[:, columns.get_loc(column)]
        if column[:2] == "h_":
            stat = column[2:]
            column_values = column_values - values[:, columns.get_loc("a_" + stat)]
            column = stat
        elif column[:2] == "a_":
            continue
        if output_array is None:
            output_array = column_values[:, None]
        else:
            output_array = np.append(output_array, column_values[:, None], axis=1)
        column_name.append(column)
    return pd.DataFrame(columns=column_name, data=output_array)





if __name__ == '__main__':
    path = sys.argv[1]
    target_file = sys.argv[2]
    original_df = pd.read_csv(path)
    (merge_home_and_away_scores(original_df)).to_csv(target_file, index=False)
