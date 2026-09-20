"""Generate the original, self-contained SVG portfolio cards. No dependencies."""
from pathlib import Path
from html import escape

root = Path(__file__).parent
cards = [
    ('foodbridge', '01 / BACKEND ENGINEERING', 'FoodBridge', 'Food redistribution platform', 'Go · Echo · PostgreSQL · Docker', '#77e4c8', 'API'),
    ('togeta', '02 / TEAM DEVELOPMENT', 'Togeta', 'Find people. Share activities.', 'C# · ASP.NET MVC · SQL Server', '#a7baff', '</>'),
    ('drugbrief', '03 / AI INTEGRATION', 'DrugBrief', 'Drug information, with sources', 'TypeScript · React · OpenRouter', '#f5cc89', 'AI'),
    ('boardbased', '04 / WEB & DATA', 'BoardBased', 'Discover your next board game', 'React · Node.js · Python', '#9edaf0', '{}'),
]
for slug, label, title, desc, stack, accent, icon in cards:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="240" viewBox="0 0 600 240" role="img" aria-label="{escape(title)}: {escape(desc)}">
<rect x="1" y="1" width="598" height="238" rx="15" fill="#101c2d" stroke="#2a3c51"/>
<rect x="26" y="28" width="4" height="19" rx="2" fill="{accent}"/>
<g font-family="Segoe UI,Arial,sans-serif">
<text x="42" y="43" font-size="13" letter-spacing="2" fill="{accent}">{escape(label)}</text>
<text x="30" y="102" font-size="36" font-weight="700" fill="#f2f6fc">{escape(title)}</text>
<text x="30" y="140" font-size="20" fill="#b9c9de">{escape(desc)}</text>
<path d="M30 165H570" stroke="#2a3c51"/>
<text x="30" y="202" font-size="17" fill="{accent}">{escape(stack)}</text>
<text x="531" y="99" font-size="28" text-anchor="middle" fill="{accent}" opacity=".75">{escape(icon)}</text>
</g></svg>'''
    (root / f'{slug}.svg').write_text(svg, encoding='utf-8')

labels = [('Go', 69), ('Python', 105), ('C#', 69), ('PostgreSQL', 148), ('Docker', 108), ('AWS', 82), ('LLM integration', 187)]
x = 1
parts = []
for label, width in labels:
    parts.append(f'<rect x="{x}" y="1" width="{width}" height="38" rx="7" fill="#14243a" stroke="#344b65"/><text x="{x+width/2}" y="26" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="16" fill="#d2e8f7">{escape(label)}</text>')
    x += width + 9
(root / 'stack.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{x}" height="40" viewBox="0 0 {x} 40" role="img" aria-label="Go, Python, C sharp, PostgreSQL, Docker, AWS, LLM integration">'+''.join(parts)+'</svg>', encoding='utf-8')
