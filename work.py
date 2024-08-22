from Policyholder import Policyholder
from Product import Product
from Payment import Payment
import datetime

# Create policyholders and products
policyholder1 = Policyholder("Denyse", "Kicukiro-Gikondo", "0785674564", [])
policyholder2 = Policyholder("Jean", "Kenya-Nairobi", "0798657432", [])

product1 = Product("Property Insurance", "offer property protection, including structural damage, theft of personal belongings, and liability coverageh", 100)
product2 = Product("Health Insurance", "Covers medical expenses", 200)

# Register policyholders and pay for products
policyholder1.register()
policyholder1.policy_products.append(product1)
policyholder2.register()
policyholder2.policy_products.append(product2)

# Process payments
payment1 = Payment(100, datetime.date.today(), policyholder1)
payment1.process()

payment2 = Payment(200, datetime.date.today(), policyholder2)
payment2.process()

# Display account details
policyholder1.account_details()
policyholder2.account_details()
