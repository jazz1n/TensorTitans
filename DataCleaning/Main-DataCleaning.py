import os
import pandas as pd
from DataCleaning.DataCleaningFunctions_Persian import PersianTextPreprocessor
from DataCleaning.DataCleaningFunctions_English import EnglishTextPreprocessor

# Define the directory containing the data files
directory_path = "DataSource"

# List of files in the directory
files = [
    "NeuLab-TedTalks-fa.csv",
    "ELRC_2922-fa.csv",
    "GNOME-fa.csv",
    "infopankki-fa.csv",
    "QED-fa.csv",
    "Tanzil-fa.csv",
    "TED2020-fa.csv",
    "TEP-fa.csv",
    "tico-19-fa.csv",
    "tldr-pages-fa.csv",
    "MIZAN-fa.csv",
    "Ubuntu-fa.csv",
    "WikiMatrix-fa.csv",
    "wikimedia-fa.csv",
    "XLEnt-fa.csv",
    "OpenSubtitles-fa.csv",
    "Sentence pairs in Persian-English - 2024-08-15.csv"
]

# Instantiate the text processors
persian_processor = PersianTextPreprocessor()
english_processor = EnglishTextPreprocessor()


def process_file(file_path):
    try:
        # Load the CSV file
        df = pd.read_csv(file_path)

        # Check for columns containing Persian or English text
        if 'Farsi' in df.columns or 'Persian' in df.columns:
            farsi_column = 'Farsi' if 'Farsi' in df.columns else 'Persian'
            df[f"Cleaned_{farsi_column}"] = persian_processor.process_column(df[farsi_column])

        if 'English' in df.columns:
            df['Cleaned_English'] = english_processor.process_column(df['English'])

        cleaned_file_path = os.path.join(directory_path, f"cleaned_{os.path.basename(file_path)}")
        df.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned and saved: {cleaned_file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    # Process each file in the directory
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        process_file(file_path)

    print("Data cleaning completed for all files!")


if __name__ == "__main__":
    main()
