import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in environment variables")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Function to Generate Complaint Email using Gemini
async def generate_complaint_email(buyer_name: str, product_name: str, issue: str, complaint_id: str, image_url: str):
    prompt = f"""
    Generate a structured, professional email for an e-commerce complaint.
    
    Details:
    - Buyer: {buyer_name}
    - Product: {product_name}
    - Issue: {issue}
    - Complaint ID: {complaint_id}
    - Image URL (if applicable): {image_url}
    
    The email should include:
    - A polite introduction.
    - Summary of the issue.
    - Next steps for resolution.
    - Formal closing with support contact details.
    - The content should be concise, professional, and formatted in HTML.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    if response.text:
        return response.text
    else:
        return "Error generating email content."

# Function to Generate Order Confirmation Email
async def generate_order_email(buyer_name: str, order_id: str, items: list, total_price: float):
    items_text = "\n".join([f"- {item['name']} (Qty: {item['quantity']}, Price: ${item['price']})" for item in items])

    prompt = f"""
    Generate a structured, professional order confirmation email.

    Details:
    - Buyer: {buyer_name}
    - Order ID: {order_id}
    - Items: {items_text}
    - Total Price: ${total_price}

    The email should include:
    - A warm thank-you message.
    - Order summary.
    - Estimated delivery information.
    - Contact details for support.
    - The content should be concise, professional, and formatted in HTML.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    if response.text:
        return response.text
    else:
        return "Error generating email content."
