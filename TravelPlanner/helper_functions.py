from IPython.display import Markdown,display, HTML
import pandas as pd 
def display_table(data):
    df = pd.DataFrame(data)

    # Display the DataFrame as an HTML table
    display(HTML(df.to_html(index=False)))