
import pandas as pd

# Settings
input_csv = 'painting list.csv'
#output_html = 'gallery_items.html'  # or you can just print() instead of writing file

# Load CSV
df = pd.read_csv(input_csv)

# Optional: generate safe page name
df['page_name'] = df['title'].str.strip().str.replace(' ', '_').str.lower() + '.html'
df['page_name'] = df["page_name"].str.replace("?", '')
df = df[df['hide'] == 1]
df = df.sort_values(by = 'rank', ascending=True)
df = df.fillna('')
df = df.reset_index()


template_file = 'portfoliotemplate.html'
template_file = 'paintingtemplate.html'


# Start output
gallery_html = ''

for index, row in df.iterrows():
    title = row['title']
    image_filename = row['file']
    description = row['description']
    tags = row['tags']
    medium = row['medium']

    tag_classes = ' '.join(tags.split())
    detail_page = f"portfolio/{row['page_name']}"

    gallery_item = f'''
<div class="gallery-item {tag_classes}">               
    <a href="{detail_page}">
        <img src="images/{image_filename}" loading="lazy" alt="{title} - {description}, {medium}">
    </a>
    <div class="caption">{title}</div>
</div>
'''

    gallery_html += gallery_item
# with open(template_file, 'r', encoding='utf-8') as f:
#     template = f.read()
# html = template
# html = html.replace('{{ title }}', row['title'])
# output_path = os.path.join(output_dir, filename)

# with open(output_path, 'w', encoding='utf-8') as out_file:
#     out_file.write(html)
# # Output to file (or print to console)
# #with open(output_html, 'w', encoding='utf-8') as out_file:
# #    out_file.write(gallery_html)

print(gallery_html)
