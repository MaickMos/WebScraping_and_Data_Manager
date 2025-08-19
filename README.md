# Downloader-videos-and-data-analyzer

This project provides a tool to **download TikTok videos directly from collections**. By simply entering the link of any TikTok collection, the program automatically extracts all video links within that collection, stores them in a database, and organizes them for easy access and analysis.

Each video is categorized with a **class (the collection’s name)** and assigned a **unique identifier**, then downloaded into corresponding folders for structured storage.

This enables not only simplified video access but also the ability to **analyze the extracted data** efficiently.

---

## ✨ Features

* Extract all video links from a TikTok collection.
* Automatically create and manage a **PostgreSQL database** with video information.
* Classify videos by collection name and ID.
* Download videos into organized folders by collection.
* Enable structured analysis of TikTok video data.

---

## 🛠️ Technologies Used

* **Selenium** – for automated browsing and scraping.
* **BeautifulSoup** – for parsing HTML content.
* **Pandas** – for data handling and analysis.
* **SQL / PostgreSQL** – for database storage and management.
* **Git** – for version control.

---

## 🚀 How It Works

1. Provide one or more TikTok collection links.
2. The script extracts all video URLs from each collection.
3. A PostgreSQL database is created/updated with video metadata.
4. Videos are downloaded into organized folders.
5. Data can be easily accessed for further analysis or processing.

---

## 📂 Project Structure

```
📦 tiktok-collections-downloader
 ┣ 📂 data                # Video database and metadata
 ┣ 📂 downloads           # Downloaded videos organized by collection
 ┣ 📜 main.py             # Main script
 ┣ 📜 requirements.txt    # Dependencies
 ┗ 📜 README.md           # Project documentation
```

---

## ⚡ Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/tiktok-collections-downloader.git
   cd tiktok-collections-downloader
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your PostgreSQL connection in `config.py`.

4. Run the script and input TikTok collection links:

   ```bash
   python main.py
   ```

---

## 📊 Example Use Case

* Save and organize your favorite TikTok collections.
* Build datasets for analysis.
* Automate video archiving for research or personal use.

---

## 📜 License

This project is licensed under the MIT License.

