# 2domain - by: proxlu

import sys
import itertools
import whois
from tqdm import tqdm

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return True
        else:
            return False
    except whois.parser.PywhoisError:
        return True

def generate_domains(extension):
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    domains = []

    for combo in itertools.product(chars, repeat=2):
        domain = ''.join(combo) + extension
        domains.append(domain)

    return domains

extension = None
if len(sys.argv) == 2:
    extension = sys.argv[1]
else:
    extension = input("Digite a extensão do domínio (exemplo: .com): ")

available_domains = []
domains = generate_domains(extension)

print("Verificando a disponibilidade de domínios:")
for domain in tqdm(domains):
    if check_domain_availability(domain):
        available_domains.append(domain)

print("\nDomínios disponíveis:")
for domain in available_domains:
    print(domain)
