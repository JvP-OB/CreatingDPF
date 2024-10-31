from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import datetime

def create_pdf(sender_details, recipient_name, recipient_details, statement_data, transactions):
    current_time = datetime.datetime.now()
    filename = f"Statement_{current_time.strftime('%Y%m%d%H%M')}.pdf"

    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Sender Header
    sender_text = f"<b>{sender_details['name']}</b><br/>{sender_details['address']}<br/>TEL: {sender_details['tel']}  FAX: {sender_details['fax']}  EMAIL: {sender_details['email']}"
    header = Paragraph(sender_text, styles['Normal'])
    story.append(header)
    story.append(Spacer(1, 12))

    # Recipient Details
    recipient_text = f"<b>TO: {recipient_name}</b><br/>{recipient_details['address']}<br/>TEL: {recipient_details['tel']}  FAX: {recipient_details['fax']}"
    recipient = Paragraph(recipient_text, styles['Normal'])
    story.append(recipient)
    story.append(Spacer(1, 12))

    # Statement Data
    dates_text = f"<b>STATEMENT DATE:</b> {current_time.strftime('%B %d, %Y')}<br/><b>STATEMENT PERIOD:</b> {statement_data['period']}<br/><b>CURRENCY:</b> {statement_data['currency']}<br/><b>PREVIOUS BALANCE:</b> {statement_data['previous_balance']}<br/><b>BALANCE DUE:</b> {statement_data['balance_due']}"
    dates = Paragraph(dates_text, styles['Normal'])
    story.append(dates)
    story.append(Spacer(1, 12))

    # Transactions Table
    table_data = [['DATE', 'FILING NO.', 'YOUR REF. NO.', 'B/L NO.', 'D/C No.', 'DEBIT', 'CREDIT', 'PAID', 'BALANCE']] + transactions
    table = Table(table_data, colWidths=[doc.width/9.]*9)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ]))
    story.append(table)

    # Grand Total
    grand_total_text = f"<b>GRAND TOTAL:</b> {statement_data['grand_total']}"
    grand_total = Paragraph(grand_total_text, styles['Normal'])
    story.append(Spacer(1, 12))
    story.append(grand_total)

    # Remark and Footer
    remark_text = "REMARK: "
    remark = Paragraph(remark_text, styles['Normal'])
    story.append(remark)
    story.append(Spacer(1, 12))

    footer_text = "OCEAN BLUE EXPRESS INC. Page number: 1"
    footer = Paragraph(footer_text, styles['Normal'])
    story.append(footer)

    # Generate PDF
    doc.build(story)

# Example data placeholders
sender_details = {
    'name': 'OCEAN BLUE EXPRESS INC',
    'address': '255 W. VICTORIA ST., COMPTON, CA 90220',
    'tel': '310-719-2500',
    'fax': '310-719-2510',
    'email': 'jvpark@oceanbluexp.com'
}

recipient_name = input("Enter the recipient name: ")
recipient_details = {
    'address': 'Placeholder Address',
    'tel': 'Placeholder Telephone',
    'fax': 'Placeholder Fax'
}

statement_data = {
    'period': '09/01/2024 ~ 09/30/2024',
    'currency': 'USD',
    'previous_balance': '-403,418.00',
    'balance_due': '3,468.51',
    'grand_total': 'USD 24,792.51'
}

transactions = [
    ['09/12/2024', 'NYOBOI-52560', 'JSCH2408201', '53211', '', '2,248.35', '0.00', '0.00', '2,248.35'],
    # More transactions...
]

# Call the function with placeholders
create_pdf(sender_details, recipient_name, recipient_details, statement_data, transactions)
