import pandas as pd
import os

# Settings
input_csv = 'painting list.csv'
output_dir = 'pages'
template_file = 'paintingtemplate.html'

# Ensure output dir exists
os.makedirs(output_dir, exist_ok=True)

# Load CSV
df = pd.read_csv(input_csv)

# Add page name column (you can customize this logic)
df['page_name'] = df['title'].str.strip().str.replace(' ', '_').str.lower() + '.html'
df['page_name'] = df["page_name"].str.replace("?", '')
df['tags'] = df['tags'].astype(str)
df['page_name'] = df['title'].str.strip().str.replace(' ', '_').str.lower() + '.html'
df['etsy link'] = '<a href="' + df['etsy link']+ '"> Print </a>'
df = df[df['hide'] == 1]
df = df.sort_values(by='rank', ascending=True)
df = df.fillna('')
df = df.reset_index()


# Read template
with open(template_file, 'r', encoding='utf-8') as f:
    template = f.read()

total = len(df)

df = df.fillna('')

# Loop through paintings
for i, row in df.iterrows():
    filename = row['page_name']

    # Circular prev/next indices
    prev_index = (i - 1) % total
    next_index = (i + 1) % total

    prev_page = df.iloc[prev_index]['page_name']
    next_page = df.iloc[next_index]['page_name']

    # Tags → HTML links
    tags_list = row['tags'].split()
    tag_links = ' '.join([f'<a href="portfolio.html#{tag}">{tag}</a>' for tag in tags_list])
    
    # Replace template placeholders
    html = template
    html = html.replace('{{ title }}', row['title'])
    html = html.replace('{{ description }}', row['description'])
    # = html.replace('{{ dimensions }}', row['dimensions'])
    html = html.replace('{{ year }}', " " + str(row['year']))
    html = html.replace('{{ file }}', row['file'])
    #html = html.replace('{{ prev_page }}', prev_page)
    #html = html.replace('{{ next_page }}', next_page)
    html = html.replace('{{ tag_links }}', tag_links)
    html = html.replace('{{ availability }}', row['price'])
    html = html.replace('{{ etsy }}', row['etsy link'])
    html = html.replace('{{ medium }}', row['medium'] + " on "+  row['on'])


    # Save
    output_path = os.path.join(output_dir, filename)
    with open(output_path, 'w', encoding='utf-8') as out_file:
        out_file.write(html)

    print(f"Generated: {output_path}")
