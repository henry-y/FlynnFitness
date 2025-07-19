import os
import arrow

# 创建输出文件夹（如果不存在）
output_folder = 'markdown_files'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取当前时间，并格式化为 "YYYY MMM Do ddd HH:mm"
current_date = arrow.now().format('YYYY MMM Do ddd HH:mm')

# 遍历当前文件夹下的所有PDF文件
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        # 获取文件名，不包含扩展名
        title = os.path.splitext(filename)[0]
        # 在指定文件夹下创建同名的Markdown文件
        markdown_filename = os.path.join(output_folder, f"{title}.md")
        
        # Markdown文件的内容模板
        content = f"""---
category: 医学本科生存指南
tags: 
 - 医学本科生存指南
 - 口腔医学通关指南
title: {title}
date: "{current_date}"
cover: ["img/口腔医学/cover.jpg"]
banner: 
  type: img
  bgurl: "img/口腔医学/cover.jpg"
  bannerText: 
---

{{% pdf /pdf/口腔医学/{filename} %}}
"""

        # 写入内容到Markdown文件
        with open(markdown_filename, 'w', encoding='utf-8') as md_file:
            md_file.write(content)

        print(f"Markdown file created: {markdown_filename}")

print("All PDF files have been processed.")
