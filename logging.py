# logging.py
def log_attack(address, data):
    with open('attacks.log', 'a') as log_file:
        log_file.write(f"Attack from {address[0]}:{address[1]} - Data: {data.decode('utf-8')}\n")
