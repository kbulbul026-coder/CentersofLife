# app.py
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# --- 1. JSON Data for D3.js Mind Map ---
MIND_MAP_JSON = {
  "name": "You / Self-Identification",
  "icon": "👤",
  "children": [
    {
      "name": "Principles Center 🌟",
      "color": "blue",
      "children": [
        {"name": "Spouse/Partner", "icon": "🤝", "value": "Equal partner in a mutually beneficial interdependent relationship"},
        {"name": "Family", "icon": "🏡", "value": "Sacred stewardship and responsibility"},
        {"name": "Friends", "icon": "🌱", "value": "Companions in growth and shared values"},
        {"name": "Work", "icon": "🧭", "value": "Opportunity to contribute meaningfully and ethically"},
        {"name": "Possessions", "icon": "✨", "value": "Tools to contribute or manage responsibly"},
        {"name": "Community/Church", "icon": "🙏", "value": "Platform for service and shared moral commitment"},
        {"name": "Self", "icon": "🧘", "value": "Focus on growth, contribution, and character development"}
      ]
    },
    {
      "name": "Self Center",
      "color": "purple",
      "children": [
        {"name": "Spouse/Partner", "icon": " Narcissus", "value": "Someone who should meet my needs and validate my identity"},
        {"name": "Family", "icon": "👪", "value": "Extensions of myself; source of unconditional approval"},
        {"name": "Friends", "icon": "🙌", "value": "People who admire and affirm my choices"},
        {"name": "Work", "icon": "🗣️", "value": "Platform for self-expression and recognition"},
        {"name": "Possessions", "icon": "💎", "value": "Symbols that reflect my unique taste and status"},
        {"name": "Community/Church", "icon": "🎙️", "value": "Venue for performing my role or seeking attention"},
        {"name": "Self", "icon": "👑", "value": "The primary focus and source of all goals"}
      ]
    },
    {
      "name": "Work Center",
      "color": "orange",
      "children": [
        {"name": "Spouse/Partner", "icon": "🛠️", "value": "Support system for career success; handles domestic distractions"},
        {"name": "Family", "icon": "💼", "value": "Dependents relying on my productivity; reason for long hours"},
        {"name": "Friends", "icon": "🤝", "value": "Networking contacts or people who advance my career"},
        {"name": "Work", "icon": "📈", "value": "The central duty and main source of identity and security"},
        {"name": "Possessions", "icon": "💰", "value": "Rewards for hard work; symbols of achievement"},
        {"name": "Community/Church", "icon": "📢", "value": "Place to showcase professional leadership or network"},
        {"name": "Self", "icon": "⌚", "value": "Defined by titles, accomplishments, and efficiency"}
      ]
    },
    {
      "name": "Family Center",
      "color": "green",
      "children": [
        {"name": "Spouse/Partner", "icon": "💍", "value": "Core member of family unit; role-based loyalty"},
        {"name": "Family", "icon": "🔒", "value": "The ultimate source of security and the main priority in all decisions"},
        {"name": "Friends", "icon": "🏡", "value": "Extensions of family circle; people who fit into the family unit"},
        {"name": "Work", "icon": "📝", "value": "Duty to provide for family; measured by financial stability"},
        {"name": "Possessions", "icon": "🖼️", "value": "Assets to be inherited or managed for the family's welfare"},
        {"name": "Community/Church", "icon": "👨‍👩‍👧‍👦", "value": "Place to reinforce family traditions and values"},
        {"name": "Self", "icon": "🛡️", "value": "Defined by my role (Parent, Spouse, Provider) within the family"}
      ]
    },
    {
      "name": "Pleasure Center",
      "color": "red",
      "children": [
        {"name": "Spouse/Partner", "icon": "🥳", "value": "Source of fun, excitement, or sensual gratification"},
        {"name": "Family", "icon": "🍹", "value": "Companions for enjoyment and leisure; source of effortless fun"},
        {"name": "Friends", "icon": "🎈", "value": "People to party with; temporary companions for entertainment"},
        {"name": "Work", "icon": "💸", "value": "Means to afford pleasures; distraction from boredom"},
        {"name": "Possessions", "icon": "🎮", "value": "Toys and tools that maximize enjoyment and comfort"},
        {"name": "Community/Church", "icon": "📺", "value": "Avoided, unless it offers effortless enjoyment or entertainment"},
        {"name": "Self", "icon": "😋", "value": "Focused on comfort, instant gratification, and sensory input"}
      ]
    },
    {
      "name": "Possessions Center",
      "color": "yellow",
      "children": [
        {"name": "Spouse/Partner", "icon": "💎", "value": "Status symbol or extension of personal success"},
        {"name": "Family", "icon": "🏦", "value": "Assets to be inherited or managed; must not damage property"},
        {"name": "Friends", "icon": " admiring", "value": "People who admire my possessions and appreciate my success"},
        {"name": "Work", "icon": "🏆", "value": "The means to acquire, protect, and enhance assets"},
        {"name": "Possessions", "icon": "🏠", "value": "The main focus of security, guidance, and pride"},
        {"name": "Community/Church", "icon": "🖼️", "value": "Place to display wealth and reinforce social standing"},
        {"name": "Self", "icon": "🔑", "value": "Worth is tied directly to net worth and material holdings"}
      ]
    }
  ]
}

# --- 2. Legend Data ---
# This data is used to render the color key in the HTML template.
CENTER_LEGEND = [
    {"name": "Principles Center", "color": "blue"},
    {"name": "Self Center", "color": "purple"},
    {"name": "Work Center", "color": "orange"},
    {"name": "Family Center", "color": "green"},
    {"name": "Pleasure Center", "color": "red"},
    {"name": "Possessions Center", "color": "yellow"}
]

# --- 3. Routes ---

@app.route('/')
def index():
    return '<h1>Covey\'s Centers of Life</h1><p>Navigate to <a href="/mindmap">/mindmap</a> to see the interactive D3.js visualization!</p>'

# Route to render the HTML template, passing the legend data
@app.route('/mindmap')
def mind_map():
    # Renders the mind_map.html file and passes the LEGEND data for the Jinja loop
    return render_template('mind_map.html', legend_data=CENTER_LEGEND)

# API endpoint to serve the JSON data to the D3.js script
@app.route('/api/data')
def api_data():
    return jsonify(MIND_MAP_JSON)

# --- 4. Run Application ---
if __name__ == '__main__':
    app.run(debug=True)
