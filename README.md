# MapSift

**Turn Raw Google Maps Text into Structured Excel Data**

---

## About

**MapSift** is a simple yet powerful desktop application designed to convert unstructured Google Maps text listings into clean, structured datasets without any coding. Whether you’re collecting information about real estate agencies, gyms, schools, or any other businesses worldwide, MapSift makes it easy to organize and export your data. It’s built in Python with a user-friendly Tkinter interface that works on any screen size, from laptops to large desktops.

The app offers several convenient features to streamline your workflow. It automatically extracts company names, addresses, and phone numbers from raw text data, intelligently recognizing international dialing codes and formatting them into consistent digit-only formats (for example, `61412345678` for Australia or `11234567890` for the USA). MapSift displays all extracted records in an interactive table so you can quickly review your results. With a single click, you can export everything to an Excel file for further analysis or sharing with your team.

MapSift is built for researchers, marketers, sales teams, and anyone who needs to quickly transform messy text listings into usable records.

---

## Features

- Supports any business category and any country
- Automatically extracts company names, addresses, and phone numbers
- Detects and formats international phone numbers consistently
- Clean, responsive Tkinter GUI
- One-click export to Excel (.xlsx)
- No APIs or web scraping required—just paste raw text

---

## How to Use

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/MapSift.git
   cd MapSift
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the app:

   ```
   python main.py
   ```

4. Paste your raw Google Maps text data into the input box.

5. Click “Process Data” to extract and structure the information.

6. Review the results in the table below.

7. Click “Export to Excel” to save your clean data.

---

## License

This project is open source and free to use under the MIT License.
