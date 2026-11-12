import sys

def add_analytics_to_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Analytics script to add
    analytics_script = """  <!-- Vercel Web Analytics -->
  <script>
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
  </script>
  <script defer src="/_vercel/insights/script.js"></script>
"""
    
    # Find </head> and insert before it
    if '</head>' in content:
        content = content.replace('</head>', analytics_script + '</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully added analytics to {filepath}")
        return True
    else:
        print(f"Could not find </head> in {filepath}")
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        add_analytics_to_html(sys.argv[1])
    else:
        print("Usage: python add_analytics.py <filepath>")
