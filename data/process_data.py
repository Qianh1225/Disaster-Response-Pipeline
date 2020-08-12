import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Load and merge datasets
    
    Args:
    messages_filepath: str. The path of messages.csv
    categories_filepath: str. The path of categories_filepath
    
    Returns:
    df: pandas dataframe. The merged dataset.  
    """
    # load dataset
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # merge dataset
    df = pd.merge(categories, messages, how='inner', on='id')

    return df


def clean_data(df):
    """
    Convert categories column of df into separate category columns 
    with numbers 0 or 1 in each row
    """
    # split categories into separate category column
    categories = df.categories.str.split(';', expand=True)

    # exact column name for each category
    category_col_name = categories.iloc[0,:].apply(lambda x: x[:-2]).values

    # rename the columns of 'categories'
    categories.columns = category_col_name

    # convert category values to just numbers 0 or 1
    for col in categories.columns:
        categories[col] = categories[col].apply(lambda x: x[-1])
        # convert column from string to numeric
        categories[col] = pd.to_numeric(categories[col])

    # concatenate the original dataframe with the new 'categories' dataframe
    df.drop(columns=['categories'], inplace=True)
    df_new = pd.concat([df, categories], axis=1)

    # drop duplicates
    df = df_new.drop_duplicates(subset=['id', 'message'])

    return df


def save_data(df, database_filename):
    """
    Save dataframe df as a sql database
    """
    save_path = 'sqlite:///'+ database_filename
    engine = create_engine(save_path)

    df.to_sql('Data', engine, index=False)


def main():
    """
    Load, clean and save data
    """
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
