import dns.resolver
import sys


record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']

try:
    domain = sys.argv[1]
except IndexError:
    print('[!]\tUsage: python3 dnsdemo.py <domain name>')
    quit()

for record in record_types:
    try:
        answer = dns.resolver.resolve(domain, record)
        print(f'\n{record} Records')
        print('=' * 80)
        for server in answer:
            print(server.to_text())
    except dns.resolver.NoAnswer as e: 
        print('\n[!]\tAn error occured:')
        print(e)
    except dns.resolver.NXDOMAIN as e:
        print('\n[!]\tAn error occured:')
        print(e)
        print(f'{domain} does not exist.')
    except KeyboardInterrupt:
        print('\n[!]\tProgram terminating.')
        quit()
