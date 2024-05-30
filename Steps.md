# Steps Taken

# Step 1. Copy given resources
```bash
cd WindmillDashboard
```
```bash
git clone https://github.com/neuralix-ai/Hackathon_Dashboard.git
```
# Step2
```bash
mkdir "JupyterOutputs"
```

# Step3. Add this code snippet to each of the cells that makes a figure
```python
config = {
    'scrollZoom': False,
    'showLink': False,
    'displayModeBar': False
}

# Extract the title from the layout
title = fig.layout.title.text

html = pio.to_html(fig, validate=False, include_plotlyjs='cdn', config=config)

# Define the output directory path (one level up and inside 'Output' folder)
output_dir = os.path.join('..', '..', 'JupyterOutputs')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Construct the file path
file_path = os.path.join(output_dir, f'{title.replace(" ", "_").lower()}.html')

# Save the HTML to a file
with open(file_path, 'w') as file:
    file.write(html)
```
