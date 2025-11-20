"""
Project configuration settings
This file contains content types, tones, and other constant values
"""

# Groq API settings
XAI_API_BASE = "https://api.x.ai/v1"
XAI_MODEL = "grok-beta"

# Content types and descriptions
CONTENT_TYPES = {
    "Blog Post": "Long-form, SEO-friendly, informative content",
    "Product Description": "Sales-focused, concise, persuasive text",
    "Social Media": "Short, attention-grabbing, engagement-focused",
    "Email": "Professional, clear, action-oriented",
    "Creative Writing": "Narrative-focused, original, flowing story"
}

# Tone options
TONE_OPTIONS = {
    "Professional": "Suitable for business, serious and reliable",
    "Friendly": "Casual, relaxed and approachable",
    "Formal": "Corporate, serious and authoritative",
    "Creative": "Original, different and inspiring",
    "Informative": "Educational, explanatory and clear"
}

# Length options (word count)
LENGTH_OPTIONS = {
    "Short": (100, 200),
    "Medium": (300, 500),
    "Long": (600, 1000)
}