Insurance Policy Management System
This work implements a basic insurance policy management system using Python. The system manages policyholders, products, and payments.

Classes and Their Functions:

Policyholder:
register(): Registers a new policyholder.
suspend(): Suspends a policyholder's account.
reactivate(): Reactivates a suspended policyholder's account.
account_details(): Displays the policyholder's account information.
Product:
create(): Creates a new policy product.
update(): Updates an existing policy product.
remove(): Removes a policy product.
suspend(): Suspends a policy product.
Payment:
process(): Processes a payment for a policy.
send_reminder(): Sends a payment reminder to a policyholder.
apply_penalty(): Applies a penalty for a late payment.

Usage:

Create policyholders and products:

policyholder1 = Policyholder("Denyse", "Kicukiro-Gikondo", "0785674564", [])
policyholder2 = Policyholder("Jean", "Kenya-Nairobi", "0798657432", [])

product1 = Product("Property Insurance", "offer property protection, including structural damage, theft of personal belongings, and liability coverageh", 100)
product2 = Product("Health Insurance", "Covers medical expenses", 200)

Register policyholders and pay for products:

policyholder1.register()
policyholder1.policy_products.append(product1)
policyholder2.register()
policyholder2.policy_products.append(product2)

payment1 = Payment(100, datetime.date.today(), policyholder1)
payment1.process()

payment2 = Payment(200, datetime.date.today(), policyholder2)
payment2.process()

Display account details:

policyholder1.account_details()
policyholder2.account_details()
