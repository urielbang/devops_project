import requests
import sys

def fetch_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def process_data(data):
    processed_data = []
    for item in data:
        processed_data.append({
            "id": item["id"],
            "name": item["name"],
            "value": item["value"] * 2  # example processing
        })
    return processed_data

def generate_html(data):
    html_content = "<html><head><title>Processed Data Report</title></head><body>"
    html_content += "<h1>Processed Data Report</h1>"
    html_content += "<table border='1'><tr><th>ID</th><th>Name</th><th>Value</th></tr>"
    for item in data:
        html_content += f"<tr><td>{item['id']}</td><td>{item['name']}</td><td>{item['value']}</td></tr>"
    html_content += "</table></body></html>"
    return html_content

if __name__ == "__main__":
    api_url = sys.argv[1]
    data = fetch_data(api_url)
    processed_data = process_data(data)
    html_content = generate_html(processed_data)
    with open("output.html", "w") as f:
        f.write(html_content)
