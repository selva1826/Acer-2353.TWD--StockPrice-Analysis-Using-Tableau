import yfinance as yf

# Define the ticker symbol
ticker = "2353.TW"

# Get the data for the ticker
stock_data = yf.download(ticker, start="2024-01-01", end="2024-01-30")

# Define the specific folder path where you want to save the CSV file
folder_path = "E:"  # Replace with your desired path

# Save the data as a CSV file in the specified folder
stock_data.to_csv(folder_path + 'acerIndia_stock_data2.csv')

print("Data saved as acerIndia_stock_data.csv in the specified folder")
