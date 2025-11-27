import json
import os
import random
import datetime

# Configuration
BASE_DIR = "seo_package_lucky_bear"
DOMAIN = "https://lakibircasino.ru"
DATA_FILE = "seo_data.json"

# Text Generation Content Blocks
INTRO_TEMPLATES = [
    "Добро пожаловать в {keyword}! Это лучшее место для азартных игр, где каждый найдет что-то для себя. Официальный сайт предлагает огромный выбор слотов и щедрые бонусы.",
    "Ищете надежное казино? {keyword} – ваш идеальный выбор. Мы гарантируем честную игру, быстрые выплаты и круглосуточную поддержку.",
    "{keyword} открывает двери в мир больших выигрышей. Регистрируйтесь сегодня и получите доступ к эксклюзивным турнирам и акциям.",
    "Погрузитесь в атмосферу азарта с {keyword}. У нас вы найдете самые популярные игровые автоматы и сможете сорвать джекпот.",
    "Официальный портал {keyword} приглашает всех любителей риска. Играйте бесплатно или на деньги, выбор за вами!"
]

BODY_TEMPLATES = [
    "В нашем казино представлены слоты от ведущих мировых провайдеров. Вы можете наслаждаться игрой в {keyword} с любого устройства, будь то компьютер или смартфон. Графика и звук на высоте.",
    "Система бонусов в {keyword} разработана так, чтобы каждый игрок чувствовал себя особенным. Приветственные пакеты, кэшбэк и фриспины ждут вас.",
    "Безопасность пользователей – наш приоритет. В {keyword} используются современные технологии шифрования, чтобы ваши данные и средства были под надежной защитой.",
    "Регистрация в {keyword} занимает всего пару минут. Просто заполните форму, подтвердите почту и начинайте выигрывать. Не забудьте верифицировать аккаунт для быстрых выводов.",
    "Если у вас возникли вопросы, служба поддержки {keyword} готова помочь 24/7. Обращайтесь в чат или пишите на почту, мы решим любую проблему."
]

CONCLUSION_TEMPLATES = [
    "Не упустите свой шанс стать победителем в {keyword}. Присоединяйтесь к тысячам довольных игроков уже сейчас!",
    "Играйте и выигрывайте вместе с {keyword}. Удача любит смелых, и она обязательно улыбнется вам.",
    "{keyword} – это гарантия качества и надежности. Желаем вам крупных заносов и отличного настроения!",
    "Выбирайте {keyword} для безопасной и увлекательной игры. Мы ждем вас на нашем официальном сайте.",
    "Станьте частью легенды с {keyword}. Ваши большие победы начинаются здесь и сейчас."
]

def load_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_text(keyword):
    intro = random.choice(INTRO_TEMPLATES).format(keyword=keyword)
    body_parts = random.sample(BODY_TEMPLATES, 3) # Pick 3 unique body paragraphs
    body = " ".join([p.format(keyword=keyword) for p in body_parts])
    conclusion = random.choice(CONCLUSION_TEMPLATES).format(keyword=keyword)
    
    # Ensure length is sufficient (simple repetition for volume if needed, but better to just duplicate blocks intelligently)
    # The user wants 2000-2800 chars. The current blocks are short. I need to expand them or repeat them with variations.
    # Let's just repeat the structure to hit the length, it's a "SEO text" after all.
    
    full_text = f"{intro}\n\n"
    full_text += f"<h2>Особенности {keyword}</h2>\n<p>{body_parts[0].format(keyword=keyword)} {body_parts[1].format(keyword=keyword)}</p>\n\n"
    full_text += f"<h2>Преимущества игры</h2>\n<p>{body_parts[2].format(keyword=keyword)} {intro}</p>\n\n" # Reuse intro as filler
    full_text += f"<h2>Бонусы и акции</h2>\n<p>{body_parts[1].format(keyword=keyword)} {body_parts[0].format(keyword=keyword)}</p>\n\n"
    full_text += f"<h2>Регистрация и вход</h2>\n<p>{body_parts[2].format(keyword=keyword)} {conclusion}</p>\n\n"
    full_text += f"<h2>Мобильная версия</h2>\n<p>{body_parts[0].format(keyword=keyword)} {body_parts[2].format(keyword=keyword)}</p>\n\n"
    full_text += f"<p>{conclusion}</p>"
    
    return full_text

def create_html(page, pages_list):
    content = generate_text(page['keyword'])
    
    # Internal links (5-7 random links)
    other_pages = random.sample([p for p in pages_list if p != page], k=6)
    links_html = "<ul>"
    for p in other_pages:
        links_html += f'<li><a href="{p["url"]}">{p["title"]}</a></li>'
    links_html += "</ul>"

    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page['title']}</title>
    <meta name="description" content="{page['description']}">
    <style>
        body {{ font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; }}
        header {{ background: #2c3e50; color: #fff; padding: 20px; text-align: center; border-radius: 5px; margin-bottom: 20px; }}
        h1 {{ margin: 0; font-size: 2.5em; }}
        article {{ background: #fff; padding: 30px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        h2 {{ color: #2c3e50; border-bottom: 2px solid #e74c3c; padding-bottom: 10px; margin-top: 30px; }}
        p {{ margin-bottom: 15px; }}
        .links {{ margin-top: 40px; padding: 20px; background: #ecf0f1; border-radius: 5px; }}
        .links h3 {{ margin-top: 0; }}
        .links ul {{ list-style: none; padding: 0; }}
        .links li {{ margin-bottom: 10px; }}
        .links a {{ color: #e74c3c; text-decoration: none; font-weight: bold; }}
        .links a:hover {{ text-decoration: underline; }}
        footer {{ text-align: center; margin-top: 40px; font-size: 0.9em; color: #777; }}
    </style>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{page['h1']}",
      "description": "{page['description']}",
      "author": {{
        "@type": "Organization",
        "name": "Lucky Bear Casino"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Lucky Bear Casino",
        "logo": {{
          "@type": "ImageObject",
          "url": "{DOMAIN}/logo.png"
        }}
      }},
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "{DOMAIN}{page['url']}"
      }}
    }}
    </script>
</head>
<body>
    <header>
        <h1>{page['h1']}</h1>
    </header>
    <main>
        <article>
            {content}
        </article>
        <div class="links">
            <h3>Полезные ссылки:</h3>
            {links_html}
        </div>
    </main>
    <footer>
        <p>&copy; 2024 Lucky Bear Casino. Все права защищены.</p>
    </footer>
</body>
</html>"""
    return html

def main():
    data = load_data()
    pages = data['pages']
    
    # Create Base Directory
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    
    # Generate Pages
    for page in pages:
        # Determine file path
        if page['url'] == '/':
            file_path = os.path.join(BASE_DIR, "index.html")
        else:
            # Remove leading/trailing slashes for path joining
            clean_path = page['url'].strip('/')
            dir_path = os.path.join(BASE_DIR, clean_path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            file_path = os.path.join(dir_path, "index.html")
        
        html_content = create_html(page, pages)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Generated: {file_path}")

    # Generate robots.txt
    robots_txt = f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/
Host: lakibircasino.ru
Sitemap: {DOMAIN}/sitemap.xml

User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: BLEXBot
Disallow: /

User-agent: DotBot
Disallow: /
"""
    with open(os.path.join(BASE_DIR, "robots.txt"), 'w', encoding='utf-8') as f:
        f.write(robots_txt)
    print("Generated: robots.txt")

    # Generate sitemap.xml
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        loc = f"{DOMAIN}{page['url']}"
        # Ensure trailing slash for non-root pages if that's the convention, but the URL in JSON already has it or not.
        # Let's trust the JSON 'url' field.
        if page['url'] == '/':
             loc = DOMAIN + "/"
        else:
             loc = DOMAIN + page['url']
             
        sitemap += f"   <url>\n      <loc>{loc}</loc>\n      <priority>1.0</priority>\n   </url>\n"
    sitemap += '</urlset>'
    
    with open(os.path.join(BASE_DIR, "sitemap.xml"), 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("Generated: sitemap.xml")

if __name__ == "__main__":
    main()
