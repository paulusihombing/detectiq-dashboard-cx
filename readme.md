# DetectIQ XLSMART CX Dashboard

📊 A Streamlit-based monitoring dashboard for visualizing key network performance metrics like:

- Traffic Volume  
- SWE  
- E2E Latency  
- DL Throughput  

## Features

- Secure login with session state  
- Interactive Plotly charts  
- Sidebar navigation  
- Easy-to-update data using local `.csv` or `.xlsx` files

## File Structure
📁 app/
└── pages/
└── monitoring.py
📁 utils/
📁 data/
└── your_data.csv
📄 main.py
📄 requirements.txt
📄 README.md
📄 .gitignore


## How to Use

1. Replace the dataset in the `/data` folder with your latest `.csv` or `.xlsx`
2. Run locally with:

```bash
streamlit run main.py
