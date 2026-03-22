## Blockchain-Based Voting System (Django)

This project is a secure and transparent voting system built using Django and basic blockchain principles. It demonstrates how blockchain can be applied to digital voting to ensure data integrity, transparency, and tamper-proof vote storage.

### Features

* Aadhaar-based voter authentication
* OTP verification via email
* Unique private key generation for each vote
* Secure vote casting with digital signature
* Blockchain-based storage of votes
* Block mining with proof-of-work mechanism
* Vote verification and result display
* Admin panel for managing voters and parties
* Dynamic dummy data generation for testing

### How It Works

1. User logs in using Aadhaar number
2. OTP is sent to registered email for verification
3. After verification, a unique private key is generated
4. User casts vote securely
5. Vote is hashed and stored in a blockchain block
6. Blocks are mined and added to the chain
7. Results are displayed with vote counts and rankings

### Tech Stack

* Python
* Django
* SQLite (default database)
* HTML, CSS, JavaScript
* SMTP (Email integration)

### Note

* OTP and private key delivery are handled via email for realistic simulation
* This is a prototype system intended for educational purposes

### Usage

1. Run the server
2. Enter Aadhaar number
3. Verify OTP from email
4. Cast vote using generated private key
5. Mine blocks and view results

---

This project showcases the practical application of blockchain concepts in building a secure digital voting system.
